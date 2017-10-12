'''
Title: Implementation of 'Pong' playing agent using Deep Q-Networks
File: video_animation.py
Description: Implementation of video player and slider using cv2
Company: Artificial Intelligence Research Institute (AIRI)
Author: Channy Hong

'''
import Tkinter as tk
import cv2
import numpy as np
from PIL import Image, ImageTk

import image_manipulator as im


# the video animation class
class video_animation(tk.Frame):
	def __init__(self, master, grid_top, grid_bottom, grid_left, grid_right, controller_row, controller_column, width, height, video_path, update_requested, update_frame=None):
		tk.Frame.__init__(self, master, width=width, height=height)
		self.master = master
		self.update_requested = update_requested
		self.update_frame = update_frame

		# video configuration
		self.video_path = video_path
		self.video_label = tk.Label(self)
		self.video_label.grid(row=0, column=0)
		self.video_width = width
		self.current_frame = 0


		# controller menu with play/pause and slider 
		self.controller = tk.Frame(self.master)
		
		button_image_scale = 0.2
		play_image_path = "media/video_animation/play.png"
		self.play_image = ImageTk.PhotoImage(im.scale_image(Image.open(play_image_path), button_image_scale))
		self.play_button = tk.Label(self.controller, image=self.play_image)
		pause_image_path = "media/video_animation/pause.png"
		self.pause_image = ImageTk.PhotoImage(im.scale_image(Image.open(pause_image_path), button_image_scale))
		self.pause_button = tk.Label(self.controller, image=self.pause_image)
		self.play_button.lift(self.pause_button)

		self.play_button.bind("<Button-1>", self.play)
		self.pause_button.bind("<Button-1>", self.pause)

		self.play_button.grid(row=0, column=0, sticky=tk.NW+tk.SE)
		self.pause_button.grid(row=0, column=0, sticky=tk.NW+tk.SE)


		# lay frame and controller
		self.grid(row=grid_top, column=grid_left, rowspan=grid_bottom-grid_top+1, columnspan=grid_right-grid_left+1)
		self.controller.grid(row=controller_row, column=controller_column)

		self.playing = False

	# open video
	def open_video(self):
		self.video = cv2.VideoCapture(self.video_path)
		self.frame_count = self.video.get(cv2.CAP_PROP_FRAME_COUNT)

		self.slider = tk.Scale(self.controller, from_=0, to=self.frame_count, length=self.video_width-100, showvalue=0, orient=tk.HORIZONTAL)
		self.slider.grid(row=0, column=1)

		self.play_animation()

	# close video
	def close_video(self):
		self.video.release()

	# main animation method
	def play_animation(self):
		# if master requests current frame 
		if self.update_requested:
			self.update_frame.update_current_frame(self.frame_count, self.current_frame)

		# reset if animation is over
		if self.current_frame > self.frame_count-38:
			self.playing = False
			self.current_frame = self.frame_count-38
			self.slider.set(self.current_frame)

		# read video at current frame
		self.video.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame)
		_, image = self.video.read()

		# resize video
		ratio = float(self.video_width) / image.shape[1]
		dimension = (self.video_width, int(image.shape[0] * ratio))
		image = cv2.resize(image, dimension, interpolation = cv2.INTER_AREA)

		# display video
		cv2image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
		img = Image.fromarray(cv2image)
		imgtk = ImageTk.PhotoImage(image=img)

		self.video_label.imgtk = imgtk
		self.video_label.configure(image=imgtk)

		# if playing, increment frame by one
		if self.playing:
			self.current_frame += 1
			self.slider.set(self.current_frame)

		# if not playing, update current frame to current slider position
		if not self.playing:
			self.current_frame = self.slider.get()

		self.video_label.after(10, self.play_animation)

	# play mode
	def play(self, event):
		self.playing = True
		self.pause_button.lift(self.play_button)

	# pause mode
	def pause(self, event):
		self.playing = False
		self.play_button.lift(self.pause_button)




