import os
import time
import json
from datetime import datetime
import requests
import OPi.GPIO as GPIO

def main():
	alarm = False
	token = "..." #https://api.ukrainealarm.com/
	AL_msg = "/usr/AL_main.mp3"
	OK_msg = "/usr/OK.mp3"
	test_msg = "/usr/morningTest50.mp3"

	#GPIO settings
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	green_led = <some pin>	#RUN indication
	mic = <some pin>	#Vellez "MIC" button simulation
	siren_on = <some pin>	#Siren ON relay
	siren_off = <some pin>	#Siren OFF relay
	outs = [green_led, mic, siren_on, siren_off]
	GPIO.setup(outs, GPIO.OUT)

	while True:
		click(green_led)	#
		time.sleep(5)		#
		click(green_led)	#
		time.sleep(4)		#Green LED blinks to indicate RUN
		
		#if time for everyday test
		now = datetime.now()
		timeNow = now.strftime("%H:%M")
		if timeNow == '08:00':
			playSound(mic, test_msg)
			time.sleep(60)		#wait for 1 minute
		
		#ask if alert
		try:
			r=requests.get("https://api.ukrainealarm.com/api/v3/alerts/31", 
				headers={"Authorization":token, "accept": "application/json"})
			r_dict = r.json()
			region = (r_dict[0]['regionName'])
			try:
				alert = (r_dict[0]['activeAlerts'][0]['type'])
			except Exception as e:
				alert = 'none'
		except Exception as e:
			region = 'No response from remote server'
			alert = 'unavailable'
	
		print (region, '-', alert)
	
		#set output
		if alert == 'AIR':
			if alarm == False:
				alarm = True
				playSound(mic, AL_msg)
				click(siren_on)		#outer siren starts
				time.sleep(60)		#for 1 minute
				click(siren_off)	#outer siren stops
		else:
			if alarm == True and alert == 'none':
				alarm = False
				playSound(mic, OK_msg)

def playSound(pin, message):
	click(pin)			#"MIC" button ON
	time.sleep(4)			#amplifier needs time to start
	os.system("mpg123 " + message)	#playing sound using native player
	time.sleep(1)
	click(pin)			#"MIC" button OFF

def click(pin):
	"""Emulate button click."""
	GPIO.output(pin, 1)
	time.sleep(0.5)
	GPIO.output(pin, 0)

GPIO.cleanup()

if __name__ == '__main__':
	main()
