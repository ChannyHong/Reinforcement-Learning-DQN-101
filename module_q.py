'''
Title: Reinforcement Learning and Deep Q-Network 101
File: module_q.py
Description: This is the Q-Learning module
Company: Artificial Intelligence Research Institute (AIRI)
Author: Channy Hong

'''
import Tkinter as tk
import pong_game_control as pgc

import module_frame_base as frame_base
import module_prelude as prelude

import module_play as play
import module_dqn as dqn

import event_handler as eh
from PIL import Image, ImageTk
import image_manipulator as im
import video_animation as va




'''
Action-Value Funtion: Reward

This frame consists of:
- best action scheme from state immediately previous to the non-trivial update
- corresponding explanations

The purpose of this frame is to introduce the idea of assigning a way of measuring action-value.
'''
class action_value_function_reward_frame(frame_base.frame_base):
    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        self.columnconfigure(2, weight=4)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        explanation_width = 50
        explanation_height = 2
        explanation_wraplength = 400
        
        # add widgets
        self.title = tk.Label(self, text="Action-Value Function: Reward", font=("Courier", 48))

        self.text1 = tk.Label(self, font=("Courier", 16), wraplength=1200, justify=tk.LEFT, text="Okay, let's assume we are on the current (time = t) 'state'. We have three choices of action: go up, down, or stay still. According to our strategy [pop up], what action should we take?")

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(play.strategy_from_pong_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(action_value_function_max_q_frame),
                                    text="Next", font=("Courier", 14))

        


        # define scheme frame
        self.scheme_frame = tk.Frame(self)
        self.scheme_frame.columnconfigure(0, weight=1)
        self.scheme_frame.columnconfigure(1, weight=1)
        self.scheme_frame.columnconfigure(2, weight=1)
        self.scheme_frame.rowconfigure(0, weight=1)
        self.scheme_frame.rowconfigure(1, weight=1)
        self.scheme_frame.rowconfigure(2, weight=1)
        self.scheme_frame.rowconfigure(3, weight=1)

        self.time_now = tk.Label(self.scheme_frame, text="time = t", font=("Courier", 14))
        self.time_plus_one = tk.Label(self.scheme_frame, text="time = t + 1", font=("Courier", 14))

        state_width = 210
        state_height = 150

        state_image_scale = 0.1
        original_image_path = 'media/module_q/action_value_function_reward_frame/original.png'
        self.original_image = ImageTk.PhotoImage(im.scale_image(Image.open(original_image_path), state_image_scale))
        self.original_state = tk.Label(self.scheme_frame, width=state_width, height=state_height, image=self.original_image)

        self.time_now.grid(row=0, column=0)
        self.time_plus_one.grid(row=0, column=2)
        self.original_state.grid(row=2, column=0, sticky=tk.E)

        # add best_action_scheme (args: self, master, frame_id, scheme_frame, state_image_scale, button_one_row, button_one_column, button_two_row, button_two_column, button_three_row, button_three_column, state_one_row, state_one_column, state_two_row, state_two_column, state_three_row, state_three_column, state_width, state_height, explanation_row, explanation_column, explanation_width, explanation_height, explanation_wraplength, explanation_string)
        self.best_action_scheme = eh.best_action_scheme(self, "reward", self.scheme_frame, state_image_scale, 1, 1, 2, 1, 3, 1, 1, 2, 2, 2, 3, 2, state_width, state_height, 2, 2, explanation_width, explanation_height, explanation_wraplength, "According to our strategy, it made sense to press up, because it resulted in a state that awarded a reward of 10.")



        # add toggle texts (args: self, master, text_string, width=1, height=1, wraplength=None, justify=LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        function_image_scale = 0.5
        function_image_path = 'media/module_q/action_value_function_reward_frame/function.png'
        self.function_image = ImageTk.PhotoImage(im.scale_image(Image.open(function_image_path), function_image_scale))

        self.explanation_two = eh.toggle_label(self, "Then, for our Q-Learning algorithm, how about we assign a value to an action, or an action-value (otherwise known as a Q-value) at each possible state?", 
            wraplength=explanation_wraplength, row=3, column=2, width=explanation_width, height=explanation_height)
        self.explanation_three = eh.toggle_label(self, "How so? Well, the simplest way to define such an action-value might be to let it be equal to the reward at the resulting state?:", 
            wraplength=explanation_wraplength, row=4, column=2, width=explanation_width, height=explanation_height)
        self.explanation_four = eh.toggle_image(self, image=self.function_image, 
            row=5, column=2, width=400, height=50)
        self.explanation_five = eh.toggle_label(self, "And now, we simply choose to take the action with the largest action-value! We now have an algorithm: a way of deciding which action to take in a given state.", 
            wraplength=explanation_wraplength, row=6, column=2, width=explanation_width, height=explanation_height)

        # lay widgets
        self.title.grid(row=0, 
                        column=0, 
                        columnspan=4)

        self.text1.grid(row=1, column=0, columnspan=4)
        self.scheme_frame.grid(row=2, column=1, rowspan=5, padx=40)

        self.previous_frame_button.grid(row=7, 
                                        column=0, 
                                        padx=10, 
                                        sticky=tk.W)
        self.to_roadmap_button.grid(row=7, 
                                    column=1, 
                                    columnspan=2)
        self.next_frame_button.grid(row=7, 
                                    column=3, 
                                    padx=10, 
                                    sticky=tk.E)

        





'''
Action-Value Function: Max-Q

This frame consists of:
- best action scheme from state two steps previous from non-trivial update

The purpose of this frame is to introduce the idea of adding Max-Q to the currently defined 
action-value.
'''
class action_value_function_max_q_frame(frame_base.frame_base):
    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        self.columnconfigure(2, weight=4)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        explanation_width = 50
        explanation_height = 2
        explanation_wraplength = 400
        
        # add widgets
        self.title = tk.Label(self, text="Action-Value Function: Max Q", font=("Courier", 48))

        self.text1 = tk.Label(self, font=("Courier", 16), wraplength=1200, justify=tk.LEFT, text="How about now, a little further away? Again we have three choices: according to our strategy [pop up], which action should we take?")

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(action_value_function_reward_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(q_learning_algorithm_initialization_frame),
                                    text="Next", font=("Courier", 14))

        


        # define scheme frame
        self.scheme_frame = tk.Frame(self)
        self.scheme_frame.columnconfigure(0, weight=1)
        self.scheme_frame.columnconfigure(1, weight=1)
        self.scheme_frame.columnconfigure(2, weight=1)
        self.scheme_frame.rowconfigure(0, weight=1)
        self.scheme_frame.rowconfigure(1, weight=1)
        self.scheme_frame.rowconfigure(2, weight=1)
        self.scheme_frame.rowconfigure(3, weight=1)

        self.time_now = tk.Label(self.scheme_frame, text="time = t", font=("Courier", 14))
        self.time_plus_one = tk.Label(self.scheme_frame, text="time = t + 1", font=("Courier", 14))

        state_width = 210
        state_height = 150

        state_image_scale = 0.1
        original_image_path = 'media/module_q/action_value_function_max_q_frame/original.png'
        self.original_image = ImageTk.PhotoImage(im.scale_image(Image.open(original_image_path), state_image_scale))
        self.original_state = tk.Label(self.scheme_frame, width=state_width, height=state_height, image=self.original_image)

        self.time_now.grid(row=0, column=0)
        self.time_plus_one.grid(row=0, column=2)
        self.original_state.grid(row=2, column=0, sticky=tk.E)

        # add best_action_scheme (args: self, master, frame_id, scheme_frame, state_image_scale, button_one_row, button_one_column, button_two_row, button_two_column, button_three_row, button_three_column, state_one_row, state_one_column, state_two_row, state_two_column, state_three_row, state_three_column, state_width, state_height, explanation_row, explanation_column, explanation_width, explanation_height, explanation_wraplength, explanation_string)
        self.best_action_scheme = eh.best_action_scheme(self, "max_q", self.scheme_frame, state_image_scale, 1, 1, 2, 1, 3, 1, 1, 2, 2, 2, 3, 2, state_width, state_height, 2, 2, explanation_width, explanation_height, explanation_wraplength, "According to our strategy, it made sense to press up, because the resulting state gets us closer to the state that would give us a positive reward. Note that this requires some forward thinking.")




        # add toggle texts (args: self, master, text_string, width=1, height=1, wraplength=None, justify=LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        function_image_scale = 0.5
        function_image_path = 'media/module_q/action_value_function_max_q_frame/function.png'
        self.function_image = ImageTk.PhotoImage(im.scale_image(Image.open(function_image_path), function_image_scale))

        self.explanation_two = eh.toggle_label(self, "Unfortunately, our current action-value (Q-value) function does not work here because every reward of our immediate resulting states are all the same at 0.", 
            wraplength=explanation_wraplength, row=3, column=2, width=explanation_width, height=explanation_height)
        self.explanation_three = eh.toggle_label(self, "Indeed, our current Q-value function does not have any notion of forward-planning. Then, how do we give our function this necessary sense of directionality?", 
            wraplength=explanation_wraplength, row=4, column=2, width=explanation_width, height=explanation_height)
        self.explanation_four = eh.toggle_label(self, "The answer is simple: have our action-value function take into account any potential future reward! Then on top of what we already have, let's add the maximum available action-value at the resulting state to our function:", 
            wraplength=explanation_wraplength, row=5, column=2, width=explanation_width, height=3)
        self.explanation_five = eh.toggle_image(self, image=self.function_image, 
            row=6, column=2, width=400, height=50)
        self.explanation_six = eh.toggle_label(self, "We now have our 'Q-Learning' algorithm!", 
            wraplength=explanation_wraplength, row=7, column=2, width=explanation_width, height=explanation_height)

        # lay widgets
        self.title.grid(row=0, 
                        column=0, 
                        columnspan=4)

        self.text1.grid(row=1, column=0, columnspan=4)
        self.scheme_frame.grid(row=2, column=1, rowspan=5, padx=40)

        self.previous_frame_button.grid(row=8, 
                                        column=0, 
                                        padx=10, 
                                        sticky=tk.W)
        self.to_roadmap_button.grid(row=8, 
                                    column=1, 
                                    columnspan=2)
        self.next_frame_button.grid(row=8, 
                                    column=3, 
                                    padx=10, 
                                    sticky=tk.E)





'''
Q-Learning Algorithm: Initialization

This frame consists of:
- explanation and image for how to initialize the algorithm

The purpose of this frame is to explain how the states are initialized in Q-Learning algorithm
'''
class q_learning_algorithm_initialization_frame(frame_base.frame_base):
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
        self.title = tk.Label(self, text="Q-Learning Algorithm: Initialization", font=("Courier", 48))
        
        self.text1 = tk.Label(self, font=("Courier", 16), wraplength=1000, justify=tk.LEFT, text="Now, let's see how our Q-Learning Agent equipped with the 'Q-Learning' algorithm actually plays 'Pong'!")

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(action_value_function_max_q_frame),
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(q_learning_algorithm_training_sequence_frame), self.controller.frames[q_learning_algorithm_training_sequence_frame].video_animation.open_video()],
                                    text="Next", font=("Courier", 14))
        
        # add toggle texts (args: self, master, text_string, width=1, height=1, wraplength=None, justify=LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        init_image_scale = 0.5
        init_image_path = 'media/module_q/q_learning_algorithm_initialization_frame/initialization.png'
        self.init_image = ImageTk.PhotoImage(im.scale_image(Image.open(init_image_path), init_image_scale))

        self.text2 = eh.toggle_label(self, "First thing's first, our Q-Learning Agent needs to iterate through every possible (state, action) pairs and initialize their action-values to 0.", 
            wraplength=1000, row=2, column=1)
        self.initialization_image = eh.toggle_image(self, image=self.init_image, 
            row=3, column=1, width=1000, height=200)
        self.text4 = eh.toggle_label(self, "Then, the game will start and our computer player will observe a state in the form of pixel data. It will compare all available action-values (3 of them in our case: up, down, or staying still) at the current state, and simply choose to take the action with the largest action-value.", 
            wraplength=1000, row=4, column=1)

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
                                    column=2, 
                                    padx=10, 
                                    sticky=tk.E)








'''
Q-Learning Algorithm: Training Sequence

This frame consists of:
- animation that details how the training sequence is carried out step by step

The purpose of this frame is to show the user how the training is carried out step by step
using moving visuals.
'''
class q_learning_algorithm_training_sequence_frame(frame_base.frame_base):
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
        self.title = tk.Label(self, text="Q-Learning Algorithm: Training Sequence", font=("Courier", 48))
        
        self.text1 = tk.Label(self, font=("Courier", 16), justify=tk.LEFT, wraplength=1000, text="Each time the computer agent takes an action, it will update its action-value according to the reward and the maximum available action-value of the resulting state. Since every action-value is initialized at 0, the beginning action-value updates will be trivial, until an interesting (non-trivial) case comes up.\n\nNote: We choose randomly to break ties!\n\nLet's take a look at an animation to see this action-value updating process in action:")

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(q_learning_algorithm_initialization_frame), self.video_animation.close_video()],
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(prelude.roadmap_frame), self.video_animation.close_video()],
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(q_learning_algorithm_exploration_v_exploitation_frame), self.video_animation.close_video(), self.controller.frames[q_learning_algorithm_exploration_v_exploitation_frame].video_animation.open_video()],
                                    text="Next", font=("Courier", 14))
        
        # add and lay video animation widget
        self.video_animation = va.video_animation(self, 2, 2, 1, 1, 3, 1, 600, 450, "media/module_q/q_learning_algorithm_training_sequence_frame/q_training_sequence.mov", False, self)

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
Q-Learning Algorithm: Exploration v. Exploitation

This frame consists of:
- explanation for why the algorithm must include a random exploration variable
- animation that shows how the cooling epsilon is used in training

The purpose of this frame is to demonstrate to the users the role of the random exploration
variable.
'''
class q_learning_algorithm_exploration_v_exploitation_frame(frame_base.frame_base):
    def update_current_frame(self, frame_count, current_frame):
        epsilon = int(100-(current_frame / frame_count * 101))
        self.epsilon_value.set("Epsilon: " + str(epsilon) + "%")
        self.epsilon_value_board.update()

    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=8)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)

        self.epsilon_value = tk.StringVar()
        
        # add widgets
        self.title = tk.Label(self, text="Q-Learning Algorithm: Exploration v. Exploitation", font=("Courier", 36))

        self.text1 = tk.Label(self, font=("Courier", 12), wraplength=1000, justify=tk.LEFT, text="In the beginning, choosing actions randomly was the only choice for our Q-Learning Agent, since every action-value was initialized to the identical and trivial value of 0. However, upon a series of random actions - or exploration - our Q-Learning Agent came across an instance of non-trivial action-value update. How exciting!\n\nLet's assume that our Q-Learning Agent continues with its training, and it comes across numerous non-trivial updates to the point where it no longer needs to choose actions randomly to break ties on trivial action-values. So now that our Q-Learning Agent has a non-trivial action-value system, does it make sense for it to continue with its training by only following the current method of blindly taking the action with the highest action-value?")

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(q_learning_algorithm_training_sequence_frame), self.video_animation.close_video(), self.controller.frames[q_learning_algorithm_training_sequence_frame].video_animation.open_video()],
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(prelude.roadmap_frame), self.video_animation.close_video()],
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(action_value_function_revisited_discount_factor_frame), self.video_animation.close_video()],
                                    text="Next", font=("Courier", 14))
        
        # add toggle texts (args: self, master, text_string, width=1, height=1, wraplength=None, justify=LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        self.text2 = eh.toggle_label(self, "Think about this scenario: your town has a McDonald's, a Wendy's, and a Burger King. You like burgers and you frequent the local burger joint, but you have only been to McDonald's thus far. You like McDonald's. However, does this necessarily mean that you should always keep going to McDonald's from now on? What if it turns out that your taste buds are more suited for the Whoppers from Burger King after all?", 
            wraplength=1000, font_size=12, row=2, column=1)
        self.text3 = eh.toggle_label(self, "Similarly, what if the current action-value system does not take into account all possible ways of how best to reap the rewards? What if our Q-Learning algorithm is stuck at a local maxima, and it needs to 'go outside the box' of the current action-value system to properly consider all options?", 
            wraplength=1000, font_size=12, row=3, column=1)
        self.text4 = eh.toggle_label(self, "To this logic, it is useful that our Q-Learning Agent explore erratically during the beginning stages of its training, and eventually cool down the randomness for modest yet persistent exploration onwards. At the beginning, our algorithm needs to avoid focusing only on a handful instances of early reward scenarios, which most likely are not accurate representations of the overall gameplay to come. On a separate note, after enough 'exploration', the frequency of the randomness should decrease, so as to be more focused on fine-tuning the action-value system itself; yet, there should always be a modest room for exploratory behavior!", 
            wraplength=1000, font_size=12, row=4, column=1, height=3)
        

        # add frame and animation
        self.animation_frame = tk.Frame(self)
        self.animation_frame.rowconfigure(0, weight=7)
        self.animation_frame.rowconfigure(1, weight=1)
        self.animation_frame.columnconfigure(0, weight=1)
        self.animation_frame.columnconfigure(1, weight=1)
        self.animation_frame.columnconfigure(2, weight=1)

        self.video_animation = va.video_animation(self.animation_frame, 0, 0, 0, 0, 1, 0, 240, 180, "media/module_q/q_learning_algorithm_exploration_v_exploitation_frame/epsilon.mp4", True, self)
        
        self.epsilon_value_board = tk.Label(self.animation_frame, textvariable=self.epsilon_value, font=("Courier", 16))
        self.epsilon_value_board.grid(row=0, column=1, rowspan=2)

        self.animation_text_frame = tk.Frame(self.animation_frame)
        self.animation_text_frame.grid(row=0, column=2, rowspan=2)
        self.animation_text_frame.rowconfigure(0, weight=1)
        self.animation_text_frame.rowconfigure(1, weight=1)
        self.text5 = eh.toggle_label(self.animation_text_frame, "Let's see the annealing process in action. Here, we introduce a variable called epsilon. With epsilon probability, we will randomly choose our actions rather than following our action-value system. For this example, we will start the epsilon at 100%, and eventually 'cool it down' to the 5% plateau.", 
            wraplength=650, font_size=12, row=0, column=0, width=100, height=5)
        self.text6 = eh.toggle_label(self.animation_text_frame, "By way of exploration, the Q-Learning Agent here discovers a new way of hitting the ball, and this new method is effective in eventually getting ball past its opponent, yielding a reward of 100.", 
            wraplength=650, font_size=12, row=1, column=0, width=100, height=5)


        # lay widgets
        self.title.grid(row=0, 
                        column=0, 
                        columnspan=3)

        self.text1.grid(row=1, column=1)

        self.animation_frame.grid(row=5, column=1)

        self.previous_frame_button.grid(row=6, 
                                        column=0, 
                                        padx=0, 
                                        sticky=tk.W)
        self.to_roadmap_button.grid(row=6, 
                                    column=1, 
                                    columnspan=1)
        self.next_frame_button.grid(row=6, 
                                    column=2, 
                                    padx=0, 
                                    sticky=tk.E)








'''
Action-Value Function Revisited: Discount Factor

This frame consists of:
- explanation for why the Max-Q clause in the action-value function must be discounted
- supporting image

The purpose of this frame is to demonstrate to the users the purpose of the discount factor
variable.
'''
class action_value_function_revisited_discount_factor_frame(frame_base.frame_base):
    def create_widgets(self):

        # set column and row spacing for the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=8)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        
        # add widgets
        self.title = tk.Label(self, text="Action-Value Function Revisited: Discount Factor", font=("Courier", 36))
        
        self.row_one_frame = tk.Frame(self)
        self.row_two_frame = tk.Frame(self)
        self.row_five_frame = tk.Frame(self)

        self.text1 = tk.Label(self.row_one_frame, font=("Courier", 14), wraplength=500, justify=tk.LEFT, text="Now, let's go back to our action-value function!")

        self.previous_frame_button = tk.Button(self,
                                    command=lambda: [self.controller.show_frame(q_learning_algorithm_exploration_v_exploitation_frame), self.controller.frames[q_learning_algorithm_exploration_v_exploitation_frame].video_animation.open_video()],
                                    text="Previous", font=("Courier", 14))
        self.to_roadmap_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(prelude.roadmap_frame),
                                    text="To Roadmap", font=("Courier", 14))
        self.next_frame_button = tk.Button(self,
                                    command=lambda: self.controller.show_frame(dqn.the_large_problem_with_pixel_input_frame),
                                    text="Next", font=("Courier", 14))
        

        # add toggle texts (args: self, master, text_string, width=1, height=1, wraplength=None, justify=LEFT, row=0, column=0, rowspan=1, columnspan=1, font_type="Courier", font_size=16)
        q_function_original_image_scale = 0.5
        q_function_original_image_path = 'media/module_q/action_value_function_revisited_discount_factor_frame/original.png'
        self.q_function_original_image = ImageTk.PhotoImage(im.scale_image(Image.open(q_function_original_image_path), q_function_original_image_scale))
        self.image_one = eh.toggle_image(self.row_one_frame, image=self.q_function_original_image, 
            row=0, column=1, width=600, height=100)

        states_image_scale = 0.5
        states_image_path = 'media/module_q/action_value_function_revisited_discount_factor_frame/states.png'
        self.states_image = ImageTk.PhotoImage(im.scale_image(Image.open(states_image_path), states_image_scale))
        self.image_two = eh.toggle_image(self.row_two_frame, image=self.states_image, 
            row=0, column=0, width=600, height=200)
        self.text2 = eh.toggle_label(self.row_two_frame, "As you can see, the action-value for certain (action, state) pairs are all equal to one another at 10, regardless of how far away it may be in time to the actual reward-reaping instance!", 
            wraplength=300, font_size=14, row=0, column=1, width=40)

        self.text3 = eh.toggle_label(self, "Indeed, with certain degrees of uncertainty as introduced with the epsilon variable from before, this can become problematic. What's more, we also have to take into account the various uncertainties derived from our adversary and the environment itself.", 
            wraplength=1000, font_size=14, row=3, column=1, height=2)
        self.text4 = eh.toggle_label(self, "The idea is that future rewards that are far away should be counted less, since there is a higher uncertainty of reaching that reward-reaping state.", 
            wraplength=1000, font_size=14, row=4, column=1, height=2)

        q_function_updated_image_scale = 0.5
        q_function_updated_image_path = 'media/module_q/action_value_function_revisited_discount_factor_frame/updated.png'
        self.q_function_updated_image = ImageTk.PhotoImage(im.scale_image(Image.open(q_function_updated_image_path), q_function_updated_image_scale))
        self.image_three = eh.toggle_image(self.row_five_frame, image=self.q_function_updated_image, 
            row=0, column=1, width=600, height=100)
        self.text5 = eh.toggle_label(self.row_five_frame, "And we can do this by casting a bit of doubt to the 'forward-planning' aspect of our action-value function, by multiplying with a gamma constant between 0 and 1 representing what's known as the 'discount factor.'", 
            wraplength=300, font_size=14, width=40, row=0, column=0)

        # lay widgets
        self.title.grid(row=0, 
                        column=0, 
                        columnspan=3)

        self.row_one_frame.grid(row=1, column=1)
        self.row_two_frame.grid(row=2, column=1)
        self.row_five_frame.grid(row=5, column=1)

        self.text1.grid(row=0, column=0)

        self.previous_frame_button.grid(row=6, 
                                        column=0, 
                                        padx=0, 
                                        sticky=tk.W)
        self.to_roadmap_button.grid(row=6, 
                                    column=1, 
                                    columnspan=1)
        self.next_frame_button.grid(row=6, 
                                    column=7, 
                                    padx=0, 
                                    sticky=tk.E)
