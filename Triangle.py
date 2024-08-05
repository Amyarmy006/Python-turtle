import turtle
h=turtle.Turtle()
def polygon(side,length):
    angle=360/side
    for i in range(side):
        h.forward(length)
        h.left(angle)
polygon(3,100)
