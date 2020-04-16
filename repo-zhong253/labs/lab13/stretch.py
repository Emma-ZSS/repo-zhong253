import random
import turtle

def randcolor():
    cl = ['red','yellow','green','blue','purple','orange']
    random.choice(cl)
    

class Shape():
    def __init__(self,x=0,y=0,fillColor='',fill=False):
        self.x = x
        self.y = y
        self.fC = fillColor
        self.fill = fill #???

    def setFillcolor(self,col):
        self.fC = col

    def Filled(self,boolean):
        self.fill = boolean

    def isFilled(self):
        return self.fill

class Circle(Shape):
    def __init__(self,x=0,y=0,fillColor='',fill=False,rad = 1):
        Shape.__init__(self,x,y,fillColor,fill)
        self.r = rad

    def draw(self,myt):
        myt.penup()
        myt.goto(self.x,self.y)
        myt.pendown()
        if self.fill == False:
            myt.circle(self.r)
        else:
            myt.fillcolor(self.fC)
            myt.begin_fill()
            myt.circle(self.r)
            myt.end_fill()



'''
c = Circle(-40,-40)
c.draw(turtle.Turtle())
d = Circle(-40,-40,'red',True,10)
d.draw(turtle.Turtle())
e = Circle(0,0,'yellow',True,100)
e.draw(turtle.Turtle())
'''
