from PIL import ImageGrab
import os
import time
# (581,312) with shift (203,203) lvl 3
# (608,342) with shift (149,145) lvl1
x_pad=608
y_pad=342
shift_x=149
shift_y=145
#in level 2 3x4
col=1
#in level 3 4x4
col=1
row=1
#row and col which means row=myRow-3 col=myCol-3
x_pad=x_pad-col*29 
shift_x+=col*57
y_pad=y_pad-row*26
shift_y+=row*55



def screenGrab():
    box = (x_pad,y_pad,x_pad+shift_x,y_pad+shift_y)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()