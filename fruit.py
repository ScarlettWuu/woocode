#coding:utf-8
from tkinter import *
import random
from constant import *

class fruit:
    def __init__(self, canvas, fp):
        self.canvas = canvas
        x = random.randrange(CANVAS_X/SNAKE_SIZE)*SNAKE_SIZE
        y = random.randrange(CANVAS_Y/SNAKE_SIZE)*SNAKE_SIZE
        self.pos = [x,y]
        # self.fp = PhotoImage(file='durian.gif')
        self.id = self.canvas.create_image(x, y, anchor=NW, image=fp)
        #self.id = self.canvas.create_oval(x, y, x+SNAKE_SIZE, y+SNAKE_SIZE, fill='red', outline='yellow')
        self.canvas.update()

    def getFruitPos(self):
        return self.pos
        # return self.canvas.coords(self.id)

    def beEaten(self): #水果被吃了就新生成一个水果
        old_pos = self.pos
        x = random.randrange(CANVAS_X/SNAKE_SIZE)*SNAKE_SIZE
        y = random.randrange(CANVAS_Y/SNAKE_SIZE)*SNAKE_SIZE
        self.pos = [x,y]
        self.canvas.move(self.id, x-old_pos[0], y-old_pos[1])
        self.canvas.update()