'''
Title: Reinforcement Learning and Deep Q-Network 101
File: module_frame_base.py
Description: Definition of prelude pages (title and roadmap)
Company: Artificial Intelligence Research Institute (AIRI)
Author: Channy Hong

'''
import Tkinter as tk
from PIL import Image, ImageTk

import module_frame_base as frame_base

import module_intro as intro
import module_play as play
import module_q as q
import module_dqn as dqn
import module_challenge as challenge

import image_manipulator as im


'''
Title

This frame consists of:
- the title

The purpose of this frame is to serve as the title page of this tutorial.
'''
class title_frame(frame_base.frame_base):
    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=6)
        self.columnconfigure(2, weight=2)
        self.rowconfigure(0, weight=7)
        self.rowconfigure(1, weight=1)

        # add logo image specification
        pathway_image_scale = 0.5
        self.logo_image_path = 'media/module_prelude/title/airi_logo.png'
        self.logo_image = ImageTk.PhotoImage(im.scale_image(Image.open(self.logo_image_path), pathway_image_scale))
    

        # add widgets
        self.title = tk.Label(self, text="Reinforcement Learning\n&\nDeep Q-Learning\n101", font=("Courier", 48))
        self.logo_image_label = tk.Label(self, image=self.logo_image)
        self.author = tk.Label(self, text="Author: Channy Hong", font=("Courier", 14))
        self.button_to_roadmap = tk.Button(self,
                                     command=lambda: self.controller.show_frame(roadmap_frame),
                                     text="To Roadmap", font=("Courier", 14))

        # lay widgets
        self.title.grid(row=0, column=1)
        self.logo_image_label.grid(row=1, column=0)
        self.author.grid(row=1, column=1)
        self.button_to_roadmap.grid(row=1, column=2, padx=40, sticky=tk.E)

'''
Roadmap

This frame consists of:
- roadmap outline of the modules (as images)
- buttons leading to each page of the tutorial

The purpose of this frame is to serve as the roadmap (or overview) of this tutorial.
'''
class roadmap_frame(frame_base.frame_base):
    def create_widgets(self):
        
        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)
        self.columnconfigure(3, weight=2)
        self.columnconfigure(4, weight=2)
        self.columnconfigure(5, weight=2)
        self.columnconfigure(6, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=3)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=3)

        # add specifications
        pathway_image_scale = 1
        self.intro_image_path = 'media/module_prelude/roadmap/intro.png'
        self.intro_image = ImageTk.PhotoImage(im.scale_image(Image.open(self.intro_image_path), pathway_image_scale))
        self.play_image_path = 'media/module_prelude/roadmap/play.png'
        self.play_image = ImageTk.PhotoImage(im.scale_image(Image.open(self.play_image_path), pathway_image_scale))
        self.q_image_path = 'media/module_prelude/roadmap/q.png'
        self.q_image = ImageTk.PhotoImage(im.scale_image(Image.open(self.q_image_path), pathway_image_scale))
        self.dqn_image_path = 'media/module_prelude/roadmap/dqn.png'
        self.dqn_image = ImageTk.PhotoImage(im.scale_image(Image.open(self.dqn_image_path), pathway_image_scale))
        self.challenge_image_path = 'media/module_prelude/roadmap/challenge.png'
        self.challenge_image = ImageTk.PhotoImage(im.scale_image(Image.open(self.challenge_image_path), pathway_image_scale))

        button_wraplength = 200
        button_width_text = 24
        button_height_text = 2
        button_font_size = 12

        # add widgets
        self.title = tk.Label(self, text="Roadmap", font=("Courier", 48))

        self.intro_image_label = tk.Label(self, image=self.intro_image)
        self.play_image_label = tk.Label(self, image=self.play_image)
        self.q_image_label = tk.Label(self, image=self.q_image)
        self.dqn_image_label = tk.Label(self, image=self.dqn_image)
        self.challenge_image_label = tk.Label(self, image=self.challenge_image)

        self.intro_tutorial_overview_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(intro.tutorial_overview_frame),
                                    text="Tutorial Overview", borderwidth=1, font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.intro_artificial_intelligence_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(intro.artificial_intelligence_frame),
                                    text="Artificial Intelligence", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.intro_ai_in_the_21st_century_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(intro.ai_in_the_21st_century_frame),
                                    text="AI In The 21st Century", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.intro_briefly_on_q_learning_and_deep_q_network_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(intro.briefly_on_q_learning_and_deep_q_network_frame),
                                    text="Briefly On Q-Learning & Deep Q-Network", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.play_pong_gameplay_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(play.pong_gameplay_frame),
                                    text="Pong Gameplay", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.play_reflection_on_pong_gameplay_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(play.reflection_on_pong_gameplay_frame),
                                    text="Reflection On Pong Gameplay", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.play_terminology_definition_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(play.terminology_definition_frame),
                                    text="Terminology: Definition", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.play_terminology_pong_mix_and_match_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(play.terminology_pong_mix_and_match_frame),
                                    text="Terminology: Pong Mix & Match", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.play_strategy_from_pong_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(play.strategy_from_pong_frame),
                                    text="Strategy From Pong", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.q_action_value_function_reward_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(q.action_value_function_reward_frame),
                                    text="Action-Value Function: Reward", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.q_action_value_function_max_q_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(q.action_value_function_max_q_frame),
                                    text="Action-Value Function: Max Q", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.q_q_learning_algorithm_initialization_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(q.q_learning_algorithm_initialization_frame),
                                    text="Q-Learning Algorithm: Initialization", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.q_q_learning_algorithm_training_sequence_frame_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(q.q_learning_algorithm_training_sequence_frame), self.controller.frames[q.q_learning_algorithm_training_sequence_frame].video_animation.open_video()],
                                    text="Q-Learning Algorithm: Training Sequence", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.q_q_learning_algorithm_exploration_v_exploitation_frame_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(q.q_learning_algorithm_exploration_v_exploitation_frame), self.controller.frames[q.q_learning_algorithm_exploration_v_exploitation_frame].video_animation.open_video()],
                                    text="Q-Learning Algorithm: Exploration v. Exploitation", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.q_action_value_function_revisited_discount_factor_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(q.action_value_function_revisited_discount_factor_frame),
                                    text="Action-Value Function Revisited: Discount Factor", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.dqn_the_large_problem_with_pixel_input_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(dqn.the_large_problem_with_pixel_input_frame),
                                    text="The Large Problem With Pixel Input", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.dqn_q_network_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(dqn.q_network_frame),
                                    text="Q-Network", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.dqn_q_network_training_sequence_frame_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(dqn.q_network_training_sequence_frame), self.controller.frames[dqn.q_network_training_sequence_frame].video_animation.open_video()],
                                    text="Q-Network: Training Sequence", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.dqn_replay_memory_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(dqn.replay_memory_frame),
                                    text="Replay Memory", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.challenge_challenge_dqn_player_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(challenge.challenge_dqn_player_frame),
                                    text="Challenge: DQN Player!", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)
        self.challenge_reflection_on_evolution_of_dqn_player_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(challenge.reflection_on_evolution_of_dqn_player_frame),
                                    text="Reflection On Evolution Of DQN Player", font=("Courier", button_font_size), width=button_width_text, height=button_height_text, wraplength=button_wraplength)


        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(title_frame),
                                    text="Previous", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(intro.tutorial_overview_frame),
                                    text="Next", font=("Courier", 14))

        
        # lay widgets
        self.title.grid(row=0, 
        				column=0,
        				columnspan=7)
        self.intro_image_label.grid(row=1,
                          column=1,
                          sticky=tk.NW+tk.SE)
        self.play_image_label.grid(row=1,
                          column=2,
                          sticky=tk.NW+tk.SE)
        self.q_image_label.grid(row=1,
                          column=3,
                          sticky=tk.NW+tk.SE)
        self.dqn_image_label.grid(row=1,
                          column=4,
                          sticky=tk.NW+tk.SE)
        self.challenge_image_label.grid(row=1,
                          column=5,
                          sticky=tk.NW+tk.SE)
        self.intro_tutorial_overview_frame_button.grid(row=2, 
                             column=1, 
                             sticky=tk.NW+tk.SE)
        self.intro_artificial_intelligence_frame_button.grid(row=3, 
                             column=1, 
                             sticky=tk.NW+tk.SE)
        self.intro_ai_in_the_21st_century_frame_button.grid(row=4, 
                             column=1, 
                             sticky=tk.NW+tk.SE)
        self.intro_briefly_on_q_learning_and_deep_q_network_frame_button.grid(row=5, 
                             column=1, 
                             sticky=tk.NW+tk.SE)
        self.play_pong_gameplay_frame_button.grid(row=2, 
                             column=2, 
                             sticky=tk.NW+tk.SE)
        self.play_reflection_on_pong_gameplay_frame_button.grid(row=3, 
                             column=2, 
                             sticky=tk.NW+tk.SE)
        self.play_terminology_definition_frame_button.grid(row=4, 
                             column=2, 
                             sticky=tk.NW+tk.SE)
        self.play_terminology_pong_mix_and_match_frame_button.grid(row=5, 
                             column=2, 
                             sticky=tk.NW+tk.SE)
        self.play_strategy_from_pong_frame_button.grid(row=6, 
                             column=2, 
                             sticky=tk.NW+tk.SE)
        self.q_action_value_function_reward_frame_button.grid(row=2, 
                             column=3, 
                             sticky=tk.NW+tk.SE)
        self.q_action_value_function_max_q_frame_button.grid(row=3, 
                             column=3, 
                             sticky=tk.NW+tk.SE)
        self.q_q_learning_algorithm_initialization_frame_button.grid(row=4, 
                             column=3, 
                             sticky=tk.NW+tk.SE)
        self.q_q_learning_algorithm_training_sequence_frame_button.grid(row=5, 
                             column=3, 
                             sticky=tk.NW+tk.SE)
        self.q_q_learning_algorithm_exploration_v_exploitation_frame_button.grid(row=6, 
                             column=3, 
                             sticky=tk.NW+tk.SE)
        self.q_action_value_function_revisited_discount_factor_frame_button.grid(row=7, 
                             column=3, 
                             sticky=tk.NW+tk.SE)
        self.dqn_the_large_problem_with_pixel_input_frame_button.grid(row=2, 
                             column=4, 
                             sticky=tk.NW+tk.SE)
        self.dqn_q_network_frame_button.grid(row=3, 
                             column=4, 
                             sticky=tk.NW+tk.SE)
        self.dqn_q_network_training_sequence_frame_button.grid(row=4, 
                             column=4, 
                             sticky=tk.NW+tk.SE)
        self.dqn_replay_memory_frame_button.grid(row=5,
                             column=4,
                             sticky=tk.NW+tk.SE)
        self.challenge_challenge_dqn_player_frame_button.grid(row=2,
                             column=5,
                             sticky=tk.NW+tk.SE)
        self.challenge_reflection_on_evolution_of_dqn_player_frame_button.grid(row=3,
                             column=5,
                             sticky=tk.NW+tk.SE)


        self.previous_frame_button.grid(row=8, 
                             column=0, 
                             padx=40, 
                             sticky=tk.W)
        self.next_frame_button.grid(row=8, 
                             column=6, 
                             padx=40, 
                             sticky=tk.E)

