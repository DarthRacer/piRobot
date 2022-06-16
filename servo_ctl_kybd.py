#Import modules for GPIO, time, and curses (keyboard)
import RPi.GPIO as GPIO
import time
import curses

#Set GPIO parameters and output pin
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

#Set starting position and servo PWM
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(7.5) # Initialization
cdc = 7.5

# Get curses window, turn off echoing to screen
#turn on instant no wat response,
#and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
	while True:
		char = screen.getch()
		if char == ord('q'):
			break
		elif char == curses.KEY_LEFT:
			print ("left")
			cdc+=1.25
			if cdc > 12.5:
				cdc = 12.5
			print (cdc)
			p.ChangeDutyCycle(cdc)
		elif char == curses.KEY_RIGHT:
			print ("right")
			cdc-=1.25
			if cdc < 2.5:
				cdc = 2.5
			print (cdc)
			p.ChangeDutyCycle(cdc)
		elif char == curses.KEY_UP:
			print ("center")
			cdc = 7.5
			print (cdc)
			p.ChangeDutyCycle(cdc)
finally:
#Close down curses properly, including
#turning echo back on
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()

#Shut down GPIO cleanly
p.stop()
GPIO.cleanup()
