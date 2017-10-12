'''
Title: Reinforcement Learning and Deep Q-Network 101
File: event_handler.py
Description: Objects that facilitates various user interaction
Company: Artificial Intelligence Research Institute (AIRI)
Author: Channy Hong

'''
import Tkinter as tk
from PIL import Image, ImageTk

import image_manipulator as im


# pygame_event that acts as a communication channel between 'Pong' pygame interface and the tutorial itself
class pygame_event:
	def __init__(self, master):
		self.master = master
		self.player_one_score = 0
		self.player_two_score = 0
		self.in_play = False

	# update score for non-challenge gameplay
	def update_score(self, player_one_score, player_two_score):
		self.player_one_score = player_one_score
		self.player_two_score = player_two_score
		self.master.update_score(self.player_one_score, self.player_two_score)

	# update score for challenge gameplay
	def update_challenge_score(self, player_one_challenge_score, player_two_challenge_score):
		self.player_one_challenge_score = player_one_challenge_score
		self.player_two_challenge_score = player_two_challenge_score
		self.master.update_challenge_score(self.player_one_challenge_score, self.player_two_challenge_score)

	# move onto next level of the challenge gameplay
	def next_level(self, current_trained_steps):
		next_trained_steps = None

		if current_trained_steps == "one_million":
			next_trained_steps = "two_million"
		if current_trained_steps == "two_million":
			next_trained_steps = "five_million"
		if current_trained_steps == "five_million":
			next_trained_steps = "ten_million"
		if current_trained_steps == "ten_million":
			next_trained_steps = "fourteen_million"

		self.master.challenge_gameplay(next_trained_steps)

# toggle text that shows and hides the text upon left mouse click
class toggle_label(tk.Label):
	def __init__(self, 
			master, 
			text_string, 
			width=1, 
			height=1, 
			wraplength=None, 
			justify=tk.LEFT, 
			row=0, 
			column=0, 
			rowspan=1, 
			columnspan=1,
			font_type="Courier",
			font_size=16):
		tk.Label.__init__(self, 
			master, 
			text=text_string, 
			borderwidth=3, 
			relief="groove", 
			width=width, 
			height=height, 
			wraplength=wraplength, 
			justify=justify,
			font=(font_type, font_size))
		self.screen = tk.Canvas(master, 
			borderwidth=3, 
			relief="groove", 
			width=width, 
			height=height)
		self.screen.bind("<Button-1>", self.show)
		self.bind("<Button-1>", self.hide)
		self.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky=tk.NW+tk.SE)
		self.screen.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky=tk.NW+tk.SE)
		self.hidden = True

	def show(self, event):
		if self.hidden:
			self.lift(self.screen)
			self.hidden = False
		
	def hide(self, event):
		if not self.hidden:
			self.lower(self.screen)	
			self.hidden = True

# toggle image that shows and hides upon left mouse click
class toggle_image(tk.Label):
	def __init__(self, 
			master, 
			image, 
			width=1, 
			height=1,
			row=0, 
			column=0, 
			rowspan=1, 
			columnspan=1):
		tk.Label.__init__(self, 
			master, 
			image=image, 
			borderwidth=3, 
			relief="groove", 
			width=width, 
			height=height)
		self.screen = tk.Canvas(master, 
			borderwidth=3, 
			relief="groove", 
			width=width, 
			height=height)
		self.screen.bind("<Button-1>", self.show)
		self.bind("<Button-1>", self.hide)
		self.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky=tk.NW+tk.SE)
		self.screen.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky=tk.NW+tk.SE)
		self.hidden = True

	def show(self, event):
		if self.hidden:
			self.lift(self.screen)
			self.hidden = False
		
	def hide(self, event):
		if not self.hidden:
			self.lower(self.screen)	
			self.hidden = True


# best action scheme used in action-value function frames: shows corresponding state when action buttons are pressed and shows all when explanation toggle text is shown
class best_action_scheme:
	def __init__(self,
		master,
		frame_id,
		scheme_frame,
		state_image_scale,
		button_one_row, button_one_column,
		button_two_row, button_two_column,
		button_three_row, button_three_column,
		state_one_row, state_one_column,
		state_two_row, state_two_column,
		state_three_row, state_three_column,
		state_width, state_height,
		explanation_row, explanation_column,
		explanation_width, explanation_height, explanation_wraplength,
		explanation_string):

		# state hidden booleans
		self.state_one_hidden = True
		self.state_two_hidden = True
		self.state_three_hidden = True
		self.explanation_hidden = True

		# specify and add components
		button_image_scale = 0.3
		up_image_path = "media/event_handler/shared/up.png"
		self.up_image = ImageTk.PhotoImage(im.scale_image(Image.open(up_image_path), button_image_scale))
		down_image_path = "media/event_handler/shared/down.png"
		self.down_image = ImageTk.PhotoImage(im.scale_image(Image.open(down_image_path), button_image_scale))

		self.button_one = tk.Button(scheme_frame, command=lambda: self.show_state_one(), image=self.up_image)
		self.button_two = tk.Button(scheme_frame, command=lambda: self.show_state_two(), text="Press\nNothingg ", font=("Courier", 14), wraplength=64) # little hack to make the button look as it does
		self.button_three = tk.Button(scheme_frame, command=lambda: self.show_state_three(), image=self.down_image)

		state_one_image_path = "media/event_handler/best_action_scheme_" + frame_id + "/one.png"
		self.state_one_image = ImageTk.PhotoImage(im.scale_image(Image.open(state_one_image_path), state_image_scale))
		self.state_one = tk.Label(scheme_frame, width=state_width, height=state_height, image=self.state_one_image, bg='green')
		self.state_one_screen = tk.Canvas(scheme_frame, width=state_width, height=state_height)

		state_two_image_path = "media/event_handler/best_action_scheme_" + frame_id + "/two.png"
		self.state_two_image = ImageTk.PhotoImage(im.scale_image(Image.open(state_two_image_path), state_image_scale))
		self.state_two = tk.Label(scheme_frame, width=state_width, height=state_height, image=self.state_two_image, bg='red')
		self.state_two_screen = tk.Canvas(scheme_frame, width=state_width, height=state_height)

		state_three_image_path = "media/event_handler/best_action_scheme_" + frame_id + "/three.png"
		self.state_three_image = ImageTk.PhotoImage(im.scale_image(Image.open(state_three_image_path), state_image_scale))
		self.state_three = tk.Label(scheme_frame, width=state_width, height=state_height, image=self.state_three_image, bg='red')
		self.state_three_screen = tk.Canvas(scheme_frame, width=state_width, height=state_height)

		self.explanation = tk.Label(master, wraplength=explanation_wraplength, width=explanation_width, height=explanation_height, justify=tk.LEFT, text=explanation_string, borderwidth=3, relief="groove", font=("Courier", 16))
		self.explanation_screen = tk.Canvas(master, width=explanation_width, height=explanation_height, borderwidth=3, relief="groove")
		self.explanation.bind("<Button-1>", self.hide_explanation)
		self.explanation_screen.bind("<Button-1>", self.show_explanation)

		# lay components
		self.button_one.grid(row=button_one_row, column=button_one_column)
		self.button_two.grid(row=button_two_row, column=button_two_column)
		self.button_three.grid(row=button_three_row, column=button_three_column)

		self.state_one.grid(row=state_one_row, column=state_one_column, sticky=tk.NW+tk.SE)
		self.state_one_screen.grid(row=state_one_row, column=state_one_column, sticky=tk.NW+tk.SE)
		self.state_two.grid(row=state_two_row, column=state_two_column, sticky=tk.NW+tk.SE)
		self.state_two_screen.grid(row=state_two_row, column=state_two_column, sticky=tk.NW+tk.SE)
		self.state_three.grid(row=state_three_row, column=state_three_column, sticky=tk.NW+tk.SE)
		self.state_three_screen.grid(row=state_three_row, column=state_three_column, sticky=tk.NW+tk.SE)

		self.explanation.grid(row=explanation_row, column=explanation_column, sticky=tk.NW+tk.SE)
		self.explanation_screen.grid(row=explanation_row, column=explanation_column, sticky=tk.NW+tk.SE)

	def show_state_one(self):
		if self.state_one_hidden:
			self.state_one.lift(self.state_one_screen)
			self.state_one_hidden = False
	
	def show_state_two(self):
		if self.state_two_hidden:
			self.state_two.lift(self.state_two_screen)
			self.state_two_hidden = False

	def show_state_three(self):
		if self.state_three_hidden:
			self.state_three.lift(self.state_three_screen)
			self.state_three_hidden = False

	def show_explanation(self, event):
		if self.explanation_hidden:
			self.explanation.lift(self.explanation_screen)
			self.explanation_hidden = False
		self.show_state_one()
		self.show_state_two()
		self.show_state_three()

	def hide_explanation(self, event):
		if not self.explanation_hidden:
			self.explanation.lower(self.explanation_screen)
			self.explanation_hidden = True





		