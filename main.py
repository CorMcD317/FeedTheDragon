import random
import pygame

# Set display surface
pygame.init()

# Set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed The Dragon")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
'''constant for player lives starting at 5'''
Starting_Lives = 5
'''constant for velocity starting at 10'''
Starting_Velocity = 10
'''constant for coin velocity starting at 10'''
Starting_Coin_Velocity = 10
'''constant for coin acceleration of 0.5'''
Starting_Coin_Acceleration = 0.5
'''constant for tracking score start at 0'''
score = 0
Buffer_Distance = 100

'''constant player lives set it = to the constant above'''
Lives = Starting_Lives
'''constant coin velocity  set it = to the constant above'''
CoinVelocity = Starting_Coin_Velocity


# Set colors
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set fonts
font = pygame.font.Font('AttackGraffiti.ttf', 32)

# Set text
# Score Text
score_text = font.render("Score:" + str(score), True, GREEN, DARK_GREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

# Title Text
''' same deal as score'''
title_text = font.render("Feed_The_Dragon", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH / 2
title_rect.y = 10

# Lives Text
lives_text = font.render("Lives:" + str(Lives), True, GREEN, DARK_GREEN)
Lives_rect = lives_text.get_rect()
Lives_rect.topright = (WINDOW_WIDTH - 10, 10)

# You Suck Text
game_over_text = font.render("You Suck", True, GREEN, DARK_GREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Continue Text

continue_text = font.render("Press any Key to play again:", True, GREEN, DARK_GREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 32)

#Set sound & music
coin_sound = pygame.mixer.Sound("coin_sound.wav")

miss_sound = pygame.mixer.Sound("miss_sound.wav")

pygame.mixer.music.load("ftd_background_music.wav")


#Images
player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT // 2

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.centerx = WINDOW_WIDTH + Buffer_Distance
coin_rect.centery = random.randint(64, WINDOW_HEIGHT - 32)

pygame.mixer.music.play(-1, 0.0)



# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # UPDATE HUD
    score_text = font.render("Score:" + str(score), True, GREEN, DARK_GREEN)
    lives_text = font.render("Lives:" + str(Lives), True, GREEN, DARK_GREEN)

    # Fill the Display
    display_surface.fill(BLACK)

    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, Lives_rect)
    display_surface.blit(player_image, player_rect)
    display_surface.blit(coin_image, coin_rect)




    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
