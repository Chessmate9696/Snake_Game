#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import random
import pygame
import random
import tkinter as tk
from tkinter import messagebox

width = 500
height = 500

cols = 25
rows = 20


class cube():
    rows = 20
    w = 500
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = dirnx
        self.dirny = dirny # "L", "R", "U", "D"
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos  = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
            

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1,dis-2,dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)
        


class snake():
    body = []
    turns = {}
    
    def __init__(self, color, pos):
        #pos is given as coordinates on the grid ex (1,5)
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirny = -1
                    self.dirnx = 0
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirny = 1
                    self.dirnx = 0
                    self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
        
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                c.move(c.dirnx,c.dirny)
        
        
    def reset(self,pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
    
    def draw(self, surface):
        for i,c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)



def redrawWindow():
    global win
    win.fill((0,0,0))
    drawGrid(width, rows, win)
    s.draw(win)
    snack.draw(win)
    pygame.display.update()
    pass



def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y +sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x, 0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0, y),(w,y))
    


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(1,rows-1)
        y = random.randrange(1,rows-1)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
               continue
        else:
               break

    return (x,y)


def main():
    global s, snack, win
    win = pygame.display.set_mode((width,height))
    s = snake((255,0,0), (10,10))
    s.addCube()
    snack = cube(randomSnack(rows,s), color=(0,255,0))
    flag = True
    clock = pygame.time.Clock()
    
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        headPos = s.head.pos
        if headPos[0] >= 20 or headPos[0] < 0 or headPos[1] >= 20 or headPos[1] < 0:
            print("Score:", len(s.body))
            s.reset((10, 10))

        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows,s), color=(0,255,0))
            
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print("Score:", len(s.body))
                s.reset((10,10))
                break
                    
        redrawWindow()

main()
    


# In[7]:


import turtle
import random

#head orientation
h = [0]

#score
a = [0]
b = [0]

#food coord
fcoord = [0,0,0]

#position
pos = []

#resets all the variables and clears the turtle screen to display the start message
def home(x,y):
    x = 0
    y = 0
    a[0] = 0
    b[0] = 0
    h[0] = 0
    fcoord[2] = 0
    pos[:] = []
    turtle.hideturtle()
    turtle.clear()
    turtle.pu()
    turtle.color("black")
    turtle.goto(0,0)
    turtle.write("Play")
    turtle.title("Snake game")
    turtle.onscreenclick(start)
    turtle.mainloop()
#draws the borders of the game using the turtle module.
def game():
    turtle.clear()
    turtle.pu()
    turtle.speed(0)
    turtle.pensize(20)
    turtle.color("grey")
    turtle.goto(-220,220)
    turtle.pd()
    turtle.goto(220,220)
    turtle.goto(220,-220)
    turtle.goto(-220,-220)
    turtle.goto(-220,220)
    turtle.pu()
    turtle.goto(0,0)
#Starts the game by calling game() function when the player press start and call the movement functions so the player can play
def start(x,y):
    turtle.onscreenclick(None)

    game()

    tfood = turtle.Turtle()
    tfood.hideturtle()
    tfood.pu()
    tfood.speed(0)
    tfood.shape("square")
    tfood.color("red")

    tscore = turtle.Turtle()
    tscore.hideturtle()
    tscore.pu()
    tscore.speed(0)
    tscore.goto(100,-250)
    tscore.write("Score:" + str(a[0]), align="center",font=(10))
    
    while x > -210 and x < 210 and y > -210 and y <210:
        if fcoord[2] == 0:
            food(tfood)
            fcoord[2] = 1
        turtle.onkey(u,"Up")
        turtle.onkey(l,"Left")
        turtle.onkey(r,"Right")
        turtle.onkey(d,"Down")
        turtle.listen()
        move()
        x = turtle.xcor()
        y = turtle.ycor()        
        if x > fcoord[0]*20-5 and x < fcoord[0]*20+5 and y > fcoord[1]*20-5 and y < fcoord[1]*20+5:
            fcoord[2] = 0
            tfood.clear()
            a[0] += 1
            tscore.clear()
            tscore.write("Score:" + str(a[0]), align="center",font=(10))
        
        if len(pos) > 1:
            for i in range(1,len(pos)):
                if x < pos[i][0]+5 and x > pos[i][0]-5 and y < pos[i][1]+5 and y > pos[i][1]-5:
                        tscore.clear()
                        tfood.clear()
                        gameover()
    tscore.clear()
    tfood.clear()
    gameover()


#generates random coordinates for food on the screen
def food(tfood):
    x = random.randrange(-8,8,1)
    y = random.randrange(-8,8,1)
    fcoord[0] = x
    fcoord[1] = y
    tfood.hideturtle()
    tfood.pu()
    tfood.shape("square")
    tfood.color("red")
    tfood.goto(x*20,y*20)
    tfood.stamp()
#Movement functions
#Up   
def u():
    if h[0] == 270:
        pass
    else:
        h[0] = 90
#Down
def d():
    if h[0] == 90:
        pass
    else:
        h[0] = 270
#Left
def l():
    if h[0] == 0:
        pass
    else:
        h[0] = 180
#Right
def r():
    if h[0] == 180:
        pass
    else:
        h[0] = 0
# updates the position of the snake by moving it one step forward
def move():
    turtle.pensize(1)
    turtle.color("black")
    turtle.pu()
    turtle.speed(3)
    turtle.setheading(h[0])
    turtle.shape("square")
    turtle.stamp()
    turtle.fd(20)
    x = turtle.xcor()
    y = turtle.ycor()
    if b[0] > a[0]:     
        turtle.clearstamps(1)
        pos.insert(0,[round(x),round(y)])
        pos.pop(-1)
    else:
        pos.insert(0,[round(x),round(y)])       
        b[0] += 1    
#displays the "Game Over" message and the final score    
def gameover():
    turtle.onscreenclick(None)
    turtle.speed(0)
    turtle.pu()
    turtle.goto(0,150)
    turtle.color("red")
    turtle.write("Game Over",align="center", font=(10))
    turtle.goto(0,50)
    turtle.write("Score:" + str(a[0]),align="center",font=(10))
    turtle.goto(200,-200)
    turtle.write("(Click anywhere to return to the main menu)",align="right",font=(0.0000001))
    turtle.onscreenclick(home)
    turtle.mainloop()
    
        
# # # # # # # # # # # # # # # # # # # # # #
# Main                                    #
# # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':
    home(0,0)


# In[ ]:





# In[ ]:




