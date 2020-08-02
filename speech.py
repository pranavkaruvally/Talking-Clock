import time
import pyttsx3

#ctime gives time in the format 'Day Month Date hh:mm:ss year'
fullTime = time.split()[3] #This selects the hh:mm:ss
fullTime = fullTime[:5] #This selects the hh:mm
