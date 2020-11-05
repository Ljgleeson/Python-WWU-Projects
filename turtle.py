# Author: Liam Gleeson
# Description: homework 4, CSCI 141
# Date: 5/20/18

import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

red = turtle.Turtle()
red.color("red")
red.shape("turtle")
red.down
for size in range(0, 92, 2):
    red.stamp()
    red.forward(size)
    red.right(25)


green = turtle.Turtle()
green.color("green")
green.shape("turtle")
green.up()
for size in range(0, 92, 2):
    green.stamp()
    green.forward(size+.5)
    green.right(25.075)


blue = turtle.Turtle()
blue.color("blue")
blue.shape("turtle")
blue.up()
for size in range(0, 92, 2):
    blue.stamp()
    blue.forward(size+1)
    blue.right(25.125)
