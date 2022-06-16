import evdev

print ("Finding PS3 Controller....")
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
	if device.name == 'PLAYSTATION(R)3 Controller':
		ps3dev = device.path
		gamepad = evdev.InputDevice(ps3dev)
	elif device.name == 'PLAYSTATION(R)3 Controller (E0:AE:5E:8B:3F:DF)':
                ps3dev = device.path
                gamepad = evdev.InputDevice(ps3dev)
print (gamepad)

def scale(val, src, dst):
	return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

def scale_stick(value):
	return scale(value,(0,255),(0,200))

for event in gamepad.read_loop():
	if event.type == 3:
#		if event.code == 0:
#			print ("Left X-Axis")
#			print (round(scale_stick(event.value),2))
		if event.code == 1:
			print ("Left Y-Axis")
			print (round(scale_stick(event.value),2))
#		if event.code == 2:
#			print ("Right X-Axis")
#			print (round(scale_stick(event.value),2))
		if event.code == 3:
			print ("Right Y-Axis")
			print (round(scale_stick(event.value),2))
	if event.type == 1 and event.value == 1:
		if event.code == 291:
			print ("Exiting Joystick Loop")
			running = False
			break
#	if event.type == 3:
#		print ("Event Type ", event.type)
#		print ("Event Code ", event.code)
#		print ("Event Value ", event.value)
#		print ("/n")
