'''
Title: Reinforcement Learning and Deep Q-Network 101
File: dqn.py
Description: This implemenens the Deep Q-Network used by the DQN Agent, with input and output
                specifications specialized for 'Pong' gameplay
Company: Artificial Intelligence Research Institute (AIRI)
Author: Channy Hong
'''

import tensorflow as tf
import cv2
import pong
import numpy as np
import random 
import os

from collections import deque
from numpy.random import choice


# turn off tensorflow log information
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'



# hyperparameters 

# up, stay, down
ACTIONS = 3 
# discount factor
GAMMA = 0.99 
# annealing schedule
INITIAL_EPSILON = 1.0
FINAL_EPSILON = 0.05
EXPLORE_STEPS = 500000
# number of initial steps to explore before training
OBSERVE_STEPS = 1000
# training v. testing (False = training)
USE_MODEL = True
# save interval
SAVE_STEP = 1000000
# replay memory and batch size
REPLAY_MEMORY_SIZE = 200000
BATCH = 100

# create tensorflow graph
def create_graph():
    with tf.device('/cpu:0'):

        # define layers
        W_conv1 = tf.Variable(tf.truncated_normal([6, 6, 4, 32], stddev=0.02))
        b_conv1 = tf.Variable(tf.constant(0.01, shape=[32]))

        W_conv2 = tf.Variable(tf.truncated_normal([4, 4, 32, 64], stddev=0.02))
        b_conv2 = tf.Variable(tf.constant(0.01, shape=[64]))

        W_conv3 = tf.Variable(tf.truncated_normal([3, 3, 64, 64], stddev=0.02))
        b_conv3 = tf.Variable(tf.constant(0.01, shape=[64]))

        W_fc4 = tf.Variable(tf.truncated_normal([1024, 512], stddev=0.02))
        b_fc4 = tf.Variable(tf.constant(0.01, shape=[512]))

        W_fc5 = tf.Variable(tf.truncated_normal([512, ACTIONS], stddev=0.02))
        b_fc5 = tf.Variable(tf.constant(0.01, shape=[ACTIONS]))

        # input tensor
        s = tf.placeholder("float", [None, 60, 60, 4])

        # configure layers
        conv1 = tf.nn.relu(tf.nn.conv2d(s, W_conv1, strides = [1, 4, 4, 1], padding = "SAME") + b_conv1)

        pool1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")

        conv2 = tf.nn.relu(tf.nn.conv2d(pool1, W_conv2, strides = [1, 2, 2, 1], padding = "SAME") + b_conv2)

        conv3 = tf.nn.relu(tf.nn.conv2d(conv2, W_conv3, strides = [1, 1, 1, 1], padding = "SAME") + b_conv3)

        conv3_flat = tf.reshape(conv3, [-1, 1024])

        fc4 = tf.nn.relu(tf.matmul(conv3_flat, W_fc4) + b_fc4)
        
        fc5 = tf.matmul(fc4, W_fc5) + b_fc5

        return s, fc5


# train tensorflow graph
def train_graph(game, player, display_on, inp, out, trained_steps):

    # define variables
    argmax = tf.placeholder("float", [None, ACTIONS]) 
    ground_truth = tf.placeholder("float", [None])
    global_step = tf.Variable(0, name='global_step')

    action = tf.reduce_sum(tf.multiply(out, argmax), reduction_indices = 1)
    cost = tf.reduce_mean(tf.square(action - ground_truth))

    train_step = tf.train.AdamOptimizer(1e-6).minimize(cost)
    
    replay_memory = deque()

    # get, intial frame from 'Pong', process image, and stack frames
    frame = game.get_initial_frame(display_on)
    frame = cv2.cvtColor(cv2.resize(frame, (60, 60)), cv2.COLOR_BGR2GRAY)
    _, frame = cv2.threshold(frame, 1, 255, cv2.THRESH_BINARY)
    inp_t = np.stack((frame, frame, frame, frame), axis = 2)

    # saver and session manager
    saver = tf.train.Saver(tf.global_variables(), max_to_keep=None)    
    session = tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
    checkpoint_path = "./checkpoint_" + trained_steps
    checkpoint = tf.train.latest_checkpoint(checkpoint_path)
    if checkpoint != None:
        saver.restore(session, checkpoint)
    else:
        init = tf.global_variables_initializer()
        session.run(init)

    t = global_step.eval()   
    c = 0
    
    epsilon = INITIAL_EPSILON

    avg_max_q = 0
    
    # main training loop
    while(1):
        out_t = out.eval(feed_dict = {inp : [inp_t]})[0] # output tensor
        argmax_t = np.zeros([ACTIONS]) # argmax tensor
        reward_t = 0 # reward tensor

        # choose action to take (random if epsilon)
        if(random.random() <= epsilon and not USE_MODEL):
            maxIndex = choice((0,1,2), 1, p=(0.9, 0.05, 0.05)) # make 0 the most choosen action for realistic randomness
        else:
            maxIndex = np.argmax(out_t)

        # set action to take
        argmax_t[maxIndex] = 1
        
        # anneal epsilon according to cooling schedule
        if epsilon > FINAL_EPSILON:
            epsilon -= (INITIAL_EPSILON - FINAL_EPSILON) / EXPLORE_STEPS

        # get next frame (state) and reward from the resulting state
        if player == 1:
            reward_t, _, frame = game.get_next_frame(argmax_t, None, display_on)
        elif player == 2:
            _, reward_t, frame = game.get_next_frame(None, argmax_t, display_on)

        # process state
        frame = cv2.cvtColor(cv2.resize(frame, (60, 60)), cv2.COLOR_BGR2GRAY)
        _, frame = cv2.threshold(frame, 1, 255, cv2.THRESH_BINARY)
        frame = np.reshape(frame, (60, 60, 1))
        
        updated_inp_t = np.append(frame, inp_t[:, :, 0:3], axis = 2) # updated input tensor
        
        # add our input, argmax, reward, and updated input tensors to replay memory
        replay_memory.append((inp_t, argmax_t, reward_t, updated_inp_t))

        # if we run out of replay memory, make room
        if len(replay_memory) > REPLAY_MEMORY_SIZE:
            replay_memory.popleft()
        
        # training update iteration
        if c > OBSERVE_STEPS and not USE_MODEL:

            # get values from our replay memory
            minibatch = random.sample(replay_memory, BATCH)
        
            inp_batch = [dim[0] for dim in minibatch]
            argmax_batch = [dim[1] for dim in minibatch]
            reward_batch = [dim[2] for dim in minibatch]
            updated_inp_t_batch = [dim[3] for dim in minibatch]
        
            ground_truth_batch = []

            out_batch = out.eval(feed_dict = {inp : updated_inp_t_batch})
            
            # add values to the batch
            for i in range(0, len(minibatch)):
                ground_truth_batch.append(reward_batch[i] + GAMMA * np.max(out_batch[i]))

            # train the model
            train_step.run(feed_dict = {ground_truth : ground_truth_batch,
                                        argmax : argmax_batch,
                                        inp : inp_batch})
        
        # next frame
        inp_t = updated_inp_t
        t = t + 1   
        c = c + 1     

        # save model at set intervals
        if t % SAVE_STEP == 0 and not USE_MODEL:
            session.run(global_step.assign(t))            
            saver.save(session, './checkpoints/model.ckpt', global_step=t)    

