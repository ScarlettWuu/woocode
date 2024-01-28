#coding:utf-8
from tkinter import *
import time
from snake import *
from fruit import *
from constant import *

root = Tk()
canvas = Canvas(root,width=CANVAS_X,height=CANVAS_Y, bg="white")
canvas.pack()

fp = PhotoImage(file='goldenpenny.gif')
# myBackground = PhotoImage(file='background.gif')
# canvas.create_image(0,0,anchor=NW,image= myBackground)
canvas.update()

s = snake(canvas)
f = fruit(canvas, fp)

score = 0
while True:
    s.move()

    pos1 = f.getFruitPos()
    # s.auto_move(pos1)
    if s.eatFruit(pos1) == True: #如果吃到了水果
        f.beEaten()
        score += 1

    if s.collideWall() or s.collideBody(): #如果撞边框或自己的身体，则游戏结束
        break

    time.sleep(0.02)

canvas.create_text(CANVAS_X/2, CANVAS_Y/2, text="Game Over\n  score: %d"%score, fill='red', font=('Arial Black', 28))
mainloop()