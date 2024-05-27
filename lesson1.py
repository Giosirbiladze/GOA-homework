from turtle import *


#we want to paint a house

#step 1: draw a square

begin_fill()
width(7)
color("orange")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

forward(200)
left(90)
#end of square

#drawing a door
begin_fill()
forward(70)
color("brown")
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of roof

#drawing windows
color("black")
left(120)
penup()
goto(70,140)
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(50)

penup()
goto(130,140)
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(50)
penup()

exitonclick()
