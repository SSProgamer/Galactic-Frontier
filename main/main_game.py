import pygame
import random
from pygame import display
import enemy_info
import btn

# Intialize The Pygame
pygame.init()

# Create The Screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('stage/stage01_2.png')
background_menu = pygame.image.load("game_cover/main_game.png")
help_menu = pygame.image.load("game_cover/help_menu.png")
# Title
pygame.display.set_caption("Galactic Frontier")
# button
start_img = pygame.image.load('button/start_b.png').convert_alpha()
exit_img = pygame.image.load('button/button_e.png').convert_alpha()
return_img = pygame.image.load('button/button.png').convert_alpha()
help_img = pygame.image.load("button/button_help.png").convert_alpha()
back_img = pygame.image.load("button/button_back.png").convert_alpha()
# create button instances
start_button = btn.Button(325, 280, start_img, 0.6)
exit_button = btn.Button(325, 465, exit_img, 0.6)
help_button = btn.Button(325, 370, help_img, 0.6)
back_button = btn.Button(325, 465, back_img, 0.6)
# Icon
icon = pygame.image.load('main/Assets/icon.png')
pygame.display.set_icon(icon)

# music
bgm_vol = 0.1
sfx_vol = 0.1
pygame.mixer.music.load('main/Assets/Sound/markart.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(bgm_vol)

hit = pygame.mixer.Sound('main/Assets/Sound/360917__projectsu012__shoot1.wav')
enemy_ded = pygame.mixer.Sound(
    'main/Assets/Sound/334266__projectsu012__short-explosion-1.wav')


# Game Assets
game_over = pygame.image.load('main/Assets/GAMEOVER.png')
congrats = pygame.image.load('main/Assets/WINNER.png')
delete = pygame.image.load('main/Assets/delete.png')
delete_turret = False
ban_location = [[10, 240], [70, 240], [130, 240], [130, 300], [130, 360], [190, 360],
                [250, 360], [310, 360], [370, 360], [430, 360], [
                    490, 360], [550, 360], [550, 300], [550, 240],
                [610, 240], [670, 240], [730, 240]]
base_hp = 5

# Turret
turret_1 = pygame.image.load('main/Assets/turret_01_8.png')
turret_2 = pygame.image.load('main/Assets/turret_02_8.png')
turret_3 = pygame.image.load('main/Assets/turret_03_8.png')
turret_fire_1 = pygame.image.load('main/Assets/turret_01_8_fire.png')
turret_fire_2 = pygame.image.load('main/Assets/turret_02_8_fire.png')
turret_fire_3 = pygame.image.load('main/Assets/turret_03_8_fire.png')
fire = [turret_fire_1, turret_fire_2, turret_fire_3]
all_turretImg = []
all_turretlo = []
all_turretCool = []
all_turret_type = []
all_turret_rect = []
turret_fire = []
laser_cool = []
type_range = [200, 100, 400]  # range of turrets
type_cool_down = [50, 50, 100]
type_damage = [25, 35, 50]
num_of_turret = 0
turret_state = False
turret_sec_lo = pygame.image.load('main/Assets/test.png')
turret_sec_lo_cannot = pygame.image.load('main/Assets/cannot.png')
slot_1 = pygame.image.load('main/Assets/sign_until01.png')
slot_2 = pygame.image.load('main/Assets/sign_until02.png')
slot_3 = pygame.image.load('main/Assets/sign_until03.png')
turret_amount = [0, 0, 0]

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_health = []
enemy_state = []
num_of_enemies = 0
check_enemy_move = False
angle = 0
wave = 0

font = pygame.font.Font("main/fort/Minecraft.ttf", 30)


def show_font():
    show_wave = font.render("WAVE : %d" % wave, True, (255, 255, 255))
    show_enemy = font.render("ENEMY : %d" %
                             num_of_enemies, True, (255, 255, 255))
    show_hp = font.render("HP : %d" % base_hp, True, (255, 255, 255))
    show_turret_1 = font.render("%d" % turret_amount[0], True, (255, 255, 255))
    show_turret_2 = font.render("%d" % turret_amount[1], True, (255, 255, 255))
    show_turret_3 = font.render("%d" % turret_amount[2], True, (255, 255, 255))
    screen.blit(show_wave, (10, 10))  # กำหนดตำแหน่ง
    screen.blit(show_enemy, (335, 10))
    screen.blit(show_hp, (700, 10))
    screen.blit(show_turret_1, (215, 557))
    screen.blit(show_turret_2, (435, 557))
    screen.blit(show_turret_3, (660, 558))


def fort_help():
    """fort ช่วยเล่น"""
    help_wave = font.render(
        "Press space bar to start wave", True, (255, 255, 255))
    help_deselect = font.render(
        "Press right mouse button to deselect", True, (255, 255, 255))
    help_turret_1 = font.render(
        "Press 1 to select yellow turret", True, (255, 255, 255))
    help_turret_2 = font.render(
        "Press 2 to select purple turret", True, (255, 255, 255))
    help_turret_3 = font.render(
        "Press 3 to select red turret", True, (255, 255, 255))
    help_turret_4 = font.render(
        "Press 4 to select delete turret", True, (255, 255, 255))
    help_quit = font.render("Press Esc to quit game", True, (255, 255, 255))
    screen.blit(help_wave, (100, 50))
    screen.blit(help_deselect, (100, 100))
    screen.blit(help_turret_1, (100, 150))
    screen.blit(help_turret_2, (100, 200))
    screen.blit(help_turret_3, (100, 250))
    screen.blit(help_turret_4, (100, 300))
    screen.blit(help_quit, (100, 350))


def enemy_born():
    random_enemy = []
    for i in range(num_of_enemies):
        random_enemy.append(random.randrange(1, 4))
    random_enemy.sort()
    for i in range(num_of_enemies):
        ans = (enemy_info.Enemy)
        ans = ans.main(i, random_enemy[i])
        enemyImg.append(ans[6])
        enemyX.append(ans[0])
        enemyY.append(ans[1])
        enemyX_change.append(ans[2])
        enemyY_change.append(ans[3])
        enemy_health.append(ans[4])
        enemy_state.append(ans[5])


def player(select, x, y, radius):
    pygame.draw.circle(screen, (255, 255, 255), (x+30, y+30), radius, 5)
    screen.blit(select, (x, y))


def all_turret(i, turret_rect):
    screen.blit(all_turretImg[i], turret_rect)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def select_delete(image, x, y):
    screen.blit(image, (x, y))


def add_turret(percent):
    global turret_amount
    if percent <= 49:
        turret_amount[0] += 1
    elif percent <= 79:
        turret_amount[1] += 1
    else:
        turret_amount[2] += 1


def help_me():
    """help to play"""
    background_help = True
    while background_help:
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.blit(help_menu, (0, 0))
        fort_help()
        if exit_button.draw(screen):
            background_help = False
        display.update()


# Main Game
running = False
background_menu_start = True
background_help = False
background_menu_go = True
while background_menu_start:
    screen.fill((0, 0, 0))
    screen.blit(background_menu, (0, 0))
    if start_button.draw(screen):
        running = True
        while running:

            # Add Background
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            screen.blit(slot_1, (100, 540))
            screen.blit(slot_2, (320, 540))
            screen.blit(slot_3, (540, 540))
            screen.blit(delete, (755, 555))

            # Get Mouse Location
            mouse_location = pygame.mouse.get_pos()
            fix_mouse_lo = [(mouse_location[0]//60)*(60)+10,
                            (mouse_location[1]//60)*(60)]

            # Player Interact
            for event in pygame.event.get():

                # Quit Game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    background_menu_start = False

                # Mouse Event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    # Select Turret
                    if mouse_press[0] and check_enemy_move == False and turret_state == False and base_hp > 0 and wave != 6:
                        # Select Turret 1
                        if mouse_location[0] >= 100 and mouse_location[0] <= 260 and \
                                mouse_location[1] >= 540 and mouse_location[1] <= 600 and turret_amount[0] > 0:
                            select = turret_1
                            turret_type = 0
                            pygame.mouse.set_visible(False)
                            turret_state = True
                            delete_turret = False
                        # Select Turret 2
                        elif mouse_location[0] >= 320 and mouse_location[0] <= 480 and \
                                mouse_location[1] >= 540 and mouse_location[1] <= 600 and turret_amount[1] > 0:
                            select = turret_2
                            turret_type = 1
                            pygame.mouse.set_visible(False)
                            turret_state = True
                            delete_turret = False
                        # Select Turret 3
                        elif mouse_location[0] >= 540 and mouse_location[0] <= 700 and \
                                mouse_location[1] >= 540 and mouse_location[1] <= 600 and turret_amount[2] > 0:
                            select = turret_3
                            turret_type = 2
                            pygame.mouse.set_visible(False)
                            turret_state = True
                            delete_turret = False
                    # Add Turret
                    elif mouse_press[0] and turret_state and \
                            mouse_location[0] < 780 and mouse_location[1] < 540 \
                            and fix_mouse_lo not in all_turretlo and check_enemy_move == False \
                    and fix_mouse_lo not in ban_location:
                        pygame.mouse.set_visible(True)
                        turret_state = False
                        all_turretImg.append(select)
                        all_turretlo.append(fix_mouse_lo)
                        all_turretCool.append(0)
                        all_turret_type.append(turret_type)
                        turret_fire.append(fire[turret_type])
                        laser_cool.append(0)
                        num_of_turret += 1
                        turret_amount[turret_type] -= 1
                    # Select Delete
                    if mouse_press[0] and mouse_location[0] >= 755 and \
                        mouse_location[0] <= 785 and mouse_location[1] >= 555 and \
                            mouse_location[1] <= 585 and check_enemy_move == False and base_hp > 0 and wave != 6:
                        pygame.mouse.set_visible(False)
                        turret_state = False
                        delete_turret = True
                    # Delete Turret
                    elif mouse_press[0] and delete_turret:
                        if fix_mouse_lo in all_turretlo:
                            remove_index = all_turretlo.index(fix_mouse_lo)
                            turret_amount[all_turret_type[remove_index]] += 1
                            all_turretImg.pop(remove_index)
                            all_turretlo.pop(remove_index)
                            all_turretCool.pop(remove_index)
                            all_turret_type.pop(remove_index)
                            turret_fire.pop(remove_index)
                            laser_cool.pop(remove_index)
                            num_of_turret -= 1
                    # Deselect
                    if mouse_press[2]:
                        pygame.mouse.set_visible(True)
                        turret_state = False
                        delete_turret = False

                # Key Event
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        background_menu_start = False
                        pygame.quit()
                    if event.key == pygame.K_SPACE and base_hp > 0:
                        check_enemy_move = True
                        pygame.mouse.set_visible(True)
                    if event.key == pygame.K_1 and check_enemy_move == False and base_hp > 0 and turret_amount[0] > 0 and wave != 6:
                        select = turret_1
                        turret_type = 0
                        pygame.mouse.set_visible(False)
                        turret_state = True
                        delete_turret = False
                    if event.key == pygame.K_2 and check_enemy_move == False and base_hp > 0 and turret_amount[1] > 0 and wave != 6:
                        select = turret_2
                        turret_type = 1
                        pygame.mouse.set_visible(False)
                        turret_state = True
                        delete_turret = False
                    if event.key == pygame.K_3 and check_enemy_move == False and base_hp > 0 and turret_amount[2] > 0 and wave != 6:
                        select = turret_3
                        turret_type = 2
                        pygame.mouse.set_visible(False)
                        turret_state = True
                        delete_turret = False
                    if event.key == pygame.K_4 and check_enemy_move == False and base_hp > 0 and wave != 6:
                        pygame.mouse.set_visible(False)
                        turret_state = False
                        delete_turret = True

            # Select Turret
            if turret_state and check_enemy_move == False:
                playerX = mouse_location[0]-30
                playerY = mouse_location[1]-30
                if mouse_location[0] < 780 and mouse_location[1] < 540:
                    if (fix_mouse_lo in ban_location) or (fix_mouse_lo in all_turretlo):
                        screen.blit(turret_sec_lo_cannot,
                                    (fix_mouse_lo[0], fix_mouse_lo[1]))
                    else:
                        screen.blit(turret_sec_lo,
                                    (fix_mouse_lo[0], fix_mouse_lo[1]))
                player(select, playerX, playerY, type_range[turret_type])

            # Remove Dead Enemy
            while True in enemy_state:
                for i in range(num_of_enemies):
                    if enemy_state[i]:
                        del enemyImg[i]
                        del enemyX[i]
                        del enemyY[i]
                        del enemyX_change[i]
                        del enemyY_change[i]
                        del enemy_health[i]
                        del enemy_state[i]
                        num_of_enemies -= 1
                        if base_hp > 0:
                            enemy_ded.set_volume(sfx_vol)
                            enemy_ded.play()
                        break

            # Turret Work
            for i in range(num_of_turret):
                # Cooldown
                if all_turretCool[i] != type_cool_down[all_turret_type[i]]:
                    all_turretCool[i] += 1
                # Do Damage
                for j in range(num_of_enemies):
                    if ((enemyX[j]+30)-(all_turretlo[i][0]+30))**2 + \
                        ((enemyY[j]+30)-(all_turretlo[i][1]+30))**2 <= type_range[all_turret_type[i]]**2 and \
                            all_turretCool[i] == type_cool_down[all_turret_type[i]] and enemyX[j] > -30:
                        enemy_health[j] -= type_damage[all_turret_type[i]]
                        all_turretCool[i] = 0
                        laser_cool[i] = 10
                all_turret(i, all_turretlo[i])
                if laser_cool[i] > 0:
                    screen.blit(turret_fire[i], all_turretlo[i])
                    if base_hp > 0:
                        hit.set_volume(sfx_vol)
                        hit.play()
                    laser_cool[i] -= 1

            # Select Delete
            if delete_turret and check_enemy_move == False:
                select_delete(
                    delete, mouse_location[0]-15, mouse_location[1]-15)

            # Enemy
            for i in range(num_of_enemies):
                # Enemy Movement
                if check_enemy_move:
                    if enemyX[i] < 130:
                        enemyX[i] += enemyX_change[i]
                    elif enemyY[i] < 360 and enemyX[i] < 549:
                        enemyY[i] += enemyY_change[i]
                    elif enemyX[i] < 550:
                        enemyX[i] += enemyX_change[i]
                    elif enemyY[i] > 240:
                        enemyY[i] -= enemyY_change[i]
                    else:
                        enemyX[i] += enemyX_change[i]
                # Enemy Health
                if enemy_health[i] <= 0 or enemyX[i] > 800:
                    if enemyX[i] > 800:
                        base_hp -= 1
                    enemy_state[i] = True
                enemy(enemyX[i], enemyY[i], i)

            if num_of_enemies == 0:
                if wave == 0:
                    for _ in range(3):
                        add_turret(random.randrange(100))
                else:
                    for _ in range(2):
                        add_turret(random.randrange(100))
                wave += 1
                num_of_enemies = 6+2*(wave-1)  # เติมที่นี้
                enemy_born()
                check_enemy_move = False
                turret_state = False
                delete_turret = False

            show_font()
            exit_button = btn.Button(325, 400, exit_img, 0.6)
            if base_hp <= 0:
                screen.blit(game_over, (0, 0))
                if exit_button.draw(screen):
                    pygame.quit()
            if wave == 6 and base_hp > 0:
                screen.blit(congrats, (0, 0))
                if exit_button.draw(screen):
                    pygame.quit()

            pygame.display.update()
    if exit_button.draw(screen):
        pygame.quit()
        background_menu_start = False
        running = False

        # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            pygame.quit()
    if help_button.draw(screen):
        help_me()
    pygame.display.update()
