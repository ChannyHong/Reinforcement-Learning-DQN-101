'''
Title: Reinforcement Learning and Deep Q-Network 101
File: learning_dqn_with_pong.py
Description: This is the main file of the tutorial that initializes all the pages (frames) and
              processes queries regarding each of them (especially in terms of jumping between
              pages)
Company: Artificial Intelligence Research Institute (AIRI)
Author: Channy Hong

'''

import Tkinter as tk
import pong_game_control as pgc

import module_frame_base as frame_base
import module_prelude as prelude

import module_intro as intro
import module_play as play
import module_q as q
import module_dqn as dqn
import module_challenge as challenge



# the main window class
class main_window(tk.Tk):
    def __init__(self):
        # initalize the 
        tk.Tk.__init__(self)
        self.title("Learning DQN With Pong")
        self.create_widgets()
        self.minsize(width=640, height=480)
        self.geometry("1240x680+100+100")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def create_widgets(self):
        # make the container frame
        self.container = tk.Frame(self)
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)
        self.container.grid(row=0, column=0, sticky=tk.NW+tk.SE)

        # initialize all frames
        self.frames = {}
        for f in (prelude.title_frame, 
                  prelude.roadmap_frame, 
                  intro.tutorial_overview_frame,
                  intro.artificial_intelligence_frame,
                  intro.ai_in_the_21st_century_frame,
                  intro.briefly_on_q_learning_and_deep_q_network_frame,
                  play.pong_gameplay_frame,
                  play.reflection_on_pong_gameplay_frame,
                  play.terminology_definition_frame,
                  play.terminology_pong_mix_and_match_frame,
                  play.strategy_from_pong_frame,
                  q.action_value_function_reward_frame,
                  q.action_value_function_max_q_frame,
                  q.q_learning_algorithm_initialization_frame,
                  q.q_learning_algorithm_training_sequence_frame,
                  q.q_learning_algorithm_exploration_v_exploitation_frame,
                  q.action_value_function_revisited_discount_factor_frame,
                  dqn.the_large_problem_with_pixel_input_frame,
                  dqn.q_network_frame,
                  dqn.q_network_training_sequence_frame,
                  dqn.replay_memory_frame,
                  challenge.challenge_dqn_player_frame,
                  challenge.reflection_on_evolution_of_dqn_player_frame):
            frame = f(self.container, self)
            self.frames[f] = frame

        # start the show
        self.show_frame(prelude.title_frame)

    def show_frame(self, selected_frame):
        self.frames[selected_frame].tkraise()



# the main function
def main():
	app = main_window()
	app.mainloop()
	exit()

if __name__ == "__main__":
    main()