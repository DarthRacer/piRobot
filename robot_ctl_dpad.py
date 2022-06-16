

#dual motor robot control from PlayStation3 Controller

#Import modules for GPIO, time, and evdev
import RPi.GPIO as GPIO
import time
import curses
import os
import evdev

#Define controller input path
print ("Finding PS3 Controller....")
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
	if device.name == 'PLAYSTATION(R)3 Controller (E0:AE:5E:8B:3F:DF)':
		ps3dev = device.path
		gamepad = evdev.InputDevice(ps3dev)
print (gamepad)

#gamepad = evdev.InputDevice('/dev/input/event0')

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

#Display user instructions, controller info, and pause
os.system('clear')
print (gamepad)
print("\n")
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("\n")
print("D-Pad_UP = forward, D-Pad_DOWN = backward, R2 = turn_right, L2 = turn_left")
print("\n")
print("L1 = low_speed, R1 = medium_speed, D-PAD_RIGHT = high_speed, START = 'Exit Robot Control'")
print("\n")
input ("Starting Robot. Press Enter to begin.")

#Begin loop to grab input from controller
#Convert to robot movements
for event in gamepad.read_loop():
	if event.type == evdev.ecodes.EV_KEY:
		keyevent = (evdev.categorize(event))
		if keyevent.keystate == keyevent.key_down:
			if keyevent.keycode == 'BTN_TOP2':
				print ("forward")
				GPIO.output(in1,GPIO.HIGH)
				GPIO.output(in2,GPIO.LOW)
				GPIO.output(in3,GPIO.HIGH)
				GPIO.output(in4,GPIO.LOW)
			elif keyevent.keycode == 'BTN_BASE':
				print ("backward")
				GPIO.output(in1,GPIO.LOW)
				GPIO.output(in2,GPIO.HIGH)
				GPIO.output(in3,GPIO.LOW)
				GPIO.output(in4,GPIO.HIGH)
			elif keyevent.keycode == 'BTN_BASE3':
				print ("left")
				GPIO.output(in1,GPIO.LOW)
				GPIO.output(in2,GPIO.HIGH)
				GPIO.output(in3,GPIO.HIGH)
				GPIO.output(in4,GPIO.LOW)
			elif keyevent.keycode == 'BTN_BASE4':
				print ("right")
				GPIO.output(in1,GPIO.HIGH)
				GPIO.output(in2,GPIO.LOW)
				GPIO.output(in3,GPIO.LOW)
				GPIO.output(in4,GPIO.HIGH)
			elif keyevent.keycode == 'BTN_BASE5':
				print ("low speed")
				pa.ChangeDutyCycle(40)
				pb.ChangeDutyCycle(40)
			elif keyevent.keycode == 'BTN_BASE6':
				print ("medium speed")
				pa.ChangeDutyCycle(65)
				pb.ChangeDutyCycle(65)
			elif keyevent.keycode == 'BTN_PINKIE':
				print ("high speed")
				pa.ChangeDutyCycle(90)
				pb.ChangeDutyCycle(90)
			elif keyevent.keycode == 'BTN_TOP':
				print ("Exiting Robot Control Script")
				break
		if keyevent.keystate == keyevent.key_up:
			print ("Robot Stop")
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.LOW)

#Shut down GPIO cleanly
pa.stop()
pb.stop()
GPIO.cleanup()
