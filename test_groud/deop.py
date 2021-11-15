import pygame 
import puy

# Intialize the pygame
pygame.init()
# create screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Demo')
background = pygame.image.load("test_groud/main_game.png")
rushia = pygame.image.load("test_groud/tenor.gif")
background_1_rect = rushia.get_rect(center = (400,300))
start_img = pygame.image.load('test_groud/start_btn.png').convert_alpha()
exit_img = pygame.image.load('test_groud/exit_btn.png').convert_alpha()

#create button instances
start_button = puy.Button(325, 300, start_img, 0.6)
exit_button = puy.Button(330, 425, exit_img, 0.55)
#game loop
def rotate(rushia, angle):
	rotated_surface = pygame.transform.rotozoom(rushia, angle, 1)
	rotated_rect = rotated_surface.get_rect(center = (400,300))
	return rotated_surface, rotated_rect
run = True
running = False
angle = 1
while run:
	
	screen.fill((0, 0, 0))
	screen.blit(background, (0, 0))
	if start_button.draw(screen):
		running = True
		while running:
			for event in pygame.event.get():
			#quit game
				
				if event.type == pygame.QUIT:
					run = False
					running = False
			screen.fill((0, 0, 52))
			rushia_rotated, rushia_rect = rotate(rushia, angle)
			screen.blit(rushia_rotated, rushia_rect)
			if exit_button.draw(screen):
					angle += 1
			
			pygame.display.update()
	if exit_button.draw(screen):
		run = False

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()
pygame.quit()
