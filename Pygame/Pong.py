import pygame
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# -- Initialise PyGame
pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Pong")
# -- Exit game flag set to false
done = False 
ball_width = 20
x_val = 150
y_val = 200
x_direction = 3
y_direction = 3
padd_length = 15
padd_width = 60
x_padd = 0
y_padd = 20
score = 0
# -- Manages how fast screen refreshes
clock = pygame.time.Clock() 

### -- Game Loop 
while not done: 
    # -- User input and controls 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: 
        # - write logic that happens on key press here 
        y_padd = y_padd - 5 
    if keys[pygame.K_DOWN]: 
        # - write logic that happens on key press here 
        y_padd = y_padd + 5
            #End If 
        #End If 
    #Next event

    # -- Game logic goes after this comment 
    x_val = x_val + x_direction
    y_val = y_val + y_direction
    if y_val > 460:
        y_direction = y_direction*-1
    elif y_val < 0:
        y_direction = y_direction*-1
    if x_val > 620:
        x_direction = x_direction*-1
    elif x_val < -20:
        x_val = 320
        y_val = 240
        score = score + 1
    if y_padd > 420:
        y_padd = 420
    if y_padd < 0:
        y_padd = 0
    if x_val +x_direction < x_padd +15 and y_val>=y_padd and y_val <=y_padd+60 :
        x_direction = x_direction*-1  
    if score > 10:
        pygame.quit()
    #End If
    # -- Screen background is BLACK 
    screen.fill (BLACK)
    # -- Draw here 
    pygame.draw.rect(screen, BLUE, (x_val, y_val, ball_width, 20))
    pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_length, padd_width))
    text_surface = my_font.render('Score: ' + str(score), False, (255, 255, 255))
    screen.blit(text_surface, (260,0))
      # -- flip display to reveal new position of objects
    pygame.display.flip() 
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop pygame.