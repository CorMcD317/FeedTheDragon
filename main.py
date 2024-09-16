import pygame

#Set display surface
pygame.init()

#Set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed The Dragon")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()


#Set game values
'''constant for player lives starting at 5'''
Starting_Lives = 5
'''constant for velocity starting at 10'''
Starting_Velocity = 10
'''constant for coin velocity starting at 10'''
Starting_Coin_Velocity = 10
'''constant for coin acceleration of 0.5'''
Starting_Coin_Acceleration = 0.5
'''constant for tracking score start at 0'''
score = Starting_Score
'''constant player lives set it = to the constant above'''
Lives = Starting_Lives
'''constant coin velocity  set it = to the constant above'''
CoinVelocity = Starting_Coin_Velocity




#Set colors
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Set fonts
font = pygame.font.Font('AttackGraffiti.ttf', 32)

#Set text
#Score Text
score_text = font.render("Score:" + str(score), True, GREEN, DARK_GREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

#Title Text
''' same deal as score'''
title = "Feed_The_Dragon"
font.render("Title" + str(title), True, GREEN, WHITE)
title_rect = title.get_rect()
title_rect.centerx = WINDOW_WIDTH / 2
title_rect.y = 10

#Lives Text
font.render("Lives:" + str(Lives), True, GREEN, DARK_GREEN)
Lives_rect = Lives.get_rect()
topright =(WINDOW_WIDTH - 10, 10)

#You Suck Text
game_over_text =
font.render("You Suck:" + str(game_over_text), True, DARK_GREEN)
center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2),
game_over_text.rect = game_over_text.get_rect

#Continue Text
continue_text =
font.render("Press any Key to play again:" + str(continue_text), True, GREEN, DARK_GREEN)
center = (WINDOW_WIDTH // 2 , WINDOW_HEIGHT // 2 + 32)



#Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #UPDATE HUD
    score_text = font.render("Score:" + str(score), True, GREEN, DARK_GREEN)
    lives_text = font.render("Lives:" + str(Lives), True, GREEN, DARK_GREEN)

    #Fill the Display
    display_surface.fill(BLACK)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, Lives_rect)

    pygame.display.update()
pygame.quit()



