'''
Title: Reinforcement Learning and Deep Q-Network 101
File: module_play.py
Description: This is the play module
Company: Artificial Intelligence Research Institute (AIRI)
Author: Channy Hong

'''
import Tkinter as tk
import pong_game_control as pgc

import event_handler as eh
import mix_and_match as mam

import module_frame_base as frame_base
import module_prelude as prelude

import module_intro as intro
import module_q as q



'''
Pong Gameplay

This frame consists of:
- various instructions for 'Pong' gameplay
- 'Pong' gameplay environment with score and start button

The purpose of this frame is to have the user experience the 'Pong' gameplay.
'''
class pong_gameplay_frame(frame_base.frame_base):

    # gameplay function
    def pong_gameplay(self):
        self.pygame_event.in_play = True
        self.player_two_score.set("Score: 0")
        self.scoreboard.update()
        pgc.pong_game_control(1, 0, 1, "Play 'Pong'!", self.pygame_event, False)

    # update score function
    def update_score(self, _, player_two_score):
        self.player_two_score.set("Score: " + str(player_two_score))
        self.scoreboard.update()

    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=3)
        self.columnconfigure(3, weight=3)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)

        self.pygame_event = eh.pygame_event(self)
        self.player_two_score = tk.StringVar()

        # add widgets
        self.title = tk.Label(self, text="Pong Gameplay", font=("Courier", 48))
        self.text1 = tk.Label(self, text="'Pong' is a game developed by Atari in 1972, and is widely considered to be one of the earliest arcade video games.", font=("Courier", 16), wraplength=800)
        self.text2 = tk.Label(self, text="Okay, now it's time to play some 'Pong'! To play, the only things you have to know are the following 3 things:", font=("Courier", 16), wraplength=800)
        self.text_num1 = tk.Label(self, text="1. ", font=("Courier", 16))
        self.text_num2 = tk.Label(self, text="2. ", font=("Courier", 16))
        self.text_num3 = tk.Label(self, text="3. ", font=("Courier", 16))
        self.play_pong_button = tk.Button(self,
                                    command=lambda: self.pong_gameplay(),
                                    text="Play 'Pong'!", font=("Courier", 16))
        self.scoreboard = tk.Label(self, textvariable=self.player_two_score, font=("Courier", 16))
        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(intro.briefly_on_q_learning_and_deep_q_network_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(reflection_on_pong_gameplay_frame),
                                    text="Next", font=("Courier", 14))
        
        # add + lay toggle widgets (args: self, master, text_string, width=1, height=1, wraplength=None, justify=LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        self.text3 = eh.toggle_label(self, "You have three choices of action:\n   a. Press [Up Arrow]\n   b. Press [Down Arrow]\n   c. Don't press anything", 
            wraplength=550, row=3, column=2)
        self.text4 = eh.toggle_label(self, "You will see your score on this screen below", 
            wraplength=550, row=4, column=2)
        self.text5 = eh.toggle_label(self, "Your goal is to maximize your score", 
            wraplength=550, row=5, column=2)

        # lay widgets
        self.title.grid(row=0, column=0, columnspan=4)
        self.text1.grid(row=1, column=1, columnspan=2, sticky=tk.NW+tk.SE)
        self.text2.grid(row=2, column=1, columnspan=2, sticky=tk.NW+tk.SE)
        self.text_num1.grid(row=3, column=1, sticky=tk.NW+tk.SE)
        self.text_num2.grid(row=4, column=1, sticky=tk.NW+tk.SE)
        self.text_num3.grid(row=5, column=1, sticky=tk.NW+tk.SE)
        self.play_pong_button.grid(row=6, column=1, columnspan=1)
        self.scoreboard.grid(row=6, column=2, sticky=tk.NW+tk.SE)
        self.previous_frame_button.grid(row=7, column=0, padx=40, sticky=tk.W)
        self.to_roadmap_button.grid(row=7, column=1, columnspan=2)
        self.next_frame_button.grid(row=7, column=3, padx=40, sticky=tk.E)

'''
Reflection On Pong Gameplay

This frame consists of:
- a list of questions
- corresponding answer fields
- corresponding correct answer toggle texts

The purpose of this frame is to have the user take an analytic mindset on the game of 'Pong'.
'''
class reflection_on_pong_gameplay_frame(frame_base.frame_base):
    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=10)
        self.columnconfigure(3, weight=5)
        self.columnconfigure(4, weight=1)
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
        
        # add widgets
        self.title = tk.Label(self, text="Reflection On Pong Gameplay", font=("Courier", 48))
        self.text1 = tk.Label(self, text="Now, let's do some reflection! This reflection is meant to guide you through the thought processes that occurred inside your head while you played 'Pong'!", font=("Courier", 16), wraplength=1000, justify=tk.LEFT)
        
        self.t11 = tk.Label(self, text="Question", 
            wraplength=300, font=("Courier", 14))
        self.t12 = tk.Label(self, text="Your Response", 
            wraplength=300, font=("Courier", 14))
        self.t13 = tk.Label(self, text="Answer (click to reveal/hide)", 
            wraplength=300, font=("Courier", 14))

        self.t21 = tk.Label(self, text="As stated in the instruction before the game, what was your goal?", 
            wraplength=250, justify=tk.LEFT, font=("Courier", 12))
        self.t31 = tk.Label(self, text="To achieve your goal, what did you try to do in the game?", 
            wraplength=250, justify=tk.LEFT, font=("Courier", 12))
        self.t41 = tk.Label(self, text="When you succeeded in doing what you were trying to do, how much were you rewarded by the game (or penalized for undesirable outcomes)?", 
            wraplength=250, justify=tk.LEFT, font=("Courier", 12))
        self.t51 = tk.Label(self, text="As stated in the instruction before the game, what type of actions could you take at each tick of time?", 
            wraplength=250, justify=tk.LEFT, font=("Courier", 12))
        self.t61 = tk.Label(self, text="To decide which action to take at each time tick, what information from the game did you rely on?", 
            wraplength=250, justify=tk.LEFT, font=("Courier", 12))
        self.t71 = tk.Label(self, text="With the information from the game, what factors did you take into account when deciding which action to take?", 
            wraplength=250, justify=tk.LEFT, font=("Courier", 12))
        
        self.t22 = tk.Text(self, width=1, height=1)
        self.t32 = tk.Text(self, width=1, height=1)
        self.t42 = tk.Text(self, width=1, height=1)
        self.t52 = tk.Text(self, width=1, height=1)
        self.t62 = tk.Text(self, width=1, height=1)
        self.t72 = tk.Text(self, width=1, height=1)

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(pong_gameplay_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(terminology_definition_frame),
                                    text="Next", font=("Courier", 14))
        
        # add + lay toggle widgets (args: self, master, text_string, width=1, height=1, wraplength=None, justify=tk.LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        self.t23 = eh.toggle_label(self, "Maximize my score (disregarding my opponent's score)", 
            row=3, column=3, wraplength=280, font_size=12)
        self.t33 = eh.toggle_label(self, "Deflect the ball with my paddle and try to get the ball past my opponent's paddle", 
            row=4, column=3, wraplength=280, font_size=12)
        self.t43 = eh.toggle_label(self, "10 points for deflecting the ball with my paddle, 100 points for getting the ball past my opponent's paddle, and -100 for letting the ball past my paddle", 
            row=5, column=3, wraplength=280, font_size=12)
        self.t53 = eh.toggle_label(self, "1. Move my paddle up\n2. Move my paddle down\n3. Keep my paddle still", 
            row=6, column=3, wraplength=280, font_size=12)
        self.t63 = eh.toggle_label(self, "Pixel information from the screen", 
            row=7, column=3, wraplength=280, font_size=12)
        self.t73 = eh.toggle_label(self, "- Where the ball is going to end up when it gets to my paddle, based on current trajectory\n- Where my paddle is currently at", 
            row=8, column=3, wraplength=280, font_size=12)

        # lay widgets
        self.title.grid(row=0, 
                        column=0, 
                        columnspan=5)
        self.text1.grid(row=1, column=0, columnspan=5)

        self.t11.grid(row=2, column=1)
        self.t12.grid(row=2, column=2)
        self.t13.grid(row=2, column=3)

        self.t21.grid(row=3, column=1, sticky=tk.W)
        self.t31.grid(row=4, column=1, sticky=tk.W)
        self.t41.grid(row=5, column=1, sticky=tk.W)
        self.t51.grid(row=6, column=1, sticky=tk.W)
        self.t61.grid(row=7, column=1, sticky=tk.W)
        self.t71.grid(row=8, column=1, sticky=tk.W)

        self.t22.grid(row=3, column=2, sticky=tk.NW+tk.SE)
        self.t32.grid(row=4, column=2, sticky=tk.NW+tk.SE)
        self.t42.grid(row=5, column=2, sticky=tk.NW+tk.SE)
        self.t52.grid(row=6, column=2, sticky=tk.NW+tk.SE)
        self.t62.grid(row=7, column=2, sticky=tk.NW+tk.SE)
        self.t72.grid(row=8, column=2, sticky=tk.NW+tk.SE)

        self.previous_frame_button.grid(row=9, 
                                        column=0, 
                                        padx=40, 
                                        sticky=tk.W)
        self.to_roadmap_button.grid(row=9, 
                                    column=0,
                                    columnspan=5)
        self.next_frame_button.grid(row=9, 
                                    column=4, 
                                    padx=40, 
                                    sticky=tk.E)


'''
Terminology Definition

This frame consists of:
- toggle texts explaining the 4 Markov Decision Process concepts

The purpose of this frame is to introduce various Markov Decision Process concepts.
'''
class terminology_definition_frame(frame_base.frame_base):
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
        
        # add widgets
        self.title = tk.Label(self, text="Terminology: Definition", font=("Courier", 48))

        self.text1 = tk.Label(self, font=("Courier", 16), justify=tk.LEFT, wraplength=900, text="Okay, now it's time to delve into the idea of 'Q-Learning'.\n\nAgain, 'Q-Learning' is a type of an algorithm - or a clearly defined instruction that tells our player what to do at each and every situation.\n\nTo derive any algorithm, however, our player will need to come up with a set of vocabulary to clearly describe the most basic framework of any game. Such fundamental units of any gameplay can be boiled down to the following concepts:")
        self.text2 = tk.Label(self, text="Now, we have the basic vocabulary with which we can describe any game setting!", font=("Courier", 16), justify=tk.LEFT)
        self.text3 = tk.Label(self, text="Note: the above concepts represent the core of what is called the Markov Decision Process.", font=("Courier", 12), justify=tk.LEFT)

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(reflection_on_pong_gameplay_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(terminology_pong_mix_and_match_frame),
                                    text="Next", font=("Courier", 14))
        


        # add + lay toggle widgets (args: self, master, text_string, width=1, height=1, wraplength=None, justify=tk.LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        self.state_text = eh.toggle_label(self, "State: a certain 'state' of the game that the player can find itself in\ni.e. a configuration of a chess board resulting from a series of legal actions", 
            row=2, column=1, wraplength=900)
        self.reward_text = eh.toggle_label(self, "Reward: a numerical 'reward' (or penalty) awarded to the player at each state\ni.e. in association football, the reward when the ball goes in the opponent's net is 1, while the reward when the ball stays on the field is 0", 
            row=3, column=1, wraplength=900)
        self.action_text = eh.toggle_label(self, "Action: an 'action' that the player can take\ni.e. the act of moving the player's pawn forward by one square", 
            row=4, column=1, wraplength=900)
        self.utility_text = eh.toggle_label(self, "Utility Function: a function that describes the 'utility' or the goal of the player\ni.e. the player's goal on a quiz TV show is to receive as large a cash prize as possible", 
            row=5, column=1, wraplength=900)



        # lay widgets
        self.title.grid(row=0, 
                        column=1, 
                        columnspan=1)

        self.text1.grid(row=1, column=1, sticky=tk.W)
        self.text2.grid(row=6, column=1, sticky=tk.W)
        self.text3.grid(row=7, column=1, sticky=tk.W)

        self.previous_frame_button.grid(row=8, 
                                        column=0, 
                                        padx=40, 
                                        sticky=tk.W)
        self.to_roadmap_button.grid(row=8, 
                                    column=1, 
                                    columnspan=1)
        self.next_frame_button.grid(row=8, 
                                    column=2, 
                                    padx=40, 
                                    sticky=tk.E)






'''
Terminology Mix & Match

This frame consists of:
- a mix and match module between MDP definitions and answers from 'Pong' gameplay

The purpose of this frame is to have the user connect the MDP definitions with the various 
aspects of 'Pong' gameplay.
'''
class terminology_pong_mix_and_match_frame(frame_base.frame_base):
    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
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
        
        # add + lay mix and match canvas widget (args: self, master, grid_top, grid_bottom, grid_left, grid_right)
        self.mix_and_match = mam.mix_and_match(self, 2, 7, 2, 2)

        # add widgets
        self.title = tk.Label(self, text="Terminology: Pong Mix & Match", font=("Courier", 48))

        self.intro_text = tk.Label(self, wraplength=1100, pady=10, font=("Courier", 14), justify=tk.LEFT, text="Take a note that at the 'Reflection On Pong Gameplay' page, you broke down the various characteristics of your own 'Pong' gameplay. On the previous slide, you learned about the fundamental units of a any gameplay. Now, it's time to map the correspondence between the two by doing some mix & match!")

        self.t1 = tk.Label(self, wraplength=200, font=("Courier", 14), justify=tk.LEFT, text="State: a certain 'state' of the game that the player can find itself in")
        self.t2 = tk.Label(self, wraplength=200, font=("Courier", 14), justify=tk.LEFT, text="Reward: a numerical 'reward' (or penalty) awarded to the player at each state")
        self.t3 = tk.Label(self, wraplength=200, font=("Courier", 14), justify=tk.LEFT, text="Action: an 'action' that the player can take")
        self.t4 = tk.Label(self, wraplength=200, font=("Courier", 14), justify=tk.LEFT, text="Utility Function: a function that describes the 'utility' or the goal of the player")
        self.t5 = tk.Label(self, wraplength=200, font=("Courier", 14), justify=tk.LEFT, text="Maximize my score (disregarding my opponent's score)")
        self.t6 = tk.Label(self, wraplength=200, font=("Courier", 14), justify=tk.LEFT, text="Deflect the ball with my paddle and try to get the ball past my opponent's paddle")
        self.t7 = tk.Label(self, wraplength=200, font=("Courier", 14), justify=tk.LEFT, text="10 points for deflecting the ball with my paddle, 100 points for getting the ball past my opponent's paddle, and -100 for letting the ball past my paddle")
        self.t8 = tk.Label(self, wraplength=200, font=("Courier", 14), justify=tk.LEFT, text="1. Move my paddle up\n2. Move my paddle down\n3. Keep my paddle still")
        self.t9 = tk.Label(self, wraplength=200, font=("Courier", 14), justify=tk.LEFT, text="Pixel information from the screen")
        self.t10 = tk.Label(self, wraplength=200, font=("Courier", 14), justify=tk.LEFT, text="- Where the ball is going to end up when it gets to my paddle, based on current trajectory\n- Where my paddle is currently at")

        self.check_answer_button = tk.Button(self, command=lambda: self.mix_and_match.check_answer(), text="Check Answer", font=("Courier", 14), pady=10)
        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(terminology_definition_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(strategy_from_pong_frame),
                                    text="Next", font=("Courier", 14))
        

        # lay widgets
        self.title.grid(row=0, column=0, columnspan=6)

        self.intro_text.grid(row=1, column=0, columnspan=6)

        self.t1.grid(row=2, column=1, rowspan=2, sticky=tk.W)
        self.t2.grid(row=4, column=1, sticky=tk.W)
        self.t3.grid(row=5, column=1, rowspan=2, sticky=tk.W)
        self.t4.grid(row=7, column=1, sticky=tk.W)
        self.t5.grid(row=2, column=3, sticky=tk.W)
        self.t6.grid(row=3, column=3, sticky=tk.W)
        self.t7.grid(row=4, column=3, sticky=tk.W)
        self.t8.grid(row=5, column=3, sticky=tk.W)
        self.t9.grid(row=6, column=3, sticky=tk.W)
        self.t10.grid(row=7, column=3, sticky=tk.W)

        self.check_answer_button.grid(row=8, column=0, columnspan=6)
        
        self.previous_frame_button.grid(row=9, column=0, padx=40, sticky=tk.W)
        self.to_roadmap_button.grid(row=9, column=0, columnspan=6)
        self.next_frame_button.grid(row=9, column=5, padx=40, sticky=tk.E)






'''
Strategy From Pong

This frame consists of:
- explanation for what the remaining two answers from reflections of 'Pong' gameplay amount to

The purpose of this frame is to introduce the idea of where human intuition of how to play the
games comes in.
'''
class strategy_from_pong_frame(frame_base.frame_base):
    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=5)
        self.rowconfigure(5, weight=1)
        
        # add widgets
        self.title = tk.Label(self, text="Strategy From Pong", font=("Courier", 48))

        self.text1 = tk.Label(self, wraplength=800, font=("Courier", 16), text="So, it turns out that these two characteristics of your 'Pong' gameplay are beyond the basic framework of 'Pong'. So then, what are they?")
        self.text21 = tk.Label(self, wraplength=400, font=("Courier", 12), text="To achieve your goal, what did you try to do in the game?")
        self.text22 = tk.Label(self, wraplength=400, font=("Courier", 12), text="Deflect the ball with my paddle and try to get the ball past my opponent's paddle")
        self.text31 = tk.Label(self, wraplength=400, font=("Courier", 12), text="With the information from the game, what factors did you take into account when deciding which action to take?")
        self.text32 = tk.Label(self, wraplength=400, font=("Courier", 12), text="- Where the ball is going to end up when it gets to my paddle, based on current trajectory\n- Where my paddle is currently at")

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(terminology_pong_mix_and_match_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(q.action_value_function_reward_frame),
                                    text="Next", font=("Courier", 14))
        
        # add + lay toggle widgets (args: self, master, text_string, width=1, height=1, wraplength=None, justify=tk.LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        self.explanation = eh.toggle_label(self, "Well actually, they are something that your brain automatically came up with as it figured out - or learned - the best way to play 'Pong'. This is otherwise known as strategy!\n\nAnd this strategy is exactly what we are going to use to come up with our own algorithm, and specifically the Q-Learning algorithm!\n\nNote: remember that we are using the specific example of 'Pong' gameplay to come up with a general strategy that works for any game!", 
            row=4, column=1, columnspan=2, wraplength=800)

        # lay widgets
        self.title.grid(row=0, 
                        column=0, 
                        columnspan=4)

        self.text1.grid(row=1, column=1, columnspan=2)
        self.text21.grid(row=2, column=1)
        self.text22.grid(row=2, column=2)
        self.text31.grid(row=3, column=1)
        self.text32.grid(row=3, column=2)

        self.previous_frame_button.grid(row=5, 
                                        column=0, 
                                        padx=40, 
                                        sticky=tk.W)
        self.to_roadmap_button.grid(row=5, 
                                    column=1, 
                                    columnspan=2)
        self.next_frame_button.grid(row=5, 
                                    column=3, 
                                    padx=40, 
                                    sticky=tk.E)