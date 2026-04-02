import turtle #importing library
turtle.Screen().setup(300,400)
polygon = turtle.Turtle() #defined variable


num_sides = 6 #variable
side_length = 90
angle = 360.0 / num_sides
#iterarte loop for total number of sides 
for i in range(num_sides):
  polygon.forward(side_length)
  polygon.right(angle)
  
turtle.done()