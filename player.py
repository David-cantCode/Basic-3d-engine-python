import pygame as py
import math 
import render

blue  = (0, 0, 255)
radius = 15
width = 15

player_x = 350
player_y = 250
angle = 0
SPEED = 10
ROT_SPEED = 0.10
ray_length = 100
new_y = 0
new_x = 0
FOV = math.pi / 3   
num_rays = 800     
max_depth = 10000

#will  organize (maybe *toung out emoji*)



def draw(screen):
    #only used in debugging 

    py.draw.circle(screen, blue, (player_x, player_y), radius, width)

    # get ray end 
    end_x = player_x + math.cos(angle) * ray_length
    end_y = player_y + math.sin(angle) * ray_length


    py.draw.line(screen, blue, (int(player_x), int(player_y)), (int(end_x), int(end_y)), 2)


def main(map, tile_size):
    global player_x, player_y, angle, new_y, new_x 
    #**********************************
    #*******MOVING THE PLAYER**********
    #***********************************
    new_x = player_x
    new_y = player_y



    keys = py.key.get_pressed()
    if keys[py.K_a]:
        angle -= ROT_SPEED
    if keys[py.K_d]:
        angle += ROT_SPEED
    if keys[py.K_w]:
        new_x += math.cos(angle) * SPEED
        new_y += math.sin(angle) * SPEED
    if keys[py.K_s]:
        new_x -= math.cos(angle) * SPEED
        new_y -= math.sin(angle) * SPEED


    #idk why its so choppy ill search for a tutorial later



    #collision check apply new position if it doesnt go through a wall.
    if map[int(new_y // tile_size)][int(new_x // tile_size)] == 0:
        player_x = new_x
        player_y = new_y


def cast_ray(map, tile_size, screen, projection_plane_dist ):
    start_angle = angle - FOV / 2


    for ray in range(num_rays):
        ray_angle = start_angle + (ray / num_rays) * FOV
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        for depth in range(max_depth): #for each length the ray could be, not effecient? idk how to other wise.
            ray_x = player_x + cos_a * depth
            ray_y = player_y + sin_a * depth
            map_x = int(ray_x // tile_size)
            map_y = int(ray_y // tile_size)




            if map[map_y][map_x] == 1:  # if it hits wall, would have to change if i add other objects such as enemies
               
                #*******************************
                #*********DRAW IN 3D***********
                #******************************
                dx = ray_x - player_x # x distance wall - player
                dy = ray_y - player_y # y dis wall - player 
                distance = math.sqrt(dx * dx + dy * dy)  # nerdy pythageris therim to get distance  of the Resultant, 
                                                        #guess i eneded up learning something from physics lol

                render.render_3d( distance, projection_plane_dist, ray, num_rays, screen )



                #2d debug lines
                #py.draw.line(screen, (0, 255, 0), (int(player_x), int(player_y)), (int(ray_x), int(ray_y)), 1)
                break #python gets mad if i dont have this here lol, idk why 



