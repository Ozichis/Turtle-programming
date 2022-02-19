import time
from turtle import *

# Definition of Turtle Screen
wn = Screen()
wn.bgcolor("deepskyblue")

# Definition of Turtle cursor
cursor = Turtle()
cursor.pensize(5)
cursor.pencolor("red")
cursor.shape('turtle')

# Holding up the pen to set its position without drawing
cursor.penup()
cursor.setpos(cursor.xcor()+10, cursor.ycor()-30)
cursor.pendown()

# Assigning color for next drawing
cursor.fillcolor("light blue")

# Giving the command to color the drawing
cursor.begin_fill()

# Drawing the first window
cursor.forward(40)
cursor.right(90)
cursor.forward(40)
cursor.right(90)
cursor.forward(40)
cursor.right(90)
cursor.forward(40)

# Ending the coloring of the shape
cursor.end_fill()

# Holding the pen to set position for next drawing
cursor.penup()
cursor.setx(cursor.xcor()+140)
cursor.sety(cursor.ycor()-40)
cursor.pendown()

# Setting color for next drawing
cursor.fillcolor("light blue")

# Starting color of shapes
cursor.begin_fill()

# Drawing second window
cursor.forward(40)
cursor.right(90)
cursor.forward(40)
cursor.right(90)
cursor.forward(40)
cursor.right(90)
cursor.forward(40)

# Stop the coloring of shape
cursor.end_fill()

# Holding the pen to go to its default location
cursor.penup()
cursor.home()
cursor.pendown()

# Drawing body of the house
cursor.forward(200)
cursor.right(90)
cursor.forward(200)
cursor.right(90)
cursor.forward(200)
cursor.right(90)
cursor.forward(200)

# Setting x-position of cursor
cursor.setx(cursor.xcor()-30)

# Setting color for next drawing
cursor.fillcolor("purple")

# Drawing the roof
cursor.begin_fill()
cursor.left(120)
cursor.back(150)

cursor.left(120)
cursor.forward(150)


cursor.home()
cursor.end_fill()

# Holding pen to set new cursor position
cursor.penup()
cursor.setpos(70, -200)
cursor.pendown()

# Setting border and background color
cursor.pencolor("brown")
cursor.fillcolor("yellow")

# Drawing the door
cursor.begin_fill()
cursor.right(90)
cursor.back(90)
cursor.right(90)
cursor.back(50)
cursor.right(90)
cursor.back(90)
cursor.end_fill()

# Holding pen for new position
cursor.penup()
cursor.setpos(cursor.xcor()-40, cursor.ycor()+60)
cursor.pendown()

# Drawing the door handle
cursor.dot(2, "brown")
cursor.right(-90)
cursor.back(10)
cursor.right(-90)
cursor.back(2)

# Setting position for the sun
cursor.penup()
cursor.setpos(-200, 80)
cursor.pendown()

# Arranging colors for the sun
cursor.pencolor("orange")
cursor.fillcolor("yellow")

# Drawing the sun with circle function for body and for loop for the rays
cursor.begin_fill()
cursor.circle(50)
cursor.end_fill()

for i in range(19):
    cursor.rt(90)
    cursor.fd(40)
    cursor.bk(40)
    cursor.lt(90)
    cursor.circle(50,20)

# Setting position for grass
cursor.penup()
cursor.goto(-310, -250)
cursor.pendown()

# Setting new cursor angle
cursor.setheading(90)

# Setting color for the grass
cursor.fillcolor("green")
cursor.pencolor("green")

# Drawing the grass
cursor.begin_fill()
cursor.right(90)
cursor.forward(700)
cursor.rt(90)
cursor.forward(150)
cursor.rt(90)
cursor.forward(700)
cursor.rt(90)
cursor.forward(150)
cursor.end_fill()

# Drawing our border line for the whole image
cursor.pencolor("black")
cursor.pensize(3)
cursor.forward(700)
cursor.rt(90)
cursor.forward(700)
cursor.rt(90)
cursor.forward(700)

# Ending our code with turtle mainloop function
mainloop()