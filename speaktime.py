#!/usr/bin/env python3

import time
import pyttsx3

#ctime gives time in the format 'Day Month Date hh:mm:ss year'
fullTime = time.ctime().split()[3] #This selects the hh:mm:ss
fullTime = fullTime[:5] #This selects the hh:mm

text = "The time is " + fullTime #This is our line to speak out

engine = pyttsx3.init() #Initialises our tts engine
engine.setProperty('rate', 150) #sets the speed of the speech
engine.say(text)
engine.runAndWait() #This calls out the time
