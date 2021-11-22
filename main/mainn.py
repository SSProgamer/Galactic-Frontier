import pygame

class Enemy():
	def main(num):
		enemyImg = (pygame.image.load('main/Assets/enemy_normal.png'))
		enemyX = (-100)-num*75
		enemyY = 240
		enemyX_change,enemyY_change = 1,1
		enemy_health,enemy_state = (100),(False)
		return enemyX,enemyY,enemyX_change,enemyY_change,enemy_health,enemy_state,enemyImg
