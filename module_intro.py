'''
Title: Reinforcement Learning and Deep Q-Network 101
File: module_intro.py
Description: This is the introduction module
Company: Artificial Intelligence Research Institute (AIRI)
Author: Channy Hong

'''
import Tkinter as tk
import pong_game_control as pgc

import event_handler as eh

import module_frame_base as frame_base
import module_prelude as prelude

import module_play as play


'''
Tutorial Overview

This frame consists of:
- various toggle texts outlining the tutorial overview

The purpose of this frame is to allow the reader to gauge what this tutorial will consist of.
'''
class tutorial_overview_frame(frame_base.frame_base):
    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=6)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        self.rowconfigure(9, weight=1)
        self.rowconfigure(10, weight=1)
        self.rowconfigure(11, weight=1)
        
        # add widgets
        self.title = tk.Label(self, text="Tutorial Overview", font=("Courier", 48))
        self.text1 = tk.Label(self, text="Total duration", font=("Courier", 16))
        self.text3 = tk.Label(self, text="What do I need to know before this tutorial?", font=("Courier", 16))
        self.text5 = tk.Label(self, text="What will I leave with at the end of this tutorial?", font=("Courier", 16))
        self.text7 = tk.Label(self, text="How is this tutorial designed?", font=("Courier", 16))
        self.text9 = tk.Label(self, text="How do I navigate this tutorial?", font=("Courier", 16))

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(artificial_intelligence_frame),
                                    text="Next", font=("Courier", 14))

        
        # add + lay toggle widgets (args: self, master, text_string, width=1, height=1, wraplength=None, justify=LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        self.text2 = eh.toggle_label(self, "- Around 60 minutes", 
            wraplength=900, row=2, column=1)
        self.text4 = eh.toggle_label(self, "- A basic understanding of what an algorithm is", 
            wraplength=900, row=4, column=1)
        self.text6 = eh.toggle_label(self, "- An in-depth knowledge of how the basic 'Q-Learning' algorithm works\n- An in-depth knowledge of how the basic 'Deep Q-Learning' (DQN) algorithm works\n- An experiential understanding of how a DQN learner develops over time", 
            wraplength=900, row=6, column=1)
        self.text8 = eh.toggle_label(self, "This tutorial is designed to build layer upon layer of concepts. By integrating real-time gameplay and examples from the classic arcade video game 'Pong', this tutorial will incorporate as much experiential and graphic learning as possible to cover all the mathematical and algorithmic concepts.", 
            width=1, height=2, wraplength=900, row=8, column=1)
        self.text10 = eh.toggle_label(self, "You can move freely back and forth between pages by clicking on the buttons below. Any progress you make in a page will be left saved even if you leave that page.", 
            wraplength=900, row=10, column=1)

        # lay widgets
        self.title.grid(row=0, column=1, rowspan=1, columnspan=1, sticky=tk.NW+tk.SE)
        self.text1.grid(row=1, column=1, rowspan=1, columnspan=1, sticky=tk.NW+tk.SE)
        self.text3.grid(row=3, column=1, rowspan=1, columnspan=1, sticky=tk.NW+tk.SE)
        self.text5.grid(row=5, column=1, rowspan=1, columnspan=1, sticky=tk.NW+tk.SE)
        self.text7.grid(row=7, column=1, rowspan=1, columnspan=1, sticky=tk.NW+tk.SE)
        self.text9.grid(row=9, column=1, rowspan=1, columnspan=1, sticky=tk.NW+tk.SE)
        self.previous_frame_button.grid(row=11, column=0, sticky=tk.W)
        self.to_roadmap_button.grid(row=11, column=1)
        self.next_frame_button.grid(row=11, column=2, sticky=tk.E)





'''
Artificial Intelligence

This frame consists of:
- introductory information on AI including definitions and implications

The purpose of this frame is to introduce the idea of AI.
'''
class artificial_intelligence_frame(frame_base.frame_base):
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
        self.title = tk.Label(self, text="Artificial Intelligence", font=("Courier", 48))

        self.text1 = tk.Label(self, font=("Courier", 16), justify=tk.LEFT, wraplength=1000, text="So what we are about to learn today falls under a broad category that is called 'artificial intelligence'. We hear about this term all the time, artificial intelligence. But what does it mean to begin with?")

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(tutorial_overview_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(ai_in_the_21st_century_frame),
                                    text="Next", font=("Courier", 14))
        

        # add + lay toggle widgets (args: self, master, text_string, width=1, height=1, wraplength=None, justify=tk.LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        self.text2 = eh.toggle_label(self, "Well, according to the Merriam Webster dictionary,  artificial intelligence is:\n1. a branch of computer science dealing with the simulation of intelligent behavior in computers.\n2. the capability of a machine to imitate intelligent human behavior.", 
            row=2, column=1, wraplength=1000)
        self.text3 = eh.toggle_label(self, "In other words, artificial intelligence is a technique with which we equip our computer to behave like humans. As a tool that we humans have developed to help us solve our problems, artificial intelligence distinguishes itself from other types of tools in that we are creating a machine that supplements the function of the human brain and not something that merely supplements the function of a leg or an arm.", 
            row=3, column=1, wraplength=1000)
        self.text4 = eh.toggle_label(self, "This type of cognitive function requires two things: to perceive the environment and to make appropriate decisions.", 
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















'''
AI In The 21st Century

This frame consists of:
- information on the latest advances of AI

The purpose of this frame is to inform the readers on the latest of AI.
'''
class ai_in_the_21st_century_frame(frame_base.frame_base):
    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=16)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        
        # add widgets
        self.title = tk.Label(self, text="AI In The 21st Century", font=("Courier", 48))
        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(artificial_intelligence_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(briefly_on_q_learning_and_deep_q_network_frame),
                                    text="Next", font=("Courier", 14))
        
        # add + lay toggle widgets (args: self, master, text_string, width=1, height=1, wraplength=None, justify=tk.LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        self.text1 = eh.toggle_label(self, "Today, we can see applications of AI in branches such as:\n- natural language processing\n- speech recognition\n- face recognition\n- computer vision\n- strategic planning and computer game bot\nFor this tutorial, we are going to focus on 'strategic planning and computer game bot'.", 
            row=1, column=1, wraplength=900)
        self.text2 = eh.toggle_label(self, "In 2016, game artificial intelligence was under heavy highlight for the highly-anticipated match between 18-times Go champion Lee Sedol and an AI agent named AlphaGo, developed by Google's Deepmind team. This match astonished the world as AlphaGo succeeded in winning the series 4-1.", 
            row=2, column=1, wraplength=900)
        self.text3 = eh.toggle_label(self, "This was a major milestone in AI research as Go has been traditionally considered to be too hard a problem for a machine learning algorithm. AlphaGo's machine learning algorithm employs a technique called reinforcement, a specific type of which we will cover in this tutorial.", 
            row=3, column=1, wraplength=900)

        # lay widgets
        self.title.grid(row=0, 
                        column=0, 
                        columnspan=8)
        self.previous_frame_button.grid(row=4, 
                                        column=0, 
                                        padx=10, 
                                        sticky=tk.W)
        self.to_roadmap_button.grid(row=4, 
                                    column=1, 
                                    columnspan=1)
        self.next_frame_button.grid(row=4, 
                                    column=2, 
                                    padx=10, 
                                    sticky=tk.E)










'''
Briefly On Q-Learning & Deep Q-Network

This frame consists of:
- basic information on Q-Learning
- basic information on Deep Q-Network

The purpose of this frame is to introduce the idea of Q-Learning and Deep Q-Network.
'''
class briefly_on_q_learning_and_deep_q_network_frame(frame_base.frame_base):
    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=12)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        
        # add widgets
        self.title = tk.Label(self, text="Briefly On Q-Learning & Deep Q-Network", font=("Courier", 48))
        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(ai_in_the_21st_century_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(play.pong_gameplay_frame),
                                    text="Next", font=("Courier", 14))
        

        # add + lay toggle widgets (args: self, master, text_string, width=1, height=1, wraplength=None, justify=tk.LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        self.text1 = eh.toggle_label(self, "Q-Learning is a reinforcement learning technique that can be used to find the best policy for taking actions. The idea was first introduced by Christopher Watkins in 1989 and the convergence of its optimal policy search was proved by Watkins and Peter Dayans in 1992.", 
            row=1, column=1, wraplength=900)
        self.text2 = eh.toggle_label(self, "Deep Q-Network is an algorithm that combines the branches of Q-Learning with neural network. This was done to combat the relatively small workspace Q-Learning algorithm can work with. With recent advances in neural network techniques, Google's Deepmind team was able to create an algorithm that performed as well as or better than humans in numerous Atari 2006 games, with breakthrough publications in 2013 and in 2015.", 
            row=2, column=1, wraplength=900)



        # lay widgets
        self.title.grid(row=0, 
                        column=0, 
                        columnspan=8)
        self.previous_frame_button.grid(row=3, 
                                        column=0, 
                                        padx=10, 
                                        sticky=tk.W)
        self.to_roadmap_button.grid(row=3, 
                                    column=1, 
                                    columnspan=1)
        self.next_frame_button.grid(row=3, 
                                    column=2, 
                                    padx=10, 
                                    sticky=tk.E)

