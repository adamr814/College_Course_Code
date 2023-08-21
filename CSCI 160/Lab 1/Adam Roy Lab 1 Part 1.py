'''
Adam Roy
CSCI 160
LAB 1 PART 1 "Smile Face"
'''

#import turtle
import turtle

#name and create turtle
turt = turtle.Turtle()

#turtle movements
#outercircle
turt.speed(10)
turt.color("black","yellow")
turt.begin_fill()
turt.circle(200)
turt.end_fill()
turt.penup()
turt.pensize(2)
#lefteye
turt.left(90)
turt.forward(350)
turt.left(90)
turt.forward(75)
turt.left(90)
turt.pendown()
turt.forward(75)
turt.penup()
turt.home()
#righteye
turt.left(90)
turt.forward(350)
turt.right(90)
turt.forward(75)
turt.right(90)
turt.pendown()
turt.forward(75)
turt.penup()
#nose
turt.right(90)
turt.forward(25)
turt.left(45)
turt.forward(50)
turt.pendown()
turt.forward(50)
turt.left(45)
turt.forward(25)
turt.penup()
turt.home()
#mouth
turt.left(90)
turt.forward(135)
turt.right(90)
turt.forward(115)
turt.right(90)
turt.pendown()
for x in range(180):
    turt.forward(2)
    turt.right(1)
#turtlevanish
turt.color("yellow")
turt.forward(10)
#turtle end code
turtle.done()
