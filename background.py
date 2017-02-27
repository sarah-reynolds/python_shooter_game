import pygame

class Background():

	def draw_bg(self,screen, game_settings):
		screen.blit(game_settings.image, game_settings.bg_rect)