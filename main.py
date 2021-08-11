# Simple pygame program

# Import and initialize the pygame library
from Star import Star
from Enemy import Enemy
import pygame
from Player import Player
from Enemy import Enemy
from Star import Star
from Laser import Laser
from pygame.locals import *
import time

pygame.init()

#Creating player object
player = Player()

points = 0
# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering

enemies = pygame.sprite.Group()

laser = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

all_sprites.add(player)

# Set up the drawing window
screen = pygame.display.set_mode([1500, 800])

time.sleep(2)

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDSTAR = pygame.USEREVENT + 2
pygame.time.set_timer(ADDSTAR, 1000)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        #If key is hit
        if event.type == KEYDOWN:
            #If that key is the escape key exit program 
            if event.key == K_ESCAPE:
                running = False

            elif event.key == K_SPACE:
                # Fire a bullet if the user clicks the mouse button
                lasers = Laser()
                # Set the bullet so it is where the player is
                lasers.rect.x = player.rect.x
                lasers.rect.y = player.rect.y
                # Add the bullet to the lists
                all_sprites.add(lasers)
                laser.add(lasers)

        #If the exit button is click leave program
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

        # Calculate mechanics for each bullet
    for bullet in laser:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, enemies, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            laser.remove(bullet)
            all_sprites.remove(bullet)
            points+=1
            print(points)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            laser.remove(bullet)
            all_sprites.remove(bullet)

    # Fill the background with white
    screen.fill((0,0,0))

    #Updating a space on the display
    player.update(pressed_keys)
    laser.update()
    enemies.update()

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
    # If so, then remove the player and stop the loop
        player.kill()
        time.sleep(2)
        running = False

    #Display image on a screen
    screen.blit(player.surf, player.rect)

    #Update the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
print("GAME OVER!!!!!!")