import pyscreeze as ImageGrab
import time

image_folder = "DigitRec/orig_images/6/"

for i in range(0,1):
    #time.sleep()
    im=ImageGrab.screenshot(region=(530,230, 250, 250))
    print ("saved...",i)
    im.save(image_folder+str(i)+'.png')
    print ("clearing screen, redraw..")
