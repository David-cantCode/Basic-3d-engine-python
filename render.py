import pygame as py 
import map

                                            #yes i passed this through 4 functions; yes im stupid lol
def render_3d( distance,  projection_plane_dist,  ray, num_rays, screen):
    
    
    wall_height = (map.TILE_SIZE / distance) * projection_plane_dist 

    x = int(ray * ((1200 / num_rays))) # calculate the horizontal size of the wall
    y1 = int(800 / 2 - wall_height / 2) # subs half the wall height from the screen to get the top of the wall, 
    y2 = int(800 / 2 + wall_height / 2) #add half the wall height to the center  get bottem pixel of the wall, 
                                                            #sounds inversed but going up is going down because the cords (0,0 is in the top left of the screen)
   
    
    #change wall color based on distance - farther = less color (darker)

    distance /= 6
    shade = 255 - int(distance * 5)
    shade = max(0, min(100, shade))

    if shade != 0:  #if object is  completely hidden. hopefully makes the program faster
        py.draw.rect(screen, (shade, 0, 0), (x, y1, map.ROWS * map.TILE_SIZE // num_rays + 1, y2 - y1))
