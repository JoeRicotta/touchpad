import pygame
from pygame.locals import *  #just so that some extra functions work
import time

# turns pygame on
pygame.init()

# opens stream
stream = open('data.txt', 'w')

# initializing variables
x = y = 0
running = 1
screen = pygame.display.set_mode((640, 400))
start = time.time()

# write header
stream.write(f"x\ty\n")

# run program
while running:
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:
        running = 0
        
    elif event.type == pygame.MOUSEMOTION:
        print("mouse at (%d, %d)" % event.pos)
        print(time.time()-start)
        stream.write(f"{event.pos[0]}\t{event.pos[1]}\n")
        
        if event.pos == (300,200):
            screen = pygame.display.set_mode((400, 500))
            
    screen.fill((0, 0, 0))
    pygame.display.flip()
