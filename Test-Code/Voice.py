#Imports
import random
import pyaudio
import wave
import sys
import os

#Announcer_cwd = os.getcwd()+"Voice-Lines/Announcer" #Get the current directory of the program, use for 'realative' paths
#Turret_cwd = os.getcwd()+"Voice-Lines/Turret"

Announcer_cwd = "/home/riley/GitHub/portal2-turret/Voice-Lines/Announcer/"

Voice = {
    "Announcer": ["INIT"],
    "Turret": ["INIT"]
    } #Dictionary containing all requirements for voice lines, init to some value

#Append list inside dict for Announcer
for (dirpath, dirnames, filenames) in os.walk(Announcer_cwd):
    Voice.update(Announcer = Voice["Announcer"] + filenames)

print(Voice)
print("\n\n")

print(Voice["Announcer"][5])
