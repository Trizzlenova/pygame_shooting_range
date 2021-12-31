import pygame, sys, random

# initiating game
pygame.init()

# game screen size
screen = pygame.display.set_mode((1280, 720))

# tracking time of game (fps)
clock = pygame.time.Clock()

# removing mouse pointer from game screen
pygame.mouse.set_visible(False)

# game images
wood_bg = pygame.image.load('Wood_BG.png')
land_bg = pygame.image.load('Land_BG.png')
water_bg = pygame.image.load('Water_BG.png')
cloud_one = pygame.image.load('Cloud1.png')
cloud_two = pygame.image.load('Cloud2.png')
crosshair = pygame.image.load('crosshair.png')
duck_surface = pygame.image.load('duck.png')

# game font when player wins
game_font = pygame.font.Font(None, 60)
text_surface = game_font.render('You Won!', True, (255, 255, 255))
text_rect = text_surface.get_rect(center = (640, 360))

# setting up animated land
land_position_y = 560
land_speed = 1

# setting up animated water
water_position_y = 640
water_speed = 1.5

# default position for crosshair
crosshair_rect = crosshair.get_rect(center = (640, 360))

# setting up random positions for each duck
duck_list = []
for duck in range(20):    
    duck_position_x = random.randrange(50, 1200)
    duck_position_y = random.randrange(120, 600)
    duck_rect = duck_surface.get_rect(center = (duck_position_x, duck_position_y))
    duck_list.append(duck_rect)

# game events
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center = event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, duck_rect in enumerate(duck_list):
                if duck_rect.collidepoint(event.pos):
                    del duck_list[index]
    
    # setting wood background
    screen.blit(wood_bg, (0, 0))
    
    # duck positions
    for duck_rect in duck_list:
        screen.blit(duck_surface, duck_rect)
    
    # if duck list is empty, show text
    if len(duck_list) <= 0:
        screen.blit(text_surface, text_rect)

    # animated land
    land_position_y -= land_speed
    if land_position_y <= 520 or land_position_y >= 600:
        land_speed *= -1

    # animated water
    water_position_y += water_speed
    if water_position_y <= 600 or water_position_y >= 680:
        water_speed *= -1

    # water and land positions
    screen.blit(land_bg, (0, land_position_y))
    screen.blit(water_bg, (0, water_position_y)) 

    # crosshair position on mouse motion
    screen.blit(crosshair, crosshair_rect)

    # cloud positions
    screen.blit(cloud_one, (100, 50))
    screen.blit(cloud_one, (604, 10))
    screen.blit(cloud_one, (412, 55))
    screen.blit(cloud_two, (840, 200))
    screen.blit(cloud_two, (170, 80))
    screen.blit(cloud_two, (1000, 90))

    # updating the clock object (fps)
    pygame.display.update()
    clock.tick(120)