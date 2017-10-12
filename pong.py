'''
Title: Reinforcement Learning and Deep Q-Network 101
File: pong.py
Description: Implementation of the game 'Pong'
Company: Artificial Intelligence Research Institute (AIRI)
Author: Channy Hong

'''

import numpy as np
import random, pygame, sys
from pygame.locals import *

import tensorflow as tf

# game speed variable
GAME_SPEED = 1

# reward setting
TERMINAL_REWARD = 100
STEP_REWARD = 10

# window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

# line thickness
LINE_THICKNESS = 8

# paddle dimensions
PADDLE_SIZE = 60
PADDLE_OFFSET = 20
PADDLE_EDGE_BUFFER = 15

# color setup
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# movement size
KEYBOARD_MOVEMENT_SIZE = 40

# computer competency
COMPUTER_COMPETENCY = 0.1


# draw the arena
def draw_arena():
	# fill the display surface
	DISPLAY_SURF.fill(BLACK)
	# draw the outline of the arena
	pygame.draw.rect(DISPLAY_SURF, WHITE, ((0, 0), (WINDOW_WIDTH, WINDOW_HEIGHT)), LINE_THICKNESS * 2)
	# draw the center line
	pygame.draw.line(DISPLAY_SURF, WHITE, ((WINDOW_WIDTH / 2), 0), ((WINDOW_WIDTH / 2), WINDOW_HEIGHT), (LINE_THICKNESS / 4))

# draw the paddle
def draw_paddle(paddle):
	# stops paddle if moving too low
	if paddle.bottom > WINDOW_HEIGHT - LINE_THICKNESS:
		paddle.bottom = WINDOW_HEIGHT - LINE_THICKNESS
	# stops paddle if moving too high
	elif paddle.top < LINE_THICKNESS:
		paddle.top = LINE_THICKNESS
	# draw paddle
	pygame.draw.rect(DISPLAY_SURF, WHITE, paddle)

# draw the ball
def draw_ball(ball):
	pygame.draw.rect(DISPLAY_SURF, WHITE, ball)

# move the ball to the new position
def move_ball(ball, ball_direction_x, ball_direction_y):
	ball.x += (ball_direction_x * GAME_SPEED)
	ball.y += (ball_direction_y * GAME_SPEED)
	return ball

# check collision with edge and change sign of direction if yes
def check_edge_collision(ball, ball_direction_x, ball_direction_y):
	ball_done = 0
	if ball.top <= (LINE_THICKNESS) or ball.bottom >= (WINDOW_HEIGHT - LINE_THICKNESS):
		ball_direction_y = ball_direction_y * -1
	if ball.left <= (LINE_THICKNESS):
		ball_direction_x = ball_direction_x * -1
		ball_done = 1
	if ball.right >= (WINDOW_WIDTH - LINE_THICKNESS):
		ball_direction_x = ball_direction_x * -1
		ball_done = 2
	return ball_direction_x, ball_direction_y, ball_done

# check collision with paddle and change sign of x_direction if yes
def check_paddle_collision(ball, ball_direction_x, ball_direction_y, paddle_one, paddle_two, player_one_reward, player_two_reward):
	if ball_direction_x == -1 and paddle_one.right >= ball.left and paddle_one.top <= ball.top and paddle_one.bottom >= ball.bottom:
		# player one hit paddle edge so reverse x and y direction
		if (paddle_one.top + PADDLE_EDGE_BUFFER >= ball.bottom and (ball_direction_y == 1)) or ((paddle_one.bottom - PADDLE_EDGE_BUFFER <= ball.top) and (ball_direction_y == -1)):
			return [-1,-1, player_one_reward + STEP_REWARD, player_two_reward]
		# player one hit paddle normally so reverse x direction
		else:
			return [-1, 1, player_one_reward + STEP_REWARD, player_two_reward]
	elif ball_direction_x == 1 and paddle_two.left <= ball.right and paddle_two.top <= ball.top and paddle_two.bottom >= ball.bottom:
		# player two hit paddle edge so reverse x and y direction
		if (paddle_two.top + PADDLE_EDGE_BUFFER >= ball.bottom and (ball_direction_y == 1)) or ((paddle_two.bottom - PADDLE_EDGE_BUFFER <= ball.top) and (ball_direction_y == -1)):
			return [-1,-1, player_one_reward, player_two_reward + STEP_REWARD]
		# player two hit paddle normally so reverse x direction
		else:
			return [-1, 1, player_one_reward, player_two_reward + STEP_REWARD]
	else:
		return [1, 1, player_one_reward, player_two_reward]

# reset the game
def reset_ball():
	initial_ball_x = (WINDOW_WIDTH / 2) - (LINE_THICKNESS / 2)
	initial_ball_y = (WINDOW_HEIGHT / 2) - (LINE_THICKNESS / 2)
	
	ball = pygame.Rect(initial_ball_x, initial_ball_y, LINE_THICKNESS, LINE_THICKNESS)

	x_random = random.random()
	y_random = random.random()

	if x_random < 0.5:
		ball_direction_x = -1 # left
	else:
		ball_direction_x = 1 # right

	if y_random < 0.5:
		ball_direction_y = -1 # up
	else:
		ball_direction_y = 1 # down


	return ball, ball_direction_x, ball_direction_y

# computer complayer algorithm
def move_computer_paddle(ball, ball_direction_x, paddle, player):
	paddle_y_position = paddle.y
	# if computer agent is player 1 (left)
	if player == 1:
		# if ball is moving away from the computer player, then center the paddle
		if ball_direction_x == 1:
			if paddle.centery < (WINDOW_HEIGHT / 2):
				paddle_y_position += binary_probability(KEYBOARD_MOVEMENT_SIZE, COMPUTER_COMPETENCY/10)
			elif paddle.centery > (WINDOW_HEIGHT / 2):
				paddle_y_position -= binary_probability(KEYBOARD_MOVEMENT_SIZE, COMPUTER_COMPETENCY/10)
		# if ball is moving towards the computer player, then track its movement
		elif ball_direction_x == -1:
			if paddle.centery < ball.centery-KEYBOARD_MOVEMENT_SIZE:
				paddle_y_position += binary_probability(KEYBOARD_MOVEMENT_SIZE, COMPUTER_COMPETENCY)
			elif paddle.centery > ball.centery+KEYBOARD_MOVEMENT_SIZE:
				paddle_y_position -= binary_probability(KEYBOARD_MOVEMENT_SIZE, COMPUTER_COMPETENCY)

	# if computer agent is player 2 (right)
	elif player == 2:
		# if ball is moving away from the computer player, then center the paddle
		if ball_direction_x == -1:
			if paddle.centery < (WINDOW_HEIGHT / 2):
				paddle_y_position += binary_probability(KEYBOARD_MOVEMENT_SIZE, COMPUTER_COMPETENCY/10)
			elif paddle.centery > (WINDOW_HEIGHT / 2):
				paddle_y_position -= binary_probability(KEYBOARD_MOVEMENT_SIZE, COMPUTER_COMPETENCY/10)
		# if ball is moving towards the computer player, then track its movement
		elif ball_direction_x == 1:
			if paddle.centery < ball.centery-KEYBOARD_MOVEMENT_SIZE:
				paddle_y_position += binary_probability(KEYBOARD_MOVEMENT_SIZE, COMPUTER_COMPETENCY)
			elif paddle.centery > ball.centery+KEYBOARD_MOVEMENT_SIZE:
				paddle_y_position -= binary_probability(KEYBOARD_MOVEMENT_SIZE, COMPUTER_COMPETENCY)
	return paddle_y_position

def display_score(player_one_score, player_two_score):
	# player one results
	player_one_result_surf = BASIC_FONT.render('Score = %s' %(player_one_score), True, WHITE)
	player_one_result_rect = player_one_result_surf.get_rect()
	player_one_result_rect.topleft = (100, 25)
	DISPLAY_SURF.blit(player_one_result_surf, player_one_result_rect)
	# player two results
	player_two_result_surf = BASIC_FONT.render('Score = %s' %(player_two_score), True, WHITE)
	player_two_result_rect = player_two_result_surf.get_rect()
	player_two_result_rect.topleft = (WINDOW_WIDTH - 200, 25)
	DISPLAY_SURF.blit(player_two_result_surf, player_two_result_rect)

# return the principal value with probability, 0 if not
def binary_probability(principal, probability):
	# return 
	if np.random.rand() < probability :
		return principal
	else:
		return 0


# pong gameplay implementation
class Gameplay:
	def __init__(self, player_one, player_two, title_text, pygame_event, is_challenge_gameplay, trained_steps=None):
		# initialize pygame
		pygame.init()

		# global variables for surface and clock
		global DISPLAY_SURF
		FPS_CLCOK = pygame.time.Clock()
		DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT));

		# score font
		global BASIC_FONT, BASIC_FONT_SIZE
		BASIC_FONT_SIZE = 20
		BASIC_FONT = pygame.font.Font('freesansbold.ttf', BASIC_FONT_SIZE)

		# set display to 'Pong DQN'
		pygame.display.set_caption(title_text)

		# initalize players and pygame_event and type of gameplay
		self.player_one = player_one
		self.player_two = player_two
		self.pygame_event = pygame_event
		self.is_challenge_gameplay = is_challenge_gameplay
		if trained_steps != None:
			self.trained_steps = trained_steps

		# initialize paddle positions
		self.initial_player_one_position = (WINDOW_HEIGHT / 2) - (PADDLE_SIZE / 2)
		self.initial_player_two_position = (WINDOW_HEIGHT / 2) - (PADDLE_SIZE / 2)
		self.paddle_one = pygame.Rect(PADDLE_OFFSET, self.initial_player_one_position, LINE_THICKNESS, PADDLE_SIZE)
		self.paddle_two = pygame.Rect(WINDOW_WIDTH - PADDLE_OFFSET - LINE_THICKNESS, self.initial_player_two_position, LINE_THICKNESS, PADDLE_SIZE)

		# initialize ball position
		self.ball, self.ball_direction_x, self.ball_direction_y = reset_ball()

		# initialize scores
		self.player_one_score = 0
		self.player_two_score = 0
		self.player_one_challenge_score = 0
		self.player_two_challenge_score = 0

	# initialize the gameplay frame
	def get_initial_frame(self, display_on):
		# draw the starting positions of the arena
		draw_arena()
		draw_paddle(self.paddle_one)
		draw_paddle(self.paddle_two)
		draw_ball(self.ball)
		if display_on == 1:
			pygame.display.update()
		# get pixel data of the game surface
		surface_data = pygame.surfarray.array3d(pygame.display.get_surface())
		return surface_data

	# update to the next frame
	def get_next_frame(self, player_one_action, player_two_action, display_on):
		
		player_one_reward = 0
		player_two_reward = 0

		player_one_challenge_reward = 0
		player_two_challenge_reward = 0

		# exit game if quit
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.display.quit()
				self.pygame_event.in_play = False
				tf.reset_default_graph()

		# update paddle for human player(s)
			if event.type == KEYDOWN:
				if self.player_one == 0 and event.key == pygame.K_w:
					self.paddle_one.y -= KEYBOARD_MOVEMENT_SIZE
				elif self.player_one == 0 and event.key == pygame.K_s:
					self.paddle_one.y += KEYBOARD_MOVEMENT_SIZE
				if self.player_two == 0 and event.key == pygame.K_UP:
					self.paddle_two.y -= KEYBOARD_MOVEMENT_SIZE
				elif self.player_two == 0 and event.key == pygame.K_DOWN:
					self.paddle_two.y += KEYBOARD_MOVEMENT_SIZE

		# update paddle for computer player(s)
		if self.player_one == 1:
			self.paddle_one.y = move_computer_paddle(self.ball, self.ball_direction_x, self.paddle_one, 1)
		if self.player_two == 1:
			self.paddle_two.y = move_computer_paddle(self.ball, self.ball_direction_x, self.paddle_two, 2)

		# update paddle for dqn player(s)
		if self.player_one == 2:
			if player_one_action[1] == 1:
				self.paddle_one.y -= KEYBOARD_MOVEMENT_SIZE
			if player_one_action[2] == 1:
				self.paddle_one.y += KEYBOARD_MOVEMENT_SIZE
		if self.player_two == 2:
			if player_two_action[1] == 1:
				self.paddle_two.y -= KEYBOARD_MOVEMENT_SIZE
			if player_two_action[2] == 1:
				self.paddle_two.y += KEYBOARD_MOVEMENT_SIZE

		# update the ball 
		self.ball = move_ball(self.ball, self.ball_direction_x, self.ball_direction_y)
		self.ball_direction_x, self.ball_direction_y, self.done = check_edge_collision(self.ball, self.ball_direction_x, self.ball_direction_y)

		# based on collision, change direction of the ball or reset after changing score
		if self.done == 0:
			direction_constant_x, direction_constant_y, player_one_reward, player_two_reward = check_paddle_collision(self.ball, self.ball_direction_x, self.ball_direction_y, self.paddle_one, self.paddle_two, player_one_reward, player_two_reward)
			self.ball_direction_x = self.ball_direction_x * direction_constant_x
			self.ball_direction_y = self.ball_direction_y * direction_constant_y
		elif self.done == 1:
			self.ball, ball_direction_x, self.ball_direction_y = reset_ball()
			player_two_reward += TERMINAL_REWARD
			player_one_reward -= TERMINAL_REWARD
			player_two_challenge_reward += 1
		elif self.done == 2:
			self.ball, ball_direction_x, self.ball_direction_y = reset_ball()
			player_one_reward += TERMINAL_REWARD
			player_two_reward -= TERMINAL_REWARD
			player_one_challenge_reward += 1

		# update scores
		self.player_one_score += player_one_reward
		self.player_two_score += player_two_reward
		self.player_one_challenge_score += player_one_challenge_reward
		self.player_two_challenge_score += player_two_challenge_reward
		
		if (not self.is_challenge_gameplay) and ((player_one_reward != 0) or (player_two_reward !=0)):
			self.pygame_event.update_score(self.player_one_score, self.player_two_score)
		
		if (self.is_challenge_gameplay) and ((player_one_challenge_reward != 0) or (player_two_challenge_reward !=0)):
			self.pygame_event.update_challenge_score(self.player_one_challenge_score, self.player_two_challenge_score)
			
			# if dqn agent scores 3 points, quit game
			if self.player_one_challenge_score >= 3:
				pygame.display.quit()
				self.pygame_event.in_play = False
				tf.reset_default_graph()
			
			# if human player scores 3 points, move onto the next level unless at last level
			if self.player_two_challenge_score >= 3:
				if self.trained_steps == "fourteen_million":
					pygame.display.quit()
					self.pygame_event.in_play = False
					tf.reset_default_graph()
				else:
					tf.reset_default_graph()
					self.pygame_event.next_level(self.trained_steps)


		# draw all components
		draw_arena()
		draw_paddle(self.paddle_one)
		draw_paddle(self.paddle_two)
		draw_ball(self.ball)
		if display_on == 1:
			pygame.display.update()

		# get pixel data of the game surface
		surface_data = pygame.surfarray.array3d(pygame.display.get_surface())
		return [player_one_reward, player_two_reward, surface_data]