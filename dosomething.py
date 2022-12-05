import os
import time
import OPi.GPIO as GPIO

AL_msg = "/usr/AL_main.mp3"
OK_msg = "/usr/OK.mp3"
test_msg = "/usr/test.mp3"

def action(num):
	#GPIO settings
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)

	mic = <some pin>		#Vellez "MIC" button simulation
	siren_on = <some pin>	#siren ON relay
	siren_off = <some pin>	#siren OFF relay
	outs = [mic, siren_on, siren_off]
	GPIO.setup(outs, GPIO.OUT)


	if num == 1:
		print('Action -', num)
		playSound(mic, test_msg),
	elif num == 2:
		print('Action -', num)
		playSound(mic, test_msg)
	elif num == 3:
		print(num, 'Siren ON')
		GPIO.output(siren_on, 1)
		time.sleep(1)
		GPIO.output(siren_on, 0)
		GPIO.cleanup()
	elif num == 4:
		print(num, 'Siren OFF')
		GPIO.output(siren_off, 1)
		time.sleep(1)
		GPIO.output(siren_off, 0)
		GPIO.cleanup()

def playSound(mic, message):
	GPIO.output(mic, 1)
	time.sleep(0.5)
	GPIO.output(mic, 0) #"MIC" button ON
	time.sleep(4)
	os.system("mpg123 " + message)	#playing sound using native player
	time.sleep(1)
	GPIO.output(mic, 1)
	time.sleep(0.5)
	GPIO.output(mic, 0)	#"MIC" button OFF
	GPIO.cleanup()

GPIO.cleanup()
