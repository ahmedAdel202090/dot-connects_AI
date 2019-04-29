from PIL import ImageGrab
import win32api
import win32con
import os
import time

#x_pad=417
#y_pad=159
#def screenGrab():
#    box = (x_pad+1,y_pad+1,x_pad+532,y_pad+568)
#    im = ImageGrab.grab(box)
#    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
#'.png', 'PNG')
 
#def main():
#    screenGrab()
 
#if __name__ == '__main__':
#    main()
y_pad=159
x_pad=417
#lvl 1 (205,205)
#lvl 2 (175,200)
#lvl 3 (180,173)
#lvl 4 (180,85)
#lvl 5 (150,85)

x_start=150
y_start=85

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
def initialMove():
    mousePos([x_start,y_start])
    leftClick()
    leftClick()
    print("put initial move")
if __name__ == '__main__':
    initialMove()
    x,y=right(x_start,y_start)
    x,y=down(x,y)
    x,y=left(x,y)



