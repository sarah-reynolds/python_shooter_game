import pygame
from settings import Settings
from hero import Hero
from game_functions import check_events
from game_functions import update_screen
from pygame.sprite import Group, groupcollide
from enemy import Enemy
from button import Start_Button
from bullet import Bullet

import time

pygame.init()
pygame.display.set_caption("Attack of the Ice King")
game_settings = Settings()
screen = pygame.display.set_mode(game_settings.screen_size)



hero_group = Group()
hero = Hero(screen, game_settings)
hero_group.add(hero)

bullets = Group()

game_start_time = time.time()
print game_start_time

enemies = Group()

start_button = Start_Button(screen)

tick = 0

while 1:
	tick += 1
	if tick % 50 == 0:
		game_settings.enemy_count += 1
		enemies.add(Enemy(screen, game_settings))

	check_events(screen, hero, start_button, game_settings, bullets,enemies)
	update_screen(screen,hero,hero_group,enemies,game_settings,start_button,bullets)
