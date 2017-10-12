'''
Title: Reinforcement Learning and Deep Q-Network 101
File: pong_game_control.py
Description: The game control center
Company: Artificial Intelligence Research Institute (AIRI)
Author: Channy Hong

'''

import sys, os
import pong
import dqn

# pong game control function
def pong_game_control(player_one, player_two, display_on, title_text, pygame_event, is_challenge_gameplay, trained_steps=None):
	pong_game = pong.Gameplay(player_one, player_two, title_text, pygame_event, is_challenge_gameplay, trained_steps)
	frame = pong_game.get_initial_frame(display_on)
	
	# main game loop if no dqn player
	if player_one != 2 and player_two != 2:
		while True:
			player_one_reward, player_two_reward, _ = pong_game.get_next_frame([0,0,0],[0,0,0],display_on)

	# player 1 is dqn player
	if player_one == 2:
		# create input and output layers
		player_one_input_layer, player_one_output_layer = dqn.create_graph()
		# train the graph on the input and ooutput layer with session variables
		dqn.train_graph(pong_game, 1, display_on, player_one_input_layer, player_one_output_layer, trained_steps)

	# player 2 is dqn player
	if player_two == 2:
		# create input and output layers
		player_two_input_layer, player_two_output_layer = dqn.create_graph()
		# train the graph on the input and ooutput layer with session variables
		dqn.train_graph(pong_game, 2, display_on, player_two_input_layer, player_two_output_layer, trained_steps)

