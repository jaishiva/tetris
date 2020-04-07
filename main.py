import pygame
import numpy as np
import random

pygame.init()
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
score = 0
pygame.font.init()
# font for score and game over
font =  pygame.font.Font('freesansbold.ttf', 24)
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 

# Shape object, holds all the shapes and method to draw them on the screen
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
    global indexr,y
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
        if check_for_index(0,y):
            indexr = 0
    elif indexr == 0 and direction == -1:
        if check_for_index(max_index,y):
            indexr = max_index
    else:
        if check_for_index(indexr+direction,y):
            indexr += direction

# check if the blocks can move down 
def check_for_index(index,h):
    if h-1 < len(matrix):
        for i in range(len(tetris.shapes[random_shape][index])):
            for j in range(len(tetris.shapes[random_shape][index][i])):
                if tetris.shapes[random_shape][index][i][j] == 1 and h+i < len(matrix):
                    if matrix[h+i][x+j] == 1:
                        return False
    return True

# draw the main matrix that holds blocks once they stop moving
def draw_matrix():
    for mrow in reversed(range(len(matrix[0]))):
        for mcol in range(len(matrix)):
            if matrix[mcol][mrow] == 1:
                pygame.draw.rect(window,(255,255,255),(mrow*cube_size,mcol*cube_size,cube_size-1,cube_size-2))

# save the shape of blocks into matrix after they stop moving
def set_matrix():
    for i in range(len(tetris.shapes[random_shape][indexr])):
        for j in range(len(tetris.shapes[random_shape][indexr][i])):
            if tetris.shapes[random_shape][indexr][i][j] ==1:
                matrix[y+i][x+j] = tetris.shapes[random_shape][indexr][i][j]

# check if the blocks can be moved left or right
def check_horizontal(dx):
    global x,y
    if dx == -1:
        dy = 0
    elif dx == 1:
        dy = -1
    for i in range(len(tetris.shapes[random_shape][indexr])):
        if matrix[y+i][x+dx] == 1 and tetris.shapes[random_shape][indexr][i][dy] ==1:
            return False
    return True

# inititate new block
def new_block():
    global random_shape,block,x,y,indexr
    random_shape = random.choice(tetris_shapes)
    block = True
    x=5
    y=0
    indexr = 0

# check to see which keys are pressed to move the blocks or rotate them
def check_pressed_keys():
    global x
    keys = pygame.key.get_pressed()
    for _ in keys:
        if keys[pygame.K_RIGHT] and cols > x+len(tetris.shapes[random_shape][indexr][0]):
            if check_horizontal(1):
                x +=1
                break
        elif keys[pygame.K_LEFT] and x>0:
            if check_horizontal(-1):
                x -= 1
                break
        elif keys[pygame.K_UP]:
            change_index(-1)
            break
        elif keys[pygame.K_DOWN]:
            change_index(1)
            break

# refactor matrix once an entire line is filled
def refactor_matrix():
    global cols,matrix
    roww = 0
    for row in reversed(range(len(matrix))):
        if matrix[row].all() == 1:
            score += 1
            for roww in reversed(range(row)):
                matrix[roww+1] = matrix[roww]
            matrix[0] = np.zeros((1,cols), dtype = int)

tetris = shape()
clock = pygame.time.Clock()
clock.tick(10)

# game loop and logic
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    check_pressed_keys()
    window.fill((0,0,0))
    grid()
    draw_matrix()
    text = font.render('Score is {}'.format(score), True, green)
    textRect = text.get_rect()  
    textRect.center = (width - 80, 10)
    window.blit(text,textRect)
    if not block:
        new_block()
    tetris.draw(random_shape,[x,y],indexr)
    if (not check_for_index(indexr,y+1)) or y == len(matrix)-1:
        set_matrix()
        new_block()
    else: 
        if y < len(matrix) - len(tetris.shapes[random_shape][indexr]):
            y+=1
        else:
            print('reached end')
            set_matrix()
            new_block()
    refactor_matrix()
    pygame.display.update()
    pygame.time.wait(100)