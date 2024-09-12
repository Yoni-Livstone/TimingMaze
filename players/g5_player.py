import os
import pickle
import numpy as np
import logging

import constants
from timing_maze_state import TimingMazeState

class G5_Player:
	def __init__(self, rng: np.random.Generator, logger: logging.Logger,
				 precomp_dir: str, maximum_door_frequency: int, radius: int) -> None:
		"""Initialise the player with the basic amoeba information

			Args:
				rng (np.random.Generator): numpy random number generator, use this for same player behavior across run
				logger (logging.Logger): logger use this like logger.info("message")
				maximum_door_frequency (int): the maximum frequency of doors
				radius (int): the radius of the drone
				precomp_dir (str): Directory path to store/load pre-computation
		"""

		self.rng = rng
		self.logger = logger
		self.maximum_door_frequency = maximum_door_frequency
		self.radius = radius
		# 0 for explore and 1 for converge
		self.mode = 0
		self.location = (0,0)

	def move(self, current_percept) -> int:
		"""Function which retrieves the current state of the amoeba map and returns an amoeba movement

			Args:
				current_percept(TimingMazeState): contains current state information
			Returns:
				int: This function returns the next move of the user:
					WAIT = -1
					LEFT = 0
					UP = 1
					RIGHT = 2
					DOWN = 3
		"""
		
		if self.mode == 0:
			return self.explore(current_percept)
		else:
			return self.converge(current_percept)			

	def explore(self, current_percept) -> int:
		return constants.LEFT
		# explore the maze
		pass

	def converge(self, current_percept) -> int:
		return constants.RIGHT
		# converge to the end of the maze
		pass
	
class Wall:
	interval_candidates = []
	border_wall: bool = False
	
	def __init__(self, state: int):
		# either open or closed 
		# CLOSED = 1
		# OPEN = 2
		# BOUNDARY = 3
		self.state = state
		
	def calculate_interval_candidates(self):
		# calculate the interval candidates for the wall including always open and always closed
		pass

	def is_it_open(self, turns: int = 1) -> float:
	# check if the wall will be open
	# return the odds it is open 
	# 0 if it will be closed
	# 1 if it will be open
	# otherwise the likelihood it will be open based on observed data
	
	# the turns parameter is in the number of turns the wall will be open
		pass
	

class Cell:
	def __init__(self, UP: Wall, RIGHT: Wall, DOWN: Wall, LEFT: Wall, location: tuple):
		self.UPPER_WALL = UP
		self.RIGHT_WALL = RIGHT
		self.DOWN_WALL = DOWN
		self.LEFT_WALL = LEFT
		self.observed = False
		self.location = location

	def observed(self):
		self.observed = True

	def get_touching_wall(self, wall: Wall):
		# return the wall that is touching the specified cell wall
		pass
	
class Map:
	treasure_location = (-1,-1)

	def __init__(self, map_dim: int = constants.map_dim):
		self.map_dim = map_dim

		# TODO: techinically, we need to create a larger map to traverse and then when we move we need to resize the map.
		self.cells = [[Cell() for _ in range(map_dim)] for _ in range(map_dim)]
		current_location = (0,0)

		# TODO: set the border walls to always closed

	def move (self, direction: int):
		# move the player in the specified direction
		# return the new location of the player
		if direction == constants.WAIT:
			pass
		elif direction == constants.LEFT:
			self.current_location[0] -= 1
		elif direction == constants.UP:
			self.current_location[1] += 1
		elif direction == constants.RIGHT:
			self.current_location[0] += 1
		elif direction == constants.DOWN:
			self.current_location[1] -= 1

		return self.current_location
	

	def set_global_x(self, x):
		
		# Go through every cell in the maze and change the x value by the difference
		# Absolute_x - Relative_x for each x in the graph

		for row in self.cells:
			for cell in row:
				cell.location[0] = x - cell.location[0]
		
		return self.current_location
		
	def set_global_y(self, y) -> None:
		# Go through every cell in the maze and change the y value by the difference
		# Absolute_y - Relative_y for each y in the graph
		
		for row in self.cells:
			for cell in row:
				cell.location[1] = y - cell.location[1]
		
		return self.current_location
	
	def set_treasure_location(self, location: tuple) -> None:
		# set the location of the treasure
		self.treasure_location = location

	def get_cell(self, location: tuple) -> Cell:
		# return the cell at the specified location
		return self.cells[location[0]][location[1]]
	
	def resize_map(self, new_map_dim: int) -> None:
		# resize the map to the new map dimension
		pass
