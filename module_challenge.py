'''
Title: Reinforcement Learning and Deep Q-Network 101
File: module_challenge.py
Description: This is the challenge module
Company: Artificial Intelligence Research Institute (AIRI)
Author: Channy Hong

'''
import Tkinter as tk
import pong_game_control as pgc

import module_frame_base as frame_base
import module_prelude as prelude

import module_dqn as dqn
import event_handler as eh







'''
Challenge: DQN Player!

This frame consists of:
- explanation of how the challenge works
- buttons that start up a 'Pong' gameplay against several differently trained DQN players

The purpose of this frame is to have the user experience in gameplay how the DQN training
evolves over time.
'''
class challenge_dqn_player_frame(frame_base.frame_base):
    
    def challenge_gameplay(self, trained_steps):
        # initialize scoreboard
        self.player_one_score.set("DQN Agent Score: 0")
        self.player_two_score.set("Your Score: 0")

        trained_steps_numerical = None
        if trained_steps == "one_million":
            trained_steps_numerical = 1000000
        if trained_steps == "two_million":
            trained_steps_numerical = 2000000
        if trained_steps == "five_million":
            trained_steps_numerical = 5000000
        if trained_steps == "ten_million":
            trained_steps_numerical = 10000000
        if trained_steps == "fourteen_million":
            trained_steps_numerical = 14000000
        self.current_level.set("   Level One: " + str(trained_steps_numerical) + " steps   ")

        self.player_one_score_label.update()
        self.player_two_score_label.update()
        self.current_level_label.update()

        self.pygame_event.in_play = True
        pgc.pong_game_control(2, 0, 1, "Challenge: DQN Player!", self.pygame_event, True, trained_steps)

    def update_challenge_score(self, player_one_score, player_two_score):
        self.player_one_score.set("DQN Agent Score: " + str(player_one_score) + "   ")
        self.player_two_score.set("   Your Score: " + str(player_two_score))
        self.player_one_score_label.update()
        self.player_two_score_label.update()


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
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        self.rowconfigure(9, weight=1)
        self.rowconfigure(10, weight=1)
        self.rowconfigure(11, weight=1)

        self.pygame_event = eh.pygame_event(self)

        self.player_one_score = tk.StringVar()
        self.player_two_score = tk.StringVar()
        self.current_level = tk.StringVar()
        
        # add widgets
        self.title = tk.Label(self, text="Challenge: DQN Player!", font=("Courier", 48))

        self.text1 = tk.Label(self, font=("Courier", 16), wraplength=1000, text="Now let's play against a trained DQN player! This player was trained using the 'Pong' specifications that we have discussed thus far in this tutorial.\n\nFor this challenge, however, we are going to change up the rules a little bit, just for this gameplay:")

        self.challenge_level_one_button = tk.Button(self,
                                    command=lambda: self.challenge_gameplay("one_million"),
                                    text="Challenge: Level 1", font=("Courier", 16))
        self.challenge_level_two_button = tk.Button(self,
                                    command=lambda: self.challenge_gameplay("two_million"),
                                    text="Challenge: Level 2", font=("Courier", 16))
        self.challenge_level_three_button = tk.Button(self,
                                    command=lambda: self.challenge_gameplay("five_million"),
                                    text="Challenge: Level 3", font=("Courier", 16))
        self.challenge_level_four_button = tk.Button(self,
                                    command=lambda: self.challenge_gameplay("ten_million"),
                                    text="Challenge: Level 4", font=("Courier", 16))
        self.challenge_level_five_button = tk.Button(self,
                                    command=lambda: self.challenge_gameplay("fourteen_million"),
                                    text="Challenge: Level 5", font=("Courier", 16))

        self.scoreboard = tk.Frame(self)
        self.player_one_score_label = tk.Label(self.scoreboard, textvariable=self.player_one_score, font=("Courier", 16))
        self.player_two_score_label = tk.Label(self.scoreboard, textvariable=self.player_two_score, font=("Courier", 16))
        self.current_level_label = tk.Label(self.scoreboard, textvariable=self.current_level, font=("Courier", 16))
        self.player_one_score_label.grid(row=0, column=0)
        self.player_two_score_label.grid(row=0, column=2)
        self.current_level_label.grid(row=0, column=1)

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(dqn.replay_memory_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(reflection_on_evolution_of_dqn_player_frame),
                                    text="Next", font=("Courier", 14))
        

        # add toggle texts (args: self, master, text_string, width=1, height=1, wraplength=None, justify=LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        self.text2 = eh.toggle_label(self, "- Instead of using the scoring system from previous, we will now define a point as that when a player succeeds in getting the ball past its opponent. The first player to reach the score of 3 is the winnner.", 
            wraplength=1000, font_size=16, row=2, column=1, width=10, height=3)
        self.text3 = eh.toggle_label(self, "- If you win against the DQN Player, you will move onto the next level. Upon losing or beating Level 5, the game will exit.", 
            wraplength=1000, font_size=16, row=3, column=1, width=10, height=3)
        self.text4 = eh.toggle_label(self, "Training Specifications:\nLevel One: 1,000,000 frames\nLevel Two: 2,000,000 frames\nLevel Three: 5,000,000 frames\nLevel Four: 10,000,000 frames\nLevel Five: 14,000,000 frames", 
            wraplength=1000, font_size=16, row=4, column=1, width=10, height=6)



        # lay widgets
        self.title.grid(row=0, 
                        column=0, 
                        columnspan=3)


        self.text1.grid(row=1, column=1)

        self.challenge_level_one_button.grid(row=5, column=1)
        self.challenge_level_two_button.grid(row=6, column=1)
        self.challenge_level_three_button.grid(row=7, column=1)
        self.challenge_level_four_button.grid(row=8, column=1)
        self.challenge_level_five_button.grid(row=9, column=1)

        self.scoreboard.grid(row=10, column=1)

        self.previous_frame_button.grid(row=11, 
                                        column=0, 
                                        padx=10, 
                                        sticky=tk.W)
        self.to_roadmap_button.grid(row=11, 
                                    column=1, 
                                    columnspan=1)
        self.next_frame_button.grid(row=11, 
                                    column=2, 
                                    padx=10, 
                                    sticky=tk.E)






'''
Reflection On Evolution Of DQN Player

This frame consists of:
- answer field for user to type in reflection

The purpose of this frame is to have the user reflect on how the DQN agent developed over time
from gameplay.
'''
class reflection_on_evolution_of_dqn_player_frame(frame_base.frame_base):
    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        
        # add widgets
        self.title = tk.Label(self, text="Reflection On Evolution Of DQN Player", font=("Courier", 48))
        
        self.text1 = tk.Label(self, justify=tk.LEFT, font=("Courier", 16), wraplength=1000, text="Let's reflect on how the DQN Player evolved level by level! What differences did you notice from Level 1 to Level 2, Level 2 to Level 3, and so on? How was the gameplay of DQN Player similar to that of a human player? How was it different?")
        self.answer_field = tk.Text(self, width=140, height=30)
        self.empty_canvas = tk.Canvas(self, width=100, height=100)

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(challenge_dqn_player_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        
        # lay widgets
        self.title.grid(row=0, 
                        column=0, 
                        columnspan=3)

        self.text1.grid(row=1, column=1)
        self.answer_field.grid(row=2, column=1)

        self.previous_frame_button.grid(row=3, 
                                        column=0, 
                                        padx=10, 
                                        sticky=tk.W)
        self.to_roadmap_button.grid(row=3, 
                                    column=1, 
                                    columnspan=1)
        self.empty_canvas.grid(row=3, column=2)
