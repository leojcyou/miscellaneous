from tkinter import *
from math import*
from time import*

root = Tk()
screen = Canvas( root, width = 1000, height = 1000, background = "black" )
screen.pack()

def initialisation():
    global baseAngleO, angleSpeedO, ovalHeight, ovalWidth, bigCenterX, bigCenterY, bigEndX, bigEndY, xSpeedOval
    global baseAngleC, angleSpeedC, radius, anglesArray, dotArray, xPointsCircle, yPointsCircle
    global PointsLines, PointsLine1, PointsLine2, PointsLine3, PointsLine4, PointsLine5, PointsLine6
    global count

    baseAngleO = pi/2
    angleSpeedO = pi/3

    ovalHeight = 400
    ovalWidth = 400
    bigCenterX = 500
    bigCenterY = 500
    bigEndX = 500
    bigEndY = 0
    xSpeedOval = 1

    baseAngleC = pi/2
    angleSpeedC = pi/90

    radius = 50
    anglesArray = []
    dotArray = []
    xPointsCircle = []
    yPointsCircle = []

    PointsLines = []
    PointsLine1 = []
    PointsLine2 = []
    PointsLine3 = []
    PointsLine4 = []
    PointsLine5 = []
    PointsLine6 = []

    PointsLines.append(PointsLine1)
    PointsLines.append(PointsLine2)
    PointsLines.append(PointsLine3)
    PointsLines.append(PointsLine4)
    PointsLines.append(PointsLine5)
    PointsLines.append(PointsLine6)

    count = -1

def clearProgress():
    global xSpeedOval, bigEndX, baseAngleO, baseAngleC, anglesArray, xPointsCircle, yPointsCircle, count
    
    anglesArray = []
    xPointsCircle = []
    yPointsCircle = []

    if (bigEndX == bigCenterX + ovalWidth or bigEndX == bigCenterX - ovalWidth):
        xSpeedOval *= -1
    bigEndX = bigEndX + xSpeedOval

    baseAngleC = baseAngleC + angleSpeedC

    if(bigEndY == bigCenterY-ovalHeight):
        count = count + 1
        print(count)

    screen.delete(dot1, dot2, dot3, dot4, dot5, dot6, line1, line2, line3)
    #screen.delete(trailLine1, trailLine2, trailLine3, trailLine4, trailLine5, trailLine6)
    screen.delete(center, end, ovalLine)

def bigOvalCalc():
    global bigEndY

    posY = sqrt(abs(ovalHeight**2 - (((ovalHeight**2)*((bigEndX-bigCenterX)**2))/ovalWidth**2)))

    if (xSpeedOval > 0):
        bigEndY = bigCenterY - posY
    else:
        bigEndY = bigCenterY + posY

def bigOvalDraw():
    global center, ovalLine, end

    center = screen.create_oval(bigCenterX-2.5, bigCenterY - 2.5, bigCenterX + 2.5, bigCenterY + 2.5, fill="coral")
    end = screen.create_oval(bigEndX-2.5, bigEndY - 2.5, bigEndX + 2.5, bigEndY + 2.5, fill="coral")
    ovalLine = screen.create_line(bigCenterX, bigCenterY, bigEndX, bigEndY, fill="coral")

def drawSmallCirclePoints():
    global dot1, dot2, dot3, dot4, dot5, dot6, line1, line2, line3
    #global trailLine1, trailLine2, trailLine3, trailLine4, trailLine5, trailLine6

    for i in range(6):
        anglesArray.append(baseAngleC + i*pi/3)
        xCoord = bigEndX-radius*cos(anglesArray[i])
        yCoord = bigEndY-radius*sin(anglesArray[i])
        xPointsCircle.append(xCoord)
        yPointsCircle.append(yCoord)

        for j in range(2):
            PointsLines[i].append([xCoord,yCoord])

    for i in range(1):
        line1 = screen.create_line(xPointsCircle[0],yPointsCircle[0],xPointsCircle[3],yPointsCircle[3], fill = "gold")
        line2 = screen.create_line(xPointsCircle[1],yPointsCircle[1],xPointsCircle[4],yPointsCircle[4], fill = "gold")
        line3 = screen.create_line(xPointsCircle[2],yPointsCircle[2],xPointsCircle[5],yPointsCircle[5], fill = "gold")

        #Dot trail
        trail1 = screen.create_oval(xPointsCircle[0]-0.5,yPointsCircle[0]-0.5,xPointsCircle[0]+0.5,yPointsCircle[0]+0.5, fill = "white", outline = "white")
        trail2 = screen.create_oval(xPointsCircle[1]-0.5,yPointsCircle[1]-0.5,xPointsCircle[1]+0.5,yPointsCircle[1]+0.5, fill = "white", outline = "white")
        trail3 = screen.create_oval(xPointsCircle[2]-0.5,yPointsCircle[2]-0.5,xPointsCircle[2]+0.5,yPointsCircle[2]+0.5, fill = "white", outline = "white")
        trail4 = screen.create_oval(xPointsCircle[3]-0.5,yPointsCircle[3]-0.5,xPointsCircle[3]+0.5,yPointsCircle[3]+0.5, fill = "white", outline = "white")
        trail5 = screen.create_oval(xPointsCircle[4]-0.5,yPointsCircle[4]-0.5,xPointsCircle[4]+0.5,yPointsCircle[4]+0.5, fill = "white", outline = "white")
        trail6 = screen.create_oval(xPointsCircle[5]-0.5,yPointsCircle[5]-0.5,xPointsCircle[5]+0.5,yPointsCircle[5]+0.5, fill = "white", outline = "white")

        #Line Trail
        #trailLine1 = screen.create_line(PointsLine1,fill="white")
        #trailLine2 = screen.create_line(PointsLine2,fill="white")
        #trailLine3 = screen.create_line(PointsLine3,fill="white")
        #trailLine4 = screen.create_line(PointsLine4,fill="white")
        #trailLine5 = screen.create_line(PointsLine5,fill="white")
        #trailLine6 = screen.create_line(PointsLine6,fill="white")

        dot1 = screen.create_oval(xPointsCircle[0]-2.5,yPointsCircle[0]-2.5,xPointsCircle[0]+2.5,yPointsCircle[0]+2.5, fill = "white", outline = "white")
        dot2 = screen.create_oval(xPointsCircle[1]-2.5,yPointsCircle[1]-2.5,xPointsCircle[1]+2.5,yPointsCircle[1]+2.5, fill = "white", outline = "white")
        dot3 = screen.create_oval(xPointsCircle[2]-2.5,yPointsCircle[2]-2.5,xPointsCircle[2]+2.5,yPointsCircle[2]+2.5, fill = "white", outline = "white")
        dot4 = screen.create_oval(xPointsCircle[3]-2.5,yPointsCircle[3]-2.5,xPointsCircle[3]+2.5,yPointsCircle[3]+2.5, fill = "white", outline = "white")
        dot5 = screen.create_oval(xPointsCircle[4]-2.5,yPointsCircle[4]-2.5,xPointsCircle[4]+2.5,yPointsCircle[4]+2.5, fill = "white", outline = "white")
        dot6 = screen.create_oval(xPointsCircle[5]-2.5,yPointsCircle[5]-2.5,xPointsCircle[5]+2.5,yPointsCircle[5]+2.5, fill = "white", outline = "white")

    
def runAnimation():

    initialisation()
    while (count<3):
        bigOvalCalc()
        bigOvalDraw()
        drawSmallCirclePoints()
        
        screen.update()
        sleep(0.00000000000002)
        clearProgress()
    
    screen.mainloop()

runAnimation()