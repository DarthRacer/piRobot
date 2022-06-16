

#dual motor robot control from keyboard

#Import modules for GPIO, time, and curses (keyboard)
import RPi.GPIO as GPIO
import time
import curses
import os

#Define Motor Controller Pins
in1 = 24
in2 = 23
ena = 25
in3 = 27
in4 = 17
enb = 22

#Set GPIO parameters and output pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)

#Set initial starting parameters
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

pa=GPIO.PWM(ena,1000)
pb=GPIO.PWM(enb,1000)
pa.start(40)
pb.start(40)

#Display user instructions and pause
os.system('clear')
print("\n")
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("\n")
print("Up_Arrow = forward	Down_Arrow = backward	Right_Arrow = turn_right	Left_Arrow = turn_left")
print("\n")
print("l = low_speed	m = medium_speed	h = high_speed		s = stop 	x = exit")
print("\n")
input ("Starting Robot. Press Enter to begin.")

# Get curses window, turn off echoing to screen
#turn on instant no wat response,
#and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

#Begin loop to grab input from keyboard
#Convert to robot movements
try:
	while True:
		char = screen.getch()
		if char == ord('x'):
			break
		elif char == curses.KEY_UP:
			print ("forward")
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in4,GPIO.LOW)
		elif char == curses.KEY_DOWN:
			print ("backward")
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.HIGH)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.HIGH)
		elif char == curses.KEY_LEFT:
			print ("left")
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.HIGH)
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in4,GPIO.LOW)
		elif char == curses.KEY_RIGHT:
			print ("right")
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.HIGH)
		elif char == ord('s'):
			print ("stop")
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.LOW)
		elif char == ord('l'):
			print ("low speed")
			pa.ChangeDutyCycle(40)
			pb.ChangeDutyCycle(40)
		elif char == ord('m'):
			print ("medium speed")
			pa.ChangeDutyCycle(65)
			pb.ChangeDutyCycle(65)
		elif char == ord('h'):
			print ("high speed")
			pa.ChangeDutyCycle(90)
			pb.ChangeDutyCycle(90)
		else:
			print("<<<  wrong data  >>>")
			print("please enter the defined data to continue.....")
finally:
	#Close down curses properly, including
	#turning echo back on
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()

#Shut down GPIO cleanly
pa.stop()
pb.stop()
GPIO.cleanup()
