# red filled heart shape with text in center


from turtle import *

color('red')

begin_fill()
pensize(5)
setposition(0, 0)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

penup()
setposition(0, 220)
pendown()

write("HACKTOBERFEST 2022", font=("Arial", 20, "bold"), align="center")

hideturtle()
done()
