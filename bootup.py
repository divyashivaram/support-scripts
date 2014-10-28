'''
Script to run a terminal based alarm clock that 
pings, shows a dialog box and plays a song when the alarm ticks off.
'''

import time
from time import sleep
from pygame import mixer
import easygui
import sys

def alarm():
	print "WAAAKE UP!!!!"
	mixer.init()
	mixer.music.load('/home/divya/Music/pink')
	mixer.music.play()

def stopwatch():
	minutes = int(input("Countdown from:"))
	ticker = minutes * 60
	while ticker > 0:
		time.sleep(1)
		print(ticker)
		ticker -= 1
		alarm()
	# print("TIME'S UP!!!!")

def alarm_clock():

	hours = float(easygui.enterbox(msg='Please enter the hours: 0 to 23', title='Hours', default='23'))

	if hours < 0 or hours > 23:
		print "Invalid value for hours, should be >= 0 or <=23"
		sys.exit(1)

	minutes = float(easygui.enterbox(msg='Please enter the minutes: 0 to 60', title='Minutes', default='59'))

	if minutes < 0 or minutes > 59:
		print "Invalid value for minutes, should be >= 0 or <=59"
		sys.exit(1)

	now_hour = time.strftime("%H")
	now_min = time.strftime("%M")
	now_sec = time.strftime("%S")

	if float(now_hour) != hours or float(now_min) != minutes:
		min_hours = (hours - float(now_hour))
		min_mins = minutes - float(now_min)
		total = (min_hours*60) + min_mins
		sec = (total * 60) - float(now_sec)

		if min_mins == 1:
			unit_word = "minute"
		else:
			unit_word = "minutes"
	
		if total > 0:
			if total < 60:
				print "Sleeping for", int(total), unit_word
			else:
				print "Sleeping for", int(min_hours), "hours and", int(min_mins), unit_word
			sleep(sec)
			alarm()
			msg = "Click \"Continue\" to snooze for 10 minutes"
			title = "J.A.R.V.I.S"
			if easygui.ccbox(msg, title):
				print "Snoozing for 10 minutes"
				mixer.music.stop()
				sleep(600)
				alarm()
			else:
				for i in range(5):
					print "Alarm ringing!!", chr(7)
					sleep(1)

if __name__ == '__main__':
	msg     = "Pick an option"
	title   = "Alarm/Stopwatch"
	choices = ["Alarmclock", "Stopwatch"]
	choice   = easygui.choicebox(msg, title, choices)
	if choice == "Alarmclock":
		alarm_clock()
	elif choice == "Stopwatch":
		stopwatch()