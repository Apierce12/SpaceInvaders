# Simple pygame program

# Import and initialize the pygame library
from Explosion import Explosion
from Enemy import Enemy
import pygame
from Player import Player
from Enemy import Enemy
from Star import Star
from Laser import Laser
from pygame.locals import *
from Background import Background
from Intro import Intro
import sys
import time

#<-----------------------------------------------------------MAIN GAME------------------------------------------------------------------>#

def game():
    #--Setup for sounds. Defaults are good.--#
    pygame.mixer.init()

    #--Initialize pygame--#
    pygame.init()

    #---Creating object---#
    player = Player()
    background = Background()
    
    #-----Background events------#
    back = pygame.sprite.Group()

    #---Music player---#
    pygame.mixer.music.load("music/SpaceCadet.mp3")
    pygame.mixer.music.play(loops=-1)

    #--Keeping track of points--#
    points = 0

    #--This will be a list that will contain all the sprites we intend to use in our game--#
    enemies = pygame.sprite.Group()

    #------Explosion events------#
    explosive_sprite = pygame.sprite.Group()
    explosive_sprite2 = pygame.sprite.Group()

    #--------Laser events--------#
    laser = pygame.sprite.Group()
    laser2 = pygame.sprite.Group()

    #---------All events---------#
    all_sprites = pygame.sprite.Group()

    #---------Adding the player to events to be displayed on a screen--------#
    all_sprites.add(player)

    #---------Set up the drawing window---------#
    screen = pygame.display.set_mode([1500, 800])

    time.sleep(2)

    # Create a custom event for adding a new enemy
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 500)

    '''
    ADDEXPLOSION = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDEXPLOSION, 1000)
    '''
    '''
    ADDSTAR = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDSTAR, 1000)
    '''

    #--------------Main Loop----------------#
    running = True
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            #----when key is down----#
            if event.type == KEYDOWN:
                #---Escape key equals close program---# 
                if event.key == K_ESCAPE:
                    running = False

                elif event.key == K_SPACE:
                    #-----import laser object-----#
                    lasers = Laser()
                    lasers2 = Laser()

                    #---wherever the player is----#
                    #------Lasers are there-------#
                    lasers.rect.x = player.rect.x + 3
                    lasers.rect.y = player.rect.y

                    #---wherever the player is----#
                    #------Lasers are there-------#
                    lasers2.rect.x = player.rect.x + 57
                    lasers2.rect.y = player.rect.y

                    #---adding lasers to event list---#
                    all_sprites.add(lasers)
                    laser.add(lasers)

                    all_sprites.add(lasers2)
                    laser2.add(lasers2)

            #----X button is click----#
            elif event.type == QUIT:
                running = False

            #-----Adding new enemy-----#
            elif event.type == ADDENEMY:
                #-----Creating new enemies adding them into the events log------#
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)  

        #---------Getting key events---------#
        pressed_keys = pygame.key.get_pressed()
        
        back.add(background)
        #--Calculate mechanics for each bullet--#
        for bullet in laser:
    
            #-------See if it hit a block--------#
            block_hit_list = pygame.sprite.spritecollide(bullet, enemies, True)
    
            #------For each block hit, remove the bullet and add to the score-----#
            for block in block_hit_list:
                laser.remove(bullet)
                explode = Explosion(block.rect.x, block.rect.y) 
                explosive_sprite.add(explode)
                all_sprites.remove(bullet) 
                points+=1
    
            #----Remove the bullet if it flies up off the screen----#
            if bullet.rect.y < -10:
                laser.remove(bullet)
                all_sprites.remove(bullet)

        #--Calculate mechanics for each bullet--#
        for bullet in laser2:
    
            #-------See if it hit a block--------#
            block_hit_list = pygame.sprite.spritecollide(bullet, enemies, True)
    
            #------For each block hit, remove the bullet and add to the score-----#
            for block in block_hit_list:
                laser2.remove(bullet)
                explode2 = Explosion(block.rect.x, block.rect.y) 
                explosive_sprite2.add(explode2)
                all_sprites.remove(bullet)
                points+=1
    
            #----Remove the bullet if it flies up off the screen----#
            if bullet.rect.y < -10:
                laser2.remove(bullet)
                all_sprites.remove(bullet)

        #----Fill the background with white----#
        screen.fill((0,0,0))
        
        back.draw(screen)
        explosive_sprite.draw(screen)
        explosive_sprite2.draw(screen)
        
        #---Updating the screen and all events---#
        player.update(pressed_keys)
        laser.update()
        laser2.update()
        enemies.update()
        back.update()
        explosive_sprite.update()
        explosive_sprite2.update()

        #--------------------------Font----------------------------#
        font = pygame.font.Font("pixeboy-font/Pixeboy-z8XGD.ttf", 74)
        text = font.render(str(points), 1, (255, 0, 0))
        screen.blit(text, (750,0))

        #---Draw everything onto the screen---#
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        #--Check if any enemies have collided with the player-->
        if pygame.sprite.spritecollideany(player, enemies):
        #--Then remove the player and stop the loop--#
            player.kill()
            time.sleep(2)
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            running = False

        #-----Display player on screen-----#
        #screen.blit(player.surf, player.rect)

        #--Update the display--#
        pygame.display.flip()

    #--Done! Time to quit.--#
    pygame.quit()
    print("GAME OVER!!!!!!")
    #<-----------------------------------------------------------------------End of Main------------------------------------------------------------------------------->#
    
# Setup for sounds. Defaults are good.
pygame.mixer.init()    
    
#---Initializing the constructor---# 
pygame.init() 

#---------Set up the drawing window---------#
screen = pygame.display.set_mode([1500, 800])

#------------Music-----------#
pygame.mixer.music.load("music/Dead Man Walking.mp3")
pygame.mixer.music.play(loops=-1)

running = True

introduction = Intro()

intro = pygame.sprite.Group()

click = False

while running: 
    
    start_game = pygame.draw.rect(screen,(0,0,0),[750,400,440,55],1)
    
    mouse = pygame.mouse.get_pos()
    
    if start_game.collidepoint((mouse[0], mouse[1])):
        if click:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            game()
    
    click = False
    
    for event in pygame.event.get():
        #----when key is down----#
        if event.type == KEYDOWN:
            #---Escape key equals close program---# 
            if event.key == K_ESCAPE:
                running = False

        #----X button is click----#
        elif event.type == QUIT:
            running = False
            
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
            
    intro.add(introduction)

    #----Fill the background with white----#
    screen.fill((0,0,0))
    
    intro.draw(screen)
    
    font = pygame.font.Font("pixeboy-font/Pixeboy-z8XGD.ttf", 100)
    text = font.render("Start Game", 1, (255, 0, 0))
    text.set_alpha(255)
    screen.blit(text, (750, 400))    
    
    intro.update()
    
    #--Update the display--#
    pygame.display.flip()

#--Done! Time to quit.--#
pygame.quit()