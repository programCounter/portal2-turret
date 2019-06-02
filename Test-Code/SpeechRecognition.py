'''
Test file for offline speech detection using Sphinx.
'''

#File Imports
import speech_recognition as SR
import pyaudio
import time

audio_dev = 3

print('''
||||SpeechRecognition.py test file
||||Written by: Riley Larche using reference:
||||https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
||||\n\n\n
''')

print("Looking for audio devices...\n")
p = pyaudio.PyAudio()
if p.get_device_count():
    print("Found Devices:")
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print(info['index'], info['name'])
    print("\n\n")

#Obtain Audio
while True:
    print("Starting Recognition...\n")
    r = SR.Recognizer()
    with SR.Microphone(device_index = 3) as source:
        print("Ready. Say something!\n")
        audio = r.listen(source)

    #Recognize Audio
    try:
        print("Sphinx recognized: " + r.recognize_sphinx(audio) + "\n\n")
    except:
        print("There was an error!\n")
        print("Please try again!\n\n")
