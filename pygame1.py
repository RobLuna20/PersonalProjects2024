import pygame
from sys import exit #closes everything once we call it

def display_score():
    current_time = pygame.time.get_ticks() #gets the time since the pygame started
    score_surf = test_font.render(str(current_time), False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)


pygame.init() #starts pygame needed for the game.
screen = pygame.display.set_mode((800,400)) #width, height
pygame.display.set_caption("Bobby The Snail Runner") #title for window
clock = pygame.time.Clock()
test_font = pygame.font.Font("C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/font/Pixeltype.ttf", 50) #font type and font size

game_active = True

sky_surface = pygame.image.load('C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/Sky.png').convert()
ground_surface = pygame.image.load('C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/ground.png').convert()
# score_surf = test_font.render("Bobby The Snail Runner", False, (64,64,64) ) #text, Anti A, color
# score_rect = score_surf.get_rect(center =(400,50))

snail_surf = pygame.image.load('C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300)) #player movement, creating the rectangle
# test_surface = pygame.Surface((100, 200)) #origin is at top left
# test_surface.fill('Red')
player_gravity = 0

while True:
    for event in pygame.event.get(): #this method gets all the events so as the for loop
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20

            #keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300: #only one jump, avoids flying
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800 #resets position of snail

    if game_active:
        screen.blit(sky_surface,(0,0)) #position on the display surface
        screen.blit(ground_surface, (0, 300)) #top of the ground (green area)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(score_surf,score_rect)
        display_score()

        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800 #relocates snail (looks as a loop)
        screen.blit(snail_surf, snail_rect)
        #player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300 #keep the player on the ground as a limit
        screen.blit(player_surf,player_rect)

        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill("red")
        #keyboard input
        # keys = pygame.key.get_pressed()
        # keys[pygame.K_SPACE]:

        # if player_rect.colliderect(snail_rect): #checks if there is a collision between rectangles.
        #     print("collision")

        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #    print(pygame.mouse.get_pressed())
    pygame.display.update()
    clock.tick(60) #should not run faster than 60 fps

