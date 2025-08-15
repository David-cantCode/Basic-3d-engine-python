import pygame as py
import math 


blue  = (0, 0, 255)
radius = 15
width = 15

player_x = 350
player_y = 250
angle = 0
SPEED = 10
ROT_SPEED = 0.10
ray_length = 100





def draw(screen):
    py.draw.circle(screen, blue, (player_x, player_y), radius, width)

    # get ray end 
    end_x = player_x + math.cos(angle) * ray_length
    end_y = player_y + math.sin(angle) * ray_length





    py.draw.line(screen, blue, (int(player_x), int(player_y)), (int(end_x), int(end_y)), 2)


def main():
    global player_x, player_y, angle
    #**************************
    #*******MOVING THE PLAYER*********
    #***********************************

    keys = py.key.get_pressed()
    if keys[py.K_a]:
        angle -= ROT_SPEED
    if keys[py.K_d]:
        angle += ROT_SPEED
    if keys[py.K_w]:
        player_x += math.cos(angle) * SPEED
        player_y += math.sin(angle) * SPEED
    if keys[py.K_s]:
        player_x -= math.cos(angle) * SPEED
        player_y -= math.sin(angle) * SPEED














