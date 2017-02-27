import pygame
import sys
from bullet import Bullet
from pygame.sprite import Group, groupcollide
from background import Background

# class utility_functions(object):
# 	@staticmethod
# 	def check_events():
# 		print "static test"

def check_events(screen, hero, start_button, game_settings, bullets,enemies):
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
			if event.key == pygame.K_d:
				# print "pressed right"
				hero.moving_right = True
			elif event.key == pygame.K_a:
				# print "pressed left"
				hero.moving_left = True
			elif event.key == pygame.K_w:
				# print "pressed up"
				hero.moving_up = True
			elif event.key == pygame.K_s:
				# print "pressed down"
				hero.moving_down = True
			elif event.key == pygame.K_UP:
				new_bullet = Bullet(screen, hero, game_settings, 'up', 'vertical')
				bullets.add(new_bullet)
			elif event.key == pygame.K_RIGHT:
				new_bullet = Bullet(screen, hero, game_settings, 'right', 'horizontal')
				bullets.add(new_bullet)
			elif event.key == pygame.K_LEFT:
				new_bullet = Bullet(screen, hero, game_settings, 'left', 'horizontal')
				bullets.add(new_bullet)
			elif event.key == pygame.K_DOWN:
				new_bullet = Bullet(screen, hero, game_settings, 'down', 'vertical')
				bullets.add(new_bullet)
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_d:
				# print "pressed right"
				hero.moving_right = False
			elif event.key == pygame.K_a:
				# print "pressed left"
				hero.moving_left = False
			elif event.key == pygame.K_w:
				# print "pressed up"
				hero.moving_up = False
			elif event.key == pygame.K_s:
				# print "pressed down"
				hero.moving_down = False

def update_screen(screen,hero,hero_group,enemies,game_settings,start_button,bullets):
	background = Background()
	background.draw_bg(screen, game_settings)

	for hero in hero_group.sprites():
		if game_settings.game_active:
			hero.update_me()
		hero.draw_me()

	for bullet in bullets.sprites():
		bullet.update()
		bullet.draw_bullet()

	for enemy in enemies.sprites():
		if game_settings.game_active:
			enemy.update_me(hero)
		enemy.draw_me()

	hero_died = groupcollide(hero_group, enemies, True, True)
	if hero_died:
		print "You lost!"
		game_settings.game_active = False

	enemies_died = groupcollide(enemies, bullets, True, True)
	# enemies_died

	if game_settings.game_active == False:
		start_button.draw_button()

	pygame.display.flip()
