import pygame as py
import map
import player
import math



screen = py.display.set_mode((map.COLS * map.TILE_SIZE, map.ROWS * map.TILE_SIZE))
py.display.set_caption("3d Engine lol") 
clock  = py.time.Clock()
                        

#explaination of the 3d effect.          
projection_plane_dist = (map.COLS * map.TILE_SIZE / 2) / math.tan(player.FOV / 2)
    #this help scales everything to fit in the screen well. 
#tile_size / distance in "wall_height = (tile_size / distance) * projection_plane_dist" makes closer walls taller, and farther walls smalelr



white  = (255, 255, 255)
black = (0, 0, 0)











def draw_map():
        #not called if not debuggin 

        for row in range(map.ROWS):
            for col in range(map.COLS):
                value = map.map[row][col]
                if value == 0:
                    py.draw.rect(screen, black, 
                        (col * map.TILE_SIZE, row * map.TILE_SIZE, map.TILE_SIZE, map.TILE_SIZE), 
                        1) #outline 

                if value == 1:
                    py.draw.rect(screen, white, 
                        (col * map.TILE_SIZE, row * map.TILE_SIZE, map.TILE_SIZE, map.TILE_SIZE), 
                        1)  
                






running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT: 
            running = False

        screen.fill((0, 0, 0)) 
        #draw_map()
        #player.draw(screen)
        player.main(map.map, map.TILE_SIZE)
        player.cast_ray(map.map, map.TILE_SIZE, screen, projection_plane_dist)
    
    
    py.display.flip() 
    clock.tick(30)


