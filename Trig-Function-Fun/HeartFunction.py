from tkinter import *
from math import*
from random import*
from time import*

root = Tk()
screen = Canvas( root, width = 1000, height = 1000, background = "blue" )
screen.pack()

progress_Var = -10

def heartPlane():
    screen.create_rectangle(0,0,1000,1000,fill = "White")

def value_Generation():
    global coord_Values

    x = -1.8165
    coord_Values = []

    for i in range(50000):
        y = -((x**2)**(1/3) + (3.3-x**2)**(0.5) * sin((progress_Var)*pi*x))
        coord_Values.append((150*x+498,150*y+498))
        if abs(1.8165-x) <= 2*(0.0003633):
            x = 1.8165
        else:
            x = x + 2*(0.0003633)

def progress_Update():
    global progress_Var, coord_Values

    if progress_Var<10:
        progress_Var += 0.5
    else:
        progress_Var = -10
    
    coord_Values = []

def heartFunction():
    global heart

    heart = screen.create_line(coord_Values,fill="red",width=1)

def runAnimation():

    for i in range(1000):
        heartPlane()
        value_Generation()
        heartFunction()
        progress_Update()

        screen.update()
        
        # sleep(0.0000001)
        screen.delete(heart)
        
runAnimation()



