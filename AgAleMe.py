import turtle
import numpy as np
import random
wn = turtle.Screen()

dirt = turtle.Turtle()
dirt.color("hotpink")
dirt.shape('classic')
dirt.penup()
dirt.speed(0)

print(dirt.pos())

pos = np.array(range(-10,10))
dirt_pos = []
dirt_qtd = 10


for i in range(0,dirt_qtd):
    x = random.choice(pos)*20
    y = random.choice(pos)*20
    dirt.goto(x,y)
    dirt_pos.append([x,y,dirt.stamp()])
dirt.ht()


box = turtle.Turtle()
box.ht()
box.speed(0)
box.penup()
box.goto(-210,-210)
box.pendown()
box.goto(210,-210)
box.goto(210,210)
box.goto(-210,210)
box.goto(-210,-210)

grid = turtle.Turtle()
grid.color('lightgreen')
grid.ht()
grid.speed(0)
grid.penup()
grid.goto(-200,-200)

for i in range (21):
    grid.goto(-200,-200+(i*20))
    grid.pendown()
    grid.goto(200,-200+(i*20))
    grid.penup()
    
grid.goto(-200,-200)

for i in range(21):
    grid.goto(-200+(i*20),-200)
    grid.pendown()
    grid.goto(-200+(i*20),200)
    grid.penup()


agent = turtle.Turtle()
agent.color('red')
agent.speed(0)
pos_x = 0
pos_y = 0

text = turtle.Turtle()
text.speed(0)
text.penup()
text.goto(-230,230)
text.ht()

def tex(score,step):
    text.clear()
    text.write('Score: '+str(score)+'\nstep: '+str(step),move=False, align="left", font=("Arial", 8, "normal"))



def moveup(x,y):
    if y != 200:
        agent.goto(x,y+20)
        return x , y+20
    return x,y


def movedown(x,y):
    if y != -200:
        agent.goto(x,y-20)
        return x , y-20
    return x,y

def moveleft(x,y):
    if x != -200:
        agent.goto(x-20,y)
        return x-20 , y
    return x,y

def moveright(x,y):
    if x != 200:
        agent.goto(x+20,y)
        return x+20 , y
    return x,y

def clean(x,y,dirt_pos,score):
    for i in dirt_pos:
        if x == i[0]:
            if y == i[1]:
                dirt.clearstamp(i[2])
                dirt_pos.remove(i)
                print('removed')
                print(i)
                print(len(dirt_pos))
                score = score + 1
                return dirt_pos, score
    return dirt_pos, score-1


done = False

def isclean(dirt_pos):
    if len(dirt_pos) == 0:
        return True
    else:
        return False

moves = ['up','down','left','right']

step = 0
score = 0
visitados = []

while(done == False):
    move = random.choice(moves)
    visitados.append([pos_x,pos_y])

    if (move == 'up') and ([pos_x,pos_y+20] not in visitados):
        pos_x, pos_y = moveup(pos_x,pos_y)
    if move == 'down' and ([pos_x,pos_y-20] not in visitados):
        pos_x, pos_y = movedown(pos_x,pos_y)
    if move == 'left' and ([pos_x-20,pos_y] not in visitados):
        pos_x, pos_y = moveleft(pos_x,pos_y)
    if move == 'right' and ([pos_x+20,pos_y] not in visitados):
        pos_x, pos_y = moveright(pos_x,pos_y)

    dirt_pos, score = clean(pos_x,pos_y,dirt_pos,score)
    step = step + 1
    tex(score,step)
    done = isclean(dirt_pos)


turtle.done()