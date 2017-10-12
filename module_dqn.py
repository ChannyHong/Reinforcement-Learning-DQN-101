'''
Title: Reinforcement Learning and Deep Q-Network 101
File: module_dqn.py
Description: This is the Deep Q-Network module
Company: Artificial Intelligence Research Institute (AIRI)
Author: Channy Hong

'''
import Tkinter as tk
import pong_game_control as pgc

import module_frame_base as frame_base
import module_prelude as prelude

import module_q as q
import module_challenge as challenge

import event_handler as eh
from PIL import Image, ImageTk
import image_manipulator as im
import video_animation as va





'''
The Large Problem With Pixel Input

This frame consists of:
- explanation of what the problem is from the Q-Learning algorithm initialization as discussed
previously

The purpose of this frame is to show the users how the current Q-Learning algorithm is
unrealistic.
'''
class the_large_problem_with_pixel_input_frame(frame_base.frame_base):
    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        
        # add widgets
        self.title = tk.Label(self, text="The Large Problem With Pixel Input", font=("Courier", 48))

        self.text1 = tk.Label(self, font=("Courier", 16), wraplength=1000, justify=tk.LEFT, text="But right from the beginning, we encounter a very large problem. Literally. Think about the input that our computer player receives. The information from the game that our 'Q-Learning' player receives is a 600x400 pixel gameplay screen. Assuming that each pixel can be either white or black, that leaves our computer player with a total of 2600 x 400 state spaces to work with.")

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(q.action_value_function_revisited_discount_factor_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(q_network_frame),
                                    text="Next", font=("Courier", 14))
        
        # add toggle texts (args: self, master, text_string, width=1, height=1, wraplength=None, justify=LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        self.text2 = eh.toggle_label(self, "So, when our Q-Learning Agent iterates through every possible (state, action) pair and initialize each action-value as 0, it would have to do it 2600 x 400 times!", 
            wraplength=1000, font_size=16, row=2, column=1)

        input_problem_image_scale = 0.64
        input_problem_image_path = 'media/module_dqn/the_large_problem_with_pixel_input_frame/input_problem.png'
        self.input_problem_image = ImageTk.PhotoImage(im.scale_image(Image.open(input_problem_image_path), input_problem_image_scale))
        self.image_one = eh.toggle_image(self, image=self.input_problem_image, 
            row=3, column=1, width=600, height=200)

        self.text3 = eh.toggle_label(self, "Storing pixel data state by state becomes problematic very quickly. For example, if we assume black and white binary pixels, even a 20 x 20 screen would leave us with 2^400 = 2.58 x 10^120 states. To give you some perspective, there are estimated to be around 10^80 atoms in the entire universe.", 
            wraplength=1000, font_size=16, row=4, column=1)



        # lay widgets
        self.title.grid(row=0, 
                        column=0, 
                        columnspan=3)

        self.text1.grid(row=1, column=1)

        self.previous_frame_button.grid(row=5, 
                                        column=0, 
                                        padx=10, 
                                        sticky=tk.W)
        self.to_roadmap_button.grid(row=5, 
                                    column=1, 
                                    columnspan=1)
        self.next_frame_button.grid(row=5, 
                                    column=7, 
                                    padx=10, 
                                    sticky=tk.E)











'''
Q-Network

This frame consists of:
- explanation of how a Q-Network works
- supporting image

The purpose of this frame is to show the users how the Q-Network works, and to show how the 
problem of Q-Learning algorithm initialization is solved.
'''
class q_network_frame(frame_base.frame_base):
    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        
        # add widgets
        self.title = tk.Label(self, text="Q-Network", font=("Courier", 48))

        self.row_one_frame = tk.Frame(self)
        self.text1 = tk.Label(self.row_one_frame, font=("Courier", 16), wraplength=500, justify=tk.LEFT, text="Ok, then. Let's change our strategy and go back to how we think. Remember our strategy? Let's take a look at its language.")

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(the_large_problem_with_pixel_input_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(q_network_training_sequence_frame), self.controller.frames[q_network_training_sequence_frame].video_animation.open_video()],
                                    text="Next", font=("Courier", 14))
        
        # add toggle texts (args: self, master, text_string, width=1, height=1, wraplength=None, justify=LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        self.text2 = eh.toggle_label(self.row_one_frame, "- Where the ball is going to end up when it gets to my paddle, based on current trajectory\n- Where my paddle is currently at", 
            wraplength=500, font_size=16, row=0, column=1, width=50)
        self.text3 = eh.toggle_label(self, "So, we were never thinking about the pixel input of each frame to begin with. Rather, we were identifying the characteristics of various key objects in the screen and calculating what that meant for our ability to gain reward.", 
            wraplength=1000, font_size=16, row=2, column=1, width=80)
        self.text4 = eh.toggle_label(self, "And this is exactly where neural networks come in for the rescue! Neural network is meant to predict values from an input.", 
            wraplength=1000, font_size=16, row=3, column=1)

        q_network_image_scale = 0.5
        q_network_image_path = 'media/module_dqn/q_network_frame/q_network.png'
        self.q_network_image = ImageTk.PhotoImage(im.scale_image(Image.open(q_network_image_path), q_network_image_scale))
        self.q_network = eh.toggle_image(self, image=self.q_network_image, 
            row=4, column=1, width=800, height=300)

        # lay widgets
        self.title.grid(row=0, 
                        column=0, 
                        columnspan=3)

        self.row_one_frame.grid(row=1, column=1)
        self.text1.grid(row=0, column=0)

        self.previous_frame_button.grid(row=5, 
                                        column=0, 
                                        padx=0, 
                                        sticky=tk.W)
        self.to_roadmap_button.grid(row=5, 
                                    column=1, 
                                    columnspan=1)
        self.next_frame_button.grid(row=5, 
                                    column=2, 
                                    padx=0, 
                                    sticky=tk.E)





'''
Q-Network: Training Sequence

This frame consists of:
- animation that details what the training sequence looks like in this new Deep Q-Learning 
algorithm

The purpose of this frame is to show how the training is carried out in this Deep Q-Learning
algorithm.
'''
class q_network_training_sequence_frame(frame_base.frame_base):
    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        
        # add widgets
        self.title = tk.Label(self, text="Q-Network: Training Sequence", font=("Courier", 48))
        
        self.text1 = tk.Label(self, font=("Courier", 16), justify=tk.LEFT, wraplength=1000, text="Let's see how our agent will update its Q-Network during gameplay:")

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(q_network_frame), self.video_animation.close_video()],
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(prelude.roadmap_frame), self.video_animation.close_video()],
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(replay_memory_frame), self.video_animation.close_video()],
                                    text="Next", font=("Courier", 14))
        
        # add and lay video animation widget
        self.video_animation = va.video_animation(self, 2, 2, 1, 1, 3, 1, 600, 450, "media/module_dqn/q_network_training_sequence_frame/q_network_training_sequence.mov", False, self)

        # lay widgets
        self.title.grid(row=0, 
                        column=0, 
                        columnspan=3)

        self.text1.grid(row=1, column=1)

        self.previous_frame_button.grid(row=4, 
                                        column=0, 
                                        padx=20, 
                                        sticky=tk.W)
        self.to_roadmap_button.grid(row=4, 
                                    column=1, 
                                    columnspan=2)
        self.next_frame_button.grid(row=4, 
                                    column=2, 
                                    padx=20, 
                                    sticky=tk.E)








'''
Replay Memory

This frame consists of:
- explanation of how the replay memory is used to enhance the performance of the Deep
Q-Learning algorithm

The purpose of this frame is to explain to the users the role of replay memory in Deep
Q-Learning algorithm.
'''
class replay_memory_frame(frame_base.frame_base):
    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        
        # add widgets
        self.title = tk.Label(self, text="Replay Memory", font=("Courier", 48))

        self.text1 = tk.Label(self, font=("Courier", 16), justify=tk.LEFT, wraplength=1000, text="However, our Deep Q-Network algorithm is not without its faults. As it turns out, because it trains the model at every time step, the model is prone to very short sighted reflection, meaning that it doesn't look far back in the past to learn the best way of choosing its actions.")

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(q_network_training_sequence_frame), self.controller.frames[q_network_training_sequence_frame].video_animation.open_video()],
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(challenge.challenge_dqn_player_frame),
                                    text="Next", font=("Courier", 14))
        

        # add + lay toggle widgets (args: self, master, text_string, width=1, height=1, wraplength=None, justify=tk.LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        self.text2 = eh.toggle_label(self, "Let us say for example that after a good amount of updating and training, our Deep Q-Learning algorithm comes across by chance two non-trivial action-value update instances back to back while pressing down in the bottom corner. This may cause the algorithm to develop a bias towards pursuing this seemingly rewarding (state, action) pair, which is certainly not a winning strategy.", 
            row=2, column=1, wraplength=1000)
        self.text3 = eh.toggle_label(self, "In 2013, Google's Deepmind developed a technique to effectively combat this short term bias, and it was achieved by introducing the concept of replay memory. Quite simply, replay memory is a storage of action-observation information that goes far back in the future, and every training iteration trains over a 'batch' of randomly chosen episodes from that replay memory, rather than each immediate past episodes.", 
            row=3, column=1, wraplength=1000)
        self.text4 = eh.toggle_label(self, "Congratulations, we now have our fully-functional Deep Q-Network algorithm!", 
            row=4, column=1, wraplength=1000)

        # lay widgets
        self.title.grid(row=0, 
                        column=0, 
                        columnspan=8)

        self.text1.grid(row=1, column=1)

        self.previous_frame_button.grid(row=5, 
                                        column=0, 
                                        padx=10, 
                                        sticky=tk.W)
        self.to_roadmap_button.grid(row=5, 
                                    column=1, 
                                    columnspan=1)
        self.next_frame_button.grid(row=5, 
                                    column=2, 
                                    padx=10, 
                                    sticky=tk.E)
