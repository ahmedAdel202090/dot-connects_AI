from PIL import ImageGrab
import win32api
import win32con
import os
import time

#initially at level 0
y_pad=342
x_pad=607
x_start=19
y_start=11

def play(startPos,row,col,path):
    intialState(row,col)
    startAt(startPos[0],startPos[1])
    x=x_start
    y=y_start
    for motion in path:
        if motion=="left":
            x,y=left(x,y)
        elif motion=="right":
            x,y=right(x,y)
        elif motion == "up":
            x,y=up(x,y)
        elif motion == "down":
            x,y=down(x,y)
def intialState(myRow,myCol):
    row=myRow-3
    col=myCol-3
    global x_pad
    global y_pad
    x_pad-=col*29 
    y_pad-=row*26
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def mousePos(cord):
    win32api.SetCursorPos((cord[0]+x_pad,cord[1]+y_pad))
def up(x,y):
    mousePos([x,y-55])
    time.sleep(.6)
    print("up moved")
    return x,y-55
def down(x,y):
    mousePos([x,y+55])
    time.sleep(.6)
    print("down moved")
    return x,y+55
def left(x,y):
    mousePos([x-57,y])
    time.sleep(.6)
    print("left moved")
    return x-57,y
def right(x,y):
    mousePos([x+57,y])
    time.sleep(.6)
    print("left moved")
    return x+57,y
def startAt(i,j):
    global x_start
    global y_start
    x_start+=j*57
    y_start+=i*55
    mousePos([x_start,y_start])
    leftClick()
    leftClick()
    print("put initial move")
def initialMove():
    mousePos([x_start,y_start])
    leftClick()
    leftClick()
    print("put initial move")
#if __name__ == '__main__':
#    path=["down","down","right","right","up","up","left"]
#    play([0,0],3,3,path)



