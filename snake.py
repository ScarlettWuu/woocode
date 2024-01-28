# coding:utf-8
from tkinter import *
from constant import *


class snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.len = 3  # 游戏开始时蛇身长度为三节
        self.body = [[40, 200], [20, 200], [0, 200]]  # 这是三节的左上角坐标位置
        self.bodyId = []  # 用于存放三节身体的item id
        self.speed = [SNAKE_SIZE, 0]
        self.eatFruitFlag = False  # 是否吃到了水果的标识，用于延长蛇身
        for i in range(3):
            id = self.canvas.create_rectangle(self.body[i][0], self.body[i][1], self.body[i][0] + SNAKE_SIZE,
                                              self.body[i][1] + SNAKE_SIZE, fill='grey', outline='white')
            self.bodyId.append(id)
        self.canvas.itemconfig(self.bodyId[0],fill='red')
        self.canvas.update()
        self.canvas.bind_all('<KeyPress-Up>', self.changeDirection)
        self.canvas.bind_all('<KeyPress-Down>', self.changeDirection)
        self.canvas.bind_all('<KeyPress-Left>', self.changeDirection)
        self.canvas.bind_all('<KeyPress-Right>', self.changeDirection)

    def move(self):
        if self.eatFruitFlag:  # 如果吃了水果，克隆一个尾巴叠加在尾巴上。这样蛇就有两个重叠的尾巴，下面移动时，只会移动一个尾巴，显示的结果就是蛇变长了。
            pos_tail = self.body[self.len - 1]
            self.body.append(pos_tail)
            id = self.canvas.create_rectangle(pos_tail[0], pos_tail[1], pos_tail[0] + SNAKE_SIZE,
                                              pos_tail[1] + SNAKE_SIZE, fill='grey', outline='white')
            self.bodyId.append(id)
            self.len += 1
            self.eatFruitFlag = False

        # 蛇的移动就是把尾巴那一节移到脑袋前
        pos_tail = self.body.pop()
        id_tail = self.bodyId.pop()
        x = (self.body[0][0] + self.speed[0]) % CANVAS_X
        y = (self.body[0][1] + self.speed[1]) % CANVAS_Y
        pos_head = [x, y]
        self.body.insert(0, pos_head)
        self.bodyId.insert(0, id_tail)
        self.canvas.itemconfig(self.bodyId[0], fill='red')
        self.canvas.itemconfig(self.bodyId[1], fill='grey')

        self.canvas.move(id_tail, pos_head[0] - pos_tail[0], pos_head[1] - pos_tail[1])
        self.canvas.update()

    def changeDirection(self, event):
        if event.keysym == 'Up':
            self.speed = [0, -SNAKE_SIZE]
        elif event.keysym == 'Down':
            self.speed = [0, SNAKE_SIZE]
        elif event.keysym == 'Left':
            self.speed = [-SNAKE_SIZE, 0]
        elif event.keysym == 'Right':
            self.speed = [SNAKE_SIZE, 0]
        else:
            print('what happened')

    def eatFruit(self, fruitePos):  # 返回True表示吃到了水果, False表示没有吃到水果
        if fruitePos in self.body:
            self.eatFruitFlag = True
            return True
        return False

    def collideWall(self):  # 返回True表示吃到了撞到边框了, False表示没有
        if self.body[0][0] < 0 or self.body[0][0] >= CANVAS_X or self.body[0][1] < 0 or self.body[0][1] >= CANVAS_Y:
            return True
        return False

    def collideBody(self):  # 返回True表示蛇头碰到自己的身体了, False表示没有
        if self.body[0] in self.body[1:]:
        # if self.body.count(self.body[0]) > 1:
            return True
        return False

    def auto_move(self, food_pos):
        if food_pos[1] < self.body[0][1] :  # event.keysym == 'Up':
            self.speed = [0, -SNAKE_SIZE]
        elif food_pos[1] > self.body[0][1]:  # event.keysym == 'Down':
            self.speed = [0, SNAKE_SIZE]
        elif food_pos[0] < self.body[0][0]:  # event.keysym == 'Left':
            self.speed = [-SNAKE_SIZE, 0]
        elif food_pos[0] > self.body[0][0]:  # event.keysym == 'Right':
            self.speed = [SNAKE_SIZE, 0]
        self.move()
# if  __name__ =='__main__':
#     print 'test'
# else:
#
# if  __name__ =='snake':
#     print 'be imported'
