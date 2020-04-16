import turtle
import random

def randcolor():
    cl = ['red','yellow','green','blue','purple','orange']
    return random.choice(cl) # RETURN!!! or it will be none type



class Display:

    
    def __init__(self,myt = turtle.Turtle(),scr = turtle.Screen()):
        
        self.myt = myt
        self.myt.speed(10)
        #self.myt.hideturtle()
        self.scr = scr
        self.scr.onclick(self.mouseEvent) # register mouseEvent
        self.scr.listen()
        

        
    def mouseEvent(self,x,y):
        r = random.randint(1,100)
        fC = randcolor()
        self.myt.penup()
        self.myt.goto(x,y)
        self.myt.pendown()
        self.myt.fillcolor(fC)
        self.myt.begin_fill()
        self.myt.circle(r)
        self.myt.end_fill()

'''
Display()
'''
