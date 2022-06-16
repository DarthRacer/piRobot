import  evdev
gamepad = evdev.InputDevice('/dev/input/event0')
print (gamepad)
for event in gamepad.read_loop():
	if event.type == evdev.ecodes.EV_KEY:
		print (evdev.categorize(event))
#	else:
#		print ("Not a Button")
