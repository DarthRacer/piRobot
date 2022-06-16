

#dual motor tank robot control from PlayStation3 Controller

#Import modules for GPIO, time, and evdev
import RPi.GPIO as GPIO
import time
import curses
import os
import evdev

#Define controller input path
#gamepad = evdev.InputDevice('/dev/input/event0')
print ("Finding PS3 Controller....")
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
	if device.name == 'PLAYSTATION(R)3 Controller (E0:AE:5E:8B:3F:DF)':
		ps3dev = device.path
		gamepad = evdev.InputDevice(ps3dev)

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

# ***** Motor Control Functions *****
# Motor Stop
def MotorStop():
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)
# Motor Slow Speed
def MotorSlow():
	pa.ChangeDutyCycle(50)
	pb.ChangeDutyCycle(50)
# Motor Medium Speed
def MotorMed():
	pa.ChangeDutyCycle(80)
	pb.ChangeDutyCycle(80)
# Motor High Speed
def MotorHigh():
	pa.ChangeDutyCycle(100)
	pb.ChangeDutyCycle(100)
# Left Drive Forward
def LeftDrvFwd():
	GPIO.output(in3,GPIO.HIGH)
	GPIO.output(in4,GPIO.LOW)
# Left Drive Reverse
def LeftDrvRev():
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.HIGH)
# Right Drive Forward
def RightDrvFwd():
	GPIO.output(in1,GPIO.HIGH)
	GPIO.output(in2,GPIO.LOW)
# Right Drive Reverse
def RightDrvRev():
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.HIGH)



#Display user instructions, controller info, and pause
os.system('clear')
print (gamepad)
print("\n")
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("\n")
print("L2 = Left Drive FWD, R2 = Right Drive FWD, L2 = Left Drive Reverse, R2 = Right Drive Reverse")
print("\n")
print("D-PAD_Left = low_speed, D-Pad_Right = medium_speed, D-PAD_UP = high_speed, START = 'Exit Robot Control'")
print("\n")
#input ("Starting Robot. Press Enter to begin.")

#Begin loop to grab input from controller
#Convert to robot movements
for event in gamepad.read_loop():
	if event.type == evdev.ecodes.EV_KEY:
		keyevent = (evdev.categorize(event))
		if keyevent.keystate == keyevent.key_down:
			if keyevent.keycode == 'BTN_BASE3':
				print ("left drive forward")
				LeftDrvFwd()
			elif keyevent.keycode == 'BTN_BASE4':
				print ("right drive forward")
				RightDrvFwd()
			elif keyevent.keycode == 'BTN_BASE6':
				print ("right drive reverse")
				RightDrvRev()
			elif keyevent.keycode == 'BTN_BASE5':
				print ("left drive reverse")
				LeftDrvRev()
			elif keyevent.keycode == 'BTN_BASE2':
				print ("low speed")
				MotorSlow()
			elif keyevent.keycode == 'BTN_PINKIE':
				print ("medium speed")
				MotorMed()
			elif keyevent.keycode == 'BTN_TOP2':
				print ("high speed")
				MotorHigh()
			elif keyevent.keycode == 'BTN_TOP':
				print ("Exiting Robot Control Script")
				break
		if keyevent.keystate == keyevent.key_up:
			print ("Robot Stop")
			MotorStop()

#Shut down GPIO cleanly
pa.stop()
pb.stop()
GPIO.cleanup()
