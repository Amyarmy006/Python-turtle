import turtle
h=turtle.Turtle()
h.color("red")
def polygon(side,length,shade):
    angle=360/side
    h.color(shade)
    for i in range(side):
        h.forward(length)
        h.left(angle)
for i in range(20):
    h.begin_fill()
    polygon(3,100,"orange")
    h.end_fill()
    h.right(20)
