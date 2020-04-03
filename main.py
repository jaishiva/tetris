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
    
    def draw(self,shp):
        for i in self.shapes[shp]:
            print(i)

tetris = shape()

tetris.draw('L')
tetris.draw('C')
tetris.draw('|')