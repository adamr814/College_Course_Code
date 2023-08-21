'''
Adam Roy
CSCI 160
LAB 1 PART 2 "House"
'''

#import turtle
import turtle

#name and create turtle
h = turtle.Turtle()
t = turtle.Turtle()
s = turtle.Turtle()
w = turtle.Turtle()
#turtle movements
#house start
h.forward(100)
h.left(90)
h.forward(175)
h.right(90)
h.forward(25)
h.left(145)
h.forward(154)
h.left(70)
h.forward(154)
h.left(145)
h.forward(25)
h.right(90)
h.forward(175)
h.left(90)
h.forward(100)
h.right(90)
h.penup()
h.forward(10)
#tree start
t.penup()
t.forward(200)
t.pendown()
t.left(90)
t.color("brown")
t.forward(100)
t.right(90)
t.forward(10)
t.right(90)
t.forward(100)
t.right(90)
t.forward(10)
t.penup()
t.backward(5)
t.right(90)
t.forward(90)
t.pendown()
t.color("green")
t.right(90)
t.circle(50)
#window start
w.forward(25)
w.left(90)
w.forward(75)
w.right(90)
w.forward(50)
w.right(90)
w.forward(75)
w.right(90)
w.forward(140)
w.penup()
w.right(90)
w.forward(40)
w.pendown()
w.forward(25)
w.right(90)
w.forward(50)
w.right(90)
w.forward(25)
w.right(90)
w.forward(50)
w.right(90)
#sun start
s.penup()
s.backward(250)
s.left(90)
s.forward(300)
s.pendown()
s.color("yellow", "orange")
s.circle(25)









#turtle end code
turtle.done()
