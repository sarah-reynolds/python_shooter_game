import pygame

class Settings():
	def __init__(self):
		self.screen_size = (1000,800)
		self.bg_color = (82,111,53)
		self.hero_speed = 1
		self.game_active = False
		self.bullet_width = 3
		self.bullet_height = 10
		self.bullet_color = (0,0,0)
		self.bullet_speed = 20
		self.image = pygame.image.load('bg.jpg')
		self.bg_rect = self.image.get_rect()
		self.timer = 0
		self.enemy_count = 0