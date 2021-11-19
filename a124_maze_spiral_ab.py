import turtle as trtl
maze = trtl.Turtle()

length = 20
path_width = 20
count = 1
maze.hideturtle()
maze.penup()
maze.goto(50,-50)
maze.left(90)
maze.pensize(5)
maze.speed(0)
maze.pendown()
for i in range(25):
  if count < 4:
    maze.penup()
    count += 1
  else:
    maze.pendown()
  #doors
  maze.forward(10)
  maze.penup()
  maze.forward(path_width*2)
  maze.pendown()
  #barriers
  maze.forward(60)
  maze.left(90)
  maze.forward(path_width*2)
  maze.back(path_width*2)
  maze.right(90)
  #walls
  maze.forward(length)
  maze.left(90)
  length += 20


wn = trtl.Screen()
wn.mainloop()