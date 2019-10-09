'''
Sample program using turtle.
The purpose of Turtle graphics in Python is to help start learning python while making it fun & easy
'''
import turtle

#Create a window and optionally set background color, title
win = turtle.Screen()
win.bgcolor("lightgreen")
win.title("Turtle Demo")

#Create turtle and customize
obj = turtle.Turtle()
obj.color('blue')
obj.pensize(10)
obj.speed(1)

#Code to move the turtle
obj.forward(150)
obj.left(90)
obj.forward(100)

input("Press any key to exit")