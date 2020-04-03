import pygame
import numpy as np
import random

# game window and variables init

width = 360
height = 600
cube_size = 20
rows = height//cube_size
cols = width//cube_size
window = pygame.display.set_mode((width,height))
game = True
matrix = np.zeros((rows,cols),dtype = int)
tetris_shapes = ['L','S','C','|']
random_shape = ''
block = False
x=5
y=0
indexr = 0

class shape():
    def __init__(self):
        self.shapes = {
            'L' : [
                np.ones((3,2),dtype = int),
                np.ones((2,3),dtype = int),
                np.ones((3,2),dtype= int),
                np.ones((2,3),dtype = int)
            ],
            'S' : [
                np.ones((5,2),dtype = int),
                np.ones((5,2),dtype = int)
            ],
            'C' : [
                np.ones((2,2),dtype = int)
            ],
            '|' : [
                np.ones((4,1),dtype = int),
                np.ones((1,4),dtype = int)
            ]
        }

        # change the values of the 2d list to match the shape
        # use 1's to represent shape
        self.shapes['L'][0][0][1] = 0
        self.shapes['L'][0][1][1] = 0
        self.shapes['L'][1][1][1] = 0
        self.shapes['L'][1][1][2] = 0
        self.shapes['L'][2][1][0] = 0
        self.shapes['L'][2][2][0] = 0
        self.shapes['L'][3][0][0] = 0
        self.shapes['L'][3][0][1] = 0

        self.shapes['S'][0][1][1] = 0
        self.shapes['S'][0][3][0] = 0
        self.shapes['S'][1][1][0] = 0
        self.shapes['S'][1][3][1] = 0
    
    def draw(self,shp,pos,index):
        for i in range(len(self.shapes[shp][index])):
            for j in range(len(self.shapes[shp][index][i])):
                if self.shapes[shp][index][i][j] == 1:
                    start_pos_x = cube_size*pos[0]+1+j*cube_size
                    start_pos_y = cube_size*pos[1]+1+i*cube_size
                    pygame.draw.rect(window, (255,255,255), (start_pos_x,start_pos_y,cube_size-2,cube_size-2))

# draw grid on window
def grid():
    x = 0
    y = 0
    for i in range(height//cube_size):
        x += cube_size
        y += cube_size
        pygame.draw.line(window,(255,255,255),(x,0),(x,height))
        pygame.draw.line(window,(255,255,255),(0,y),(width,y))

# rotate the shapes by changing the index
def change_index(direction):
    global indexr
    max_index = 0
    if random_shape == 'L':
        max_index = 3
    elif random_shape == 'C':
        return 0
    elif random_shape == 'S':
        max_index = 1
    else:
        max_index = 1
    if indexr == max_index and direction == 1:
        indexr = 0
    elif indexr == 0 and direction == -1:
        indexr = max_index
    else:
        indexr += direction


tetris = shape()
clock = pygame.time.Clock()
clock.tick(10)
# game loop and logic
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    for _ in keys:
        if keys[pygame.K_RIGHT] and cols > x+len(tetris.shapes[random_shape][indexr][0]):
            x +=1
            break
        elif keys[pygame.K_LEFT] and x>0:
            x -= 1
            break
        elif keys[pygame.K_UP]:
            change_index(-1)
            break
        elif keys[pygame.K_DOWN]:
            change_index(1)
            break
    window.fill((0,0,0))
    grid()
    if not block:
        random_shape = random.choice(tetris_shapes)
        block = True
    tetris.draw(random_shape,[x,y],indexr)
    pygame.time.wait(50)
    pygame.display.update()