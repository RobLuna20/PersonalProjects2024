import pygame
from sys import exit #closes everything once we call it
from random import randint

class Player(pygame.sprite.Sprite):
    def __int__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/player/player_walk_1.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (200,300))

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time #gets the time since the pygame started
    score_surf = test_font.render(F"Score: {current_time}", False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:screen.blit(snail_surf,obstacle_rect)
            else: screen.blit(fly_surf, obstacle_rect)


        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        #jump
        player_surf = player_jump
    else:
        #walk
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]





pygame.init() #starts pygame needed for the game.
screen = pygame.display.set_mode((800,400)) #width, height
pygame.display.set_caption("Bobby The Snail Runner") #title for window
clock = pygame.time.Clock()
test_font = pygame.font.Font("C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/font/Pixeltype.ttf", 50) #font type and font size

game_active = False
start_time = 0
score = 0

player = pygame.sprite.GroupSingle()
player.add(Player())

sky_surface = pygame.image.load('C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/Sky.png').convert()
ground_surface = pygame.image.load('C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/ground.png').convert()
# score_surf = test_font.render("Bobby The Snail Runner", False, (64,64,64) ) #text, Anti A, color
# score_rect = score_surf.get_rect(center =(400,50))

# obstaculos
#snail
snail_frame_1 = pygame.image.load('C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

#fly
fly_frame1 = pygame.image.load('C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/Fly/Fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/Fly/Fly1.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk_1 = pygame.image.load('C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load("C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/player/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load("C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/player/jump.png").convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300)) #player movement, creating the rectangle
# test_surface = pygame.Surface((100, 200)) #origin is at top left
# test_surface.fill('Red')
player_gravity = 0
#intro screen
player_stand = pygame.image.load("C:/Users/Rober/Downloads/UltimatePygameIntro-main/UltimatePygameIntro-main/graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.scale2x(player_stand) #only one argument with 2x
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render("Bobby The Snail Runner", False, (111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render("Press space to run", False, (111,196,169))
game_message_rect = game_message.get_rect(center=(400,320))

#Timer
obstacle_timer = pygame.USEREVENT + 1 #avoid conflict by using +1
pygame.time.set_timer(obstacle_timer, 1500) #time of the nails spawning randomly

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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

                start_time = int(pygame.time.get_ticks() / 1000)
        if game_active:
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),210)))
            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

    if game_active:
        screen.blit(sky_surface,(0,0)) #position on the display surface
        screen.blit(ground_surface, (0, 300)) #top of the ground (green area)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(score_surf,score_rect)
        score = display_score()

        # snail_rect.x -= 4
        # if snail_rect.right <= 0:
        #     snail_rect.left = 800 #relocates snail (looks as a loop)
        # screen.blit(snail_surf, snail_rect)
        #player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300 #keep the player on the ground as a limit
            player_animation()
        screen.blit(player_surf,player_rect)

        #enemy movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list) #overwrite list

        #collision
        game_active = collisions(player_rect, obstacle_rect_list)

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0

        score_message = test_font.render(F"Your score: {score}", False, (111,196,169))
        score_message_rect = score_message.get_rect(center = (400,300))
        screen.blit(game_name,game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
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

