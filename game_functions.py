import pygame
import sys

def check_events(hero, start_button, game_settings):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			if start_button.rect.collidepoint(mouse_x, mouse_y):
				game_settings.game_active = True
				# bg_music = pygame.mixer.ound('faf.wav')
				# bg_music.play()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				# print "pressed right"
				hero.moving_right = True
			elif event.key == pygame.K_LEFT:
				# print "pressed left"
				hero.moving_left = True
			elif event.key == pygame.K_UP:
				# print "pressed up"
				hero.moving_up = True
			elif event.key == pygame.K_DOWN:
				# print "pressed down"
				hero.moving_down = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				# print "pressed right"
				hero.moving_right = False
			elif event.key == pygame.K_LEFT:
				# print "pressed left"
				hero.moving_left = False
			elif event.key == pygame.K_UP:
				# print "pressed up"
				hero.moving_up = False
			elif event.key == pygame.K_DOWN:
				# print "pressed down"
				hero.moving_down = False