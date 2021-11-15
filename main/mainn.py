import pygame

class Enemy():
	def main(num):
		enemyX = (-100)-num*75
		enemyY = 240
		enemyX_change,enemyY_change = 1,1
		enemy_health,enemy_state = (4),(False)
		return enemyX,enemyY,enemyX_change,enemyY_change,enemy_health,enemy_state
