from turtle import *

#we want to paint a house

#step 1: draw a square
width(7)
color("purple")
begin_fill()
shape("turtle")
speed(30)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#step 2:drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#end of door

#last step:drawing a roof

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(10, 130)
pendown()
color("sky blue")
begin_fill()
left(120)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
end_fill()

penup()
goto(150, 130)
pendown()
color("sky blue")
begin_fill()
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
end_fill()