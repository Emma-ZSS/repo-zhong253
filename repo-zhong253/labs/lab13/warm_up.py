import turtle
myt = turtle.Turtle()
scr = turtle.Screen()
scr.delay(1) # speed
myt.forward(100)
myt.speed(10)
myt.hideturtle()

# Move turtle
myt.penup()
myt.goto(40,40)
myt.pendown()
myt.circle(100)

# Color Circle
myt.fillcolor('red')
myt.begin_fill()
myt.circle(100)
myt.end_fill()

# Color Rectangle
myt.penup()
myt.goto(-50,-50)
myt.pendown()
myt.fillcolor('blue')
myt.begin_fill()
for i in range(4):
    myt.forward(100)
    myt.right(90)
myt.end_fill()

# On click
def mouseInput(x,y):
    print(x,',',y)
scr.onclick(mouseInput)
scr.listen()
    
