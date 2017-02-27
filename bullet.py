import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,screen,hero, game_settings, direction, bullet_type):
		super(Bullet,self).__init__()
		self.screen = screen
		self.image = pygame.image.load('bullet.png')
		if bullet_type == "vertical":
			self.rect = pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height)
		elif bullet_type == "horizontal":
			self.rect = pygame.Rect(0,0,game_settings.bullet_height,game_settings.bullet_width)
		self.rect.centerx = hero.rect.centerx
		self.rect.top = hero.rect.top
		self.color = game_settings.bullet_color
		self.x = self.rect.x
		self.y = self.rect.y
		self.direction = direction
		self.speed = game_settings.bullet_speed

	def draw_bullet(self):
		# pygame.draw.rect(self.screen,self.color,self.rect)
		self.screen.blit(source = self.image, dest = self.rect)		

	def update(self):
		if self.direction == 'up':
			self.y -= self.speed
			self.image = pygame.image.load('bullet.png')
		elif self.direction == 'down':
			self.y += self.speed
			self.image = pygame.image.load('bullet.png')
		elif self.direction == 'left':
			self.x -= self.speed
			self.image = pygame.image.load('bullet2.png')
		elif self.direction == 'right':
			self.x += self.speed
			self.image = pygame.image.load('bullet2.png')

		self.rect.y = self.y
		self.rect.x = self.x