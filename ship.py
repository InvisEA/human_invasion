#!/usr/bin/env python3

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""Class for controlling the ship."""
	def __init__(self, hi_game):
		super().__init__()
		self.screen = hi_game.screen
		self.settings = hi_game.settings
		self.screen_rect = hi_game.screen.get_rect()

		# Loads image of the ship and gets rectangle.
		self.image = pygame.image.load('images/spaceship.png').convert_alpha()
		
		# rescale the image of the ship
		w = self.image.get_width()
		h = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (w * 0.15, h * 0.15))
		self.rect = self.image.get_rect()

		# New spaceship appears on the bottom border of the screen.
		self.rect.midbottom = self.screen_rect.midbottom

		# Saving float coordinate of the center of the ship.
		self.x = float(self.rect.x)

		# flag that tracks moving
		self.moving_right = False
		self.moving_left = False


	def blitme(self):
		"""Paints ship in the current position."""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""Updates the position of the ship with respect to certain flag."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		self.rect.x = self.x


	def center_ship(self):
		"""Places the ship to the bottom center of the screen."""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
