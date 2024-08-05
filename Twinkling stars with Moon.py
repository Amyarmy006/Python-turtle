import turtle
import random
h=turtle.Turtle()
turtle.bgcolor("black")
h.speed(10)
def polygon(side,length,shade):
    angle=360/side
    h.color(shade)
    for i in range(side):
        h.forward(length)
        h.left(angle)
def traverse(x,y):
    h.penup()
    h.goto(x,y)
    h.pendown()

traverse(400,300)
h.color("white")
h.begin_fill()
h.circle(60)
h.end_fill()

def stars():
    for i in range(5):
        h.fd(10)
        h.right(144)
traverse(10,10)        
stars()
for i in range(100):
    x=random.randint(-640,640)
    y=random.randint(-330,330)
    stars()
    h.penup()
    traverse(x,y)
    
h.goto(-40,20)
stars()
h.hideturtle()
