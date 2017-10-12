'''
Title: Reinforcement Learning and Deep Q-Network 101
File: module_frame_base.py
Description: Definition of frame base
Company: Artificial Intelligence Research Institute (AIRI)
Author: Channy Hong

'''
import Tkinter as tk

# the frame base, which is the parent class of all pages (frames) in tutorial
class frame_base(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.grid(row=0, column=0, sticky=tk.NW+tk.SE)
        self.create_widgets()

    def create_widgets(self):
        raise NotImplementedError
