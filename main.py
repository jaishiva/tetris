import pygame
import numpy as np

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

tetris = shape()

for i in range(4):
    print(tetris.shapes['L'][i])
