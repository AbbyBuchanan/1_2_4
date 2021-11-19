import turtle as trtl
maze = trtl.Turtle()

length = 20
path_width = 10
maze.hideturtle()
maze.penup()
maze.goto(0,0)
maze.left(90)
maze.pensize(5)
maze.pendown()
for i in range(25):
  maze.forward(10)
  maze.penup()
  maze.forward(path_width*2)
  maze.pendown()
  maze.forward(length)
  maze.left(90)
  length += 20

wn = trtl.Screen()
wn.mainloop()