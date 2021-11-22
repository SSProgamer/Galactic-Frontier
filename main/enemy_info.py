import pygame

class Enemy():
	def main(num, enemy_type):
		if enemy_type == 1:
			enemyImg = (pygame.image.load('main/Assets/enemy_normal.png'))
			enemyX = (-100)-num*75
			enemyY = 240
			enemyX_change,enemyY_change = 2,2
			enemy_health,enemy_state = (150),(False)
		elif enemy_type == 2:
			enemyImg = (pygame.image.load('main/Assets/enemy_fast.png'))
			enemyX = (-100)-num*75
			enemyY = 240
			enemyX_change,enemyY_change = 3,3
			enemy_health,enemy_state = (100),(False)
		elif enemy_type == 3:
			enemyImg = (pygame.image.load('main/Assets/enemy_heavy.png'))
			enemyX = (-100)-num*75
			enemyY = 240
			enemyX_change,enemyY_change = 1,1
			enemy_health,enemy_state = (300),(False)
		return enemyX,enemyY,enemyX_change,enemyY_change,enemy_health,enemy_state,enemyImg
