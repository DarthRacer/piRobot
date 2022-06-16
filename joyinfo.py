import evdev
gamepad = evdev.InputDevice('/dev/input/event0')
print (gamepad)
print ()
print ("Capabilities")
print (gamepad.capabilities())
print ("Capabilites Verbose Mode")
print (gamepad.capabilities(verbose=True))
for event in  gamepad.read_loop():
	if event.type == evdev.ecodes.EV_KEY:
		print (evdev.categorize(event))
	else:
		print ("Not a Button")
