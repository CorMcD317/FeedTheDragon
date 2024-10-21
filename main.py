import random
import pygame

# Set display surface
pygame.init()

# Set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch The Clown")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values, Constants
Starting_Lives = 5
Clown_Velocity = 10
Starting_Clown_Velocity = 10
Clown_Acceleration = 0.5
score = 0
Buffer_Distance = 100
clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

'''constant player lives set it = to the constant above'''
Lives = Starting_Lives
'''constant coin velocity  set it = to the constant above'''
CoinVelocity = Starting_Clown_Velocity
PlayerSpeed = Clown_Velocity

# Set colors
BLUE = (1, 175, 209)
YELLOW = (248, 231, 28)
BLACK = (0, 0, 0)

# Set fonts
font = pygame.font.Font('Assets/Franxurter.ttf', 32)


# Set text
# Score Text
score_text = font.render("Score:" + str(score), True, BLUE, YELLOW)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

# Title Text
''' same deal as score'''
title_text = font.render("Catch The Clown", True, BLUE, YELLOW)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH / 2
title_rect.y = 10

# Lives Text
lives_text = font.render("Lives:" + str(Lives), True, BLUE, YELLOW)
Lives_rect = lives_text.get_rect()
Lives_rect.topright = (WINDOW_WIDTH - 10, 10)

# You Suck Text
game_over_text = font.render("You Suck. Do Better.", True, BLUE, YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 10)

# Continue Text
continue_text = font.render("Would You Like To Try Again?", True, BLUE, YELLOW)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 32)

#Set sound & music
click_sound = pygame.mixer.Sound("Assets/click_sound.wav")

miss_sound = pygame.mixer.Sound("Assets/miss_sound.wav")

pygame.mixer.music.load("Assets/ctc_background_music.wav")


#Images
Clown_image = pygame.image.load("Assets/clown.png")
Clown_rect = Clown_image.get_rect()
Clown_rect.center = (WINDOW_HEIGHT // 2, WINDOW_WIDTH // 2)


background_image = pygame.image.load("Assets/background.png")
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

pygame.mixer.music.play(-1, 0.0)


# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

        if Clown_rect.collidepoint(mouse_x, mouse_y):
            click_sound.play()
            score += 1
            Clown_Velocity += Clown_Acceleration

            previous_dx = clown_dx
            previous_dy = clown_dy
            while (previous_dx == clown_dx and previous_dy == clown_dy):








    score_text = font.render("Score:" + str(score), True, YELLOW)
    lives_text = font.render("Lives:" + str(Lives), True, YELLOW)

    #Game Over Check
    if Lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_text_rect)
        pygame.display.update()

        #pause game till reset
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #play again

                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False


    # Fill the Display
    display_surface.blit(background_image, background_rect)

    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, Lives_rect)
    display_surface.blit(Clown_image, Clown_rect)
    pygame.draw.line(display_surface, BLACK, (0, 64), (WINDOW_WIDTH, 64), 2)



    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
