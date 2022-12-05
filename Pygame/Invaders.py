import pygame
import random
import math
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)

## -- Define the class Invader which is a sprite 
class Invader(pygame.sprite.Sprite): 
    # Define the constructor for snow 
    def __init__(self, color, width, height, speed): 
        # Call the sprite constructor 
        super().__init__()
         # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color) 
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = random.randrange(0, 600) 
        self.rect.y = random.randrange(0, -50)
        # Set speed of the sprite 
        self.speed = speed
         #End Procedure #End Class
    # Class update function - runs for each pass through the game loop 
    def update(self): 
        self.rect.y = self.rect.y + self.speed
        if self.rect.y >480:
            self.rect.y = 0

## -- Define the class Player which is a sprite
class Player(pygame.sprite.Sprite): 
    # Define the constructor for snow 
    def __init__(self, color, width, height): 
        # Call the sprite constructor 
        super().__init__()
         # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color) 
        # Set the position of the sprite 
        self.rect = self.rect(300, size[0] - height)
        # Set speed of the sprite 
        self.speed = 0 
         #End Procedure #End Class
    # Class update function - runs for each pass through the game loop 
    def update(self): 
        self.rect.y = self.rect.y + self.speed
        if self.rect.y >480:
            self.rect.y = 0

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Invaders")
# -- Exit game flag set to false
done = False 
# Create a list of the snow blocks 
invader_group = pygame.sprite.Group()
# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()
# -- Manages how fast screen refreshes
clock = pygame.time.Clock() 

# Create the invaders 
number_of_invaders = 50 
# we are creating 50 invaders 
for x in range (number_of_invaders): 
    my_invaders = Invader(BLUE, 10, 10, 1) 
    # invaders are blue with size 10 by 10 px 
    invader_group.add (my_invaders) 
    # adds the new invaders to the group of invaders 
    all_sprites_group.add (my_invaders) 
    # adds it to the group of all Sprites 
#Next x

### -- Game Loop 
while not done: 
    # -- User input and controls 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        #End If 
    #Next event 
    # -- Game logic goes after this comment
    all_sprites_group.update()
    # -- Screen background is BLACK 
    screen.fill (BLACK)
    # -- Draw here 
    all_sprites_group.draw (screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip() 
    # - The clock ticks over 
    clock.tick(60) 
#End While 
pygame.quit()