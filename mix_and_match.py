'''
Title: Reinforcement Learning and Deep Q-Network 101
File: mix_and_match.py
Description: Implementation of the mix and match canvas
Company: Artificial Intelligence Research Institute (AIRI)
Author: Channy Hong

'''
import Tkinter as tk

# anchor properties
class mam_anchor():
	def __init__(self, master, id_number, center_x, center_y, radius):
		master.create_oval(center_x-radius, center_y-radius, center_x+radius, center_y+radius)
		self.id_number = id_number
		self.center_x = center_x
		self.center_y = center_y
		self.top = center_y - radius
		self.bottom = center_y + radius
		self.left = center_x - radius
		self.right = center_x + radius
		self.occupied = False

# line properties
class mam_line():
	def __init__(self, master, start_x, start_y, end_x, end_y):
		self.line_tag = master.create_line(start_x, start_y, end_x, end_y, width=2)
		self.left_anchor_id_number = None
		self.right_anchor_id_number = None

# the mix and match canvas
class mix_and_match(tk.Canvas):
	def __init__(self, master, grid_top, grid_bottom, grid_left, grid_right):
		tk.Canvas.__init__(self, master, width=400, height=500)
		self.master = master
		# create left side anchors
		l1 = mam_anchor(self, 1, 18, 70, 15)
		l2 = mam_anchor(self, 2, 18, 200, 15)
		l3 = mam_anchor(self, 3, 18, 325, 15)
		l4 = mam_anchor(self, 4, 18, 440, 15)
		self.left_anchors = [l1, l2, l3, l4]
		# create right side anchors
		r1 = mam_anchor(self, 5, 375, 32, 15)
		r2 = mam_anchor(self, 6, 375, 105, 15)
		r3 = mam_anchor(self, 7, 375, 204, 15)
		r4 = mam_anchor(self, 8, 375, 300, 15)
		r5 = mam_anchor(self, 9, 375, 365, 15)
		r6 = mam_anchor(self, 10, 375, 435, 15)
		self.right_anchors = [r1, r2, r3, r4, r5, r6]

		# initialize variables
		self.lines = []
		self.draw_initiated = 0
		self.new_line = None
		self.clicked_anchor_id_number = 0
		self.line_count = 0

		# bind events
		self.bind("<Button-1>", self.initialize_line)
		self.bind("<Button1-Motion>", self.sketch_line)
		self.bind("<ButtonRelease-1>", self.confirm_line)

		# lay canvas
		self.grid(row=grid_top, column=grid_left, rowspan=grid_bottom-grid_top+1, columnspan=grid_right-grid_left+1)

	# initialize line when left click
	def initialize_line(self, event):
		self.draw_initiated = 0
		# get coordinates of the click
		clicked_x = self.canvasx(event.x)
		clicked_y = self.canvasy(event.y)

        # proceed only if clicked region is inside an anchor
		for anchor in self.left_anchors:
			if (anchor.top < clicked_y) and (anchor.bottom > clicked_y) and (anchor.left < clicked_x) and (anchor.right > clicked_x):
				self.clicked_anchor_id_number = anchor.id_number
		for anchor in self.right_anchors:
			if (anchor.top < clicked_y) and (anchor.bottom > clicked_y) and (anchor.left < clicked_x) and (anchor.right > clicked_x):
				self.clicked_anchor_id_number = anchor.id_number

		# if clicked region is inside an anchor, remove the line already occupying that anchor, if exists
		if self.clicked_anchor_id_number != 0:
			for line in self.lines:
				if (self.clicked_anchor_id_number == line.left_anchor_id_number) or (self.clicked_anchor_id_number == line.right_anchor_id_number):
					self.delete(line.line_tag)
					self.lines.remove(line)
					self.left_anchors[line.left_anchor_id_number-1].occupied = False
					self.right_anchors[(line.right_anchor_id_number-len(self.left_anchors))-1].occupied = False
					self.line_count -= 1
			# initiate drawing phase
			self.draw_initiated = 1


	# sketch line as cursor moves
	def sketch_line(self, event):
		if self.draw_initiated == 1:
			start_x = None
			start_y = None

			# get line start position as center of that initial anchor
			if self.clicked_anchor_id_number <= len(self.left_anchors): # clicked left anchor
				start_x = self.left_anchors[self.clicked_anchor_id_number-1].center_x
				start_y = self.left_anchors[self.clicked_anchor_id_number-1].center_y
			elif self.clicked_anchor_id_number > len(self.left_anchors): # clicked right anchor
				start_x = self.right_anchors[(self.clicked_anchor_id_number-len(self.left_anchors))-1].center_x
				start_y = self.right_anchors[(self.clicked_anchor_id_number-len(self.left_anchors))-1].center_y

			# get current cursor position
			mouse_x = self.canvasx(event.x)
			mouse_y = self.canvasy(event.y)

			# remove the most recent version of that same line instance
			if len(self.lines)>self.line_count:
				old_line = self.lines.pop()
				self.delete(old_line.line_tag)

			# update the line instance with a new line
			new_line = mam_line(self, start_x, start_y, mouse_x, mouse_y)
			self.lines.append(new_line)
			self.master.update_idletasks()


	# confirm line when left click is lifted
	def confirm_line(self, event):
		if self.draw_initiated == 1:

			# get left click lift coordinates
			released_x = self.canvasx(event.x)
			released_y = self.canvasy(event.y)

			line_valid = 0
			new_line = self.lines.pop() # pop the msot recent versionn of the line instance for now

			# if lifted at valid region (right side if start anchor was left side, vice versa, and end anchor is not occupied)
			if self.clicked_anchor_id_number <= len(self.left_anchors): # start anchor was left side
				for anchor in self.right_anchors:
					if (anchor.top < released_y) and (anchor.bottom > released_y) and (anchor.left < released_x) and (anchor.right > released_x) and (not anchor.occupied):
						self.delete(new_line.line_tag)
						new_line = mam_line(self, self.left_anchors[self.clicked_anchor_id_number-1].center_x, self.left_anchors[self.clicked_anchor_id_number-1].center_y, anchor.center_x, anchor.center_y)
						new_line.left_anchor_id_number = self.clicked_anchor_id_number
						new_line.right_anchor_id_number = anchor.id_number
						self.lines.append(new_line)
						self.line_count += 1
						anchor.occupied = True
						self.left_anchors[self.clicked_anchor_id_number-1].occupied = True
						line_valid = 1
			elif self.clicked_anchor_id_number > len(self.left_anchors): # start anchor was right side
				for anchor in self.left_anchors:
					if (anchor.top < released_y) and (anchor.bottom > released_y) and (anchor.left < released_x) and (anchor.right > released_x) and (not anchor.occupied):
						self.delete(new_line.line_tag)
						new_line = mam_line(self, anchor.center_x, anchor.center_y, self.right_anchors[(self.clicked_anchor_id_number-len(self.left_anchors))-1].center_x, self.right_anchors[(self.clicked_anchor_id_number-len(self.left_anchors))-1].center_y)
						new_line.left_anchor_id_number = anchor.id_number
						new_line.right_anchor_id_number = self.clicked_anchor_id_number
						self.lines.append(new_line)
						self.line_count += 1
						anchor.occupied = True
						self.right_anchors[(self.clicked_anchor_id_number-len(self.left_anchors))-1].occupied = True
						line_valid = 1

			# if not valid, reset
			if line_valid == 0:
				self.delete(new_line.line_tag)
				self.draw_initiated = 0
				self.clicked_anchor_id_number = 0


	# check whether existing lines are correct or not
	def check_answer(self):
		for line in self.lines:
			correct = False

			# check if line is one of the correct configurations
			if (line.left_anchor_id_number == 1) and (line.right_anchor_id_number == 9):
				correct = True
			elif (line.left_anchor_id_number == 2) and (line.right_anchor_id_number == 7):
				correct = True
			elif (line.left_anchor_id_number == 3) and (line.right_anchor_id_number == 8):
				correct = True
			elif (line.left_anchor_id_number == 4) and (line.right_anchor_id_number == 5):
				correct = True

			# if correct, turn the line green (place a green line over it)
			if correct:
				self.itemconfig(line.line_tag, fill="green")

			# if incorrect, turn the line red (place a red line over it)
			else: 
				self.itemconfig(line.line_tag, fill="red")










