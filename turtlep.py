import turtle

window=turtle.Screen()
window.screensize(1200,1200)

draw=turtle.Turtle()
draw.pensize(2)

angle = [90,90,90,90]


for i in angle:
        draw.left(i)
        draw.forward(100)
