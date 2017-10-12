'''
Title: Reinforcement Learning and Deep Q-Network 101
File: image_manipulator.py
Description: Methods that manipulate image files
Company: Artificial Intelligence Research Institute (AIRI)
Author: Channy Hong

'''
from PIL import Image, ImageTk

# takes in Image.open file and spits out resized file
def scale_image(image, scale):
    width, height = image.width, image.height
    new_image = image.resize((int(width*scale), int(height*scale)))
    return new_image

# unused scale image to specified dimension function
def scale_image_dimensions(image, width_scale, height_scale):
	width, height = image.width, image.height
	new_image = image.resize((int(width*width_scale), int(height*height_scale)))
	return new_image