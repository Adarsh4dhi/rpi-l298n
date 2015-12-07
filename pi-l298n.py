#!/usr/bin/python3.4
#MKerbachi November 6th, 2015
#Python code to control two motors with Rpi A+ with the H bridge l298n

import RPi.GPIO as GPIO # always needed with RPi.GPIO  
import time
import curses


# get the curses screen window
screen = curses.initscr()
 
# turn off input echoing
curses.noecho()
 
# respond to keys immediately (don't wait for enter)
curses.cbreak()
 
# map arrow keys to special values
screen.keypad(True)



#If the two GND (PI + l298n) are not interconnected that won't work !
#For all Keyboard symbols:
#https://docs.python.org/2/library/curses.html
  
GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM  

#################################################################
#			Variables		  		#
#################################################################

#For Motor #1
GPIO.setup(18, GPIO.OUT)# set GPIO 01 as an output Enabler
GPIO.setup(24, GPIO.OUT)# set GPIO 05 as an output.
GPIO.setup(23, GPIO.OUT)# set GPIO 04 as an output.
  
p24 = GPIO.PWM(24, 100)
p23 = GPIO.PWM(23, 100)
p18 = GPIO.PWM(18, 100)    # create an object p for PWM on port 18 at 50 Hertz
                        # you can have more than one of these, but they need
                        # different names for each port
                        # e.g. p1, p2, motor, servo1 etc.

#For Motor #2
GPIO.setup(13, GPIO.OUT)# set GPIO 03 as an output Enabler
GPIO.setup(27, GPIO.OUT)# set GPIO 02 as an output.
GPIO.setup(17, GPIO.OUT)# set GPIO 0  as an output.

p27 = GPIO.PWM(27, 100)
p17 = GPIO.PWM(17, 100)
p13 = GPIO.PWM(13, 100)    # create an object p for PWM on port 18 at 50 Hertz  
                        # you can have more than one of these, but they need  
                        # different names for each port   
                        # e.g. p1, p2, motor, servo1 etc.  

LastKey = ""

#################################################################
#			Functions		  		#
#################################################################

def Stop():
            p18.start(0)
            p23.start(0)
            p24.start(0)

            p13.start(0)
            p27.start(0)
            p17.start(0)
            time.sleep(0.3)
            #GPIO.cleanup()
            print ("Stop executed")
            #exit()

def Left():
            if LastKey != 'left' : Stop()
            p18.start(60)
            p23.start(0)
            p24.start(100)

            time.sleep(0.4)
            p13.start(60)
            p27.start(0)
            p17.start(100)

#            time.sleep(0.3)
            #Stop()

def Right():
            if LastKey != 'right' : Stop()
            p18.start(60)
            p23.start(100)
            p24.start(0)

            time.sleep(0.4)
            p13.start(60)
            p27.start(100)
            p17.start(0)

#            time.sleep(0.3)
            #Stop()

def Up():
            #if LastKey != 'up' : Stop()
            p18.start(60)
            p23.start(100)
            p24.start(0)

            time.sleep(0.3)
            p13.start(60)
            p27.start(0)
            p17.start(100)

            time.sleep(0.3)
            #Stop()

def Down():
            #if LastKey != 'down' : Stop()
            p18.start(60)
            p23.start(0)
            p24.start(100)

            time.sleep(0.3)
            p13.start(60)
            p27.start(100)
            p17.start(0)

            time.sleep(0.3)
            #Stop()


try:
    while True:
        char = screen.getch()
        print ('you entred')
        print (char)
        if char == ord('q'):
            break
        #elif char == curses.KEY_ENTER:
        elif char == ord(' '):
            # print doesn't work with curses, use addstr instead
            #screen.addstr(0, 0, 'right')
            if not ( LastKey == "enter" ) : print ('Last key was not Enter')
            LastKey="enter"
            print ('enter\n')
            Stop()

        elif char == curses.KEY_RIGHT:
            # print doesn't work with curses, use addstr instead
            #screen.addstr(0, 0, 'right')
            if not ( LastKey == "right" ) : print ('Last key was not right, it was %s \n' % LastKey)
            LastKey="right"
            print ('right\n')
            Right() 
           
        elif char == curses.KEY_LEFT:
            #screen.addstr(0, 0, 'left ')       
            if not ( LastKey == "left" ) : print ('Last key was not left, it was %s \n' % LastKey)
            LastKey="left"
            print ('left\n')
            Left()

        elif char == curses.KEY_UP:
            #screen.addstr(0, 0, 'up   ')       
            if not ( LastKey == "up" ) : print ('Last key was not up, it was %s \n' % LastKey)
            LastKey="up"
            print ('up\n')
            Up()

        elif char == curses.KEY_DOWN:
            #screen.addstr(0, 0, 'down ')
            if not ( LastKey == "down" ) : print ('Last key was not down = %s \n' % LastKey)
            LastKey="down"
            print ('down\n')
            Down()
        else:
            print ('Nothing Entred!\n')

finally:
    # shut down cleanly 
    print ('In the finally section now')
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    p13.stop()                # stop the PWM output
    p17.stop()
    p27.stop()

    p23.stop()                # stop the PWM output
    p24.stop()
    p18.stop()

    GPIO.cleanup()          # when your program exits, tidy up after yours




p13.stop()                # stop the PWM output  
p17.stop()
p27.stop()
  
p23.stop()                # stop the PWM output  
p24.stop()
p18.stop()

GPIO.cleanup()          # when your program exits, tidy up after yours

