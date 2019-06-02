## TODO:
## 1. Finish reading up on what the code does, finish writing the code, and make notes on how this code works.
## 2. Add in code to keep track of the average time it takes to capture, recognise, and then display the image. (Use cmd arguments to put into 'time test mode' vs debugging)
## 3. Add code to see how much resourses this operation takes (part of debug mode, write this code into Utillities.py)
## 4. Compare this time to the 'faster' code in the examples (export to file for use in excel?)
## 5. A more elegent way to load the yaml file (make a class based off whats in the file)

print(
'''
A simple face recognition program heavely based off of examples provided in
the face_recognition repository:
    https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam.py

This program is ment to test the preformance on a raspberry pi which is to be
used as a part of the Portal 2 Turret project.

Author: Riley Larche (Program Counter)
Date Created: 2019-05-11
Date Updated: 2019-05-26

Python Version: 3.7.2
Atom 1.37

'''
)


#
#Import Modules
import face_recognition as FR
import numpy as np
import Utillities as U
import time
import picamera
import os
import yaml

#
#Global variables
CWD = U.GetCWD()


#
#Classes
class FRVars:
    name = []
    path = []
    images = []
    encodings = []
    locations = []

class Timed:
    start_time = 0
    end_time = 0

    def start:
        start_time = time.time()
    def stop:
        end_time = time.time() - start_time


#
#Functions
def PullPredefined(class_local, data_local):
    print("[INFO] Pulling known faces from config file.")
    try:
        class_local.name = data_local.Known.names
        class_local.path = data_local.Known.images

        count = 0
        for x in class_local.path:
            class_local.images = face_recognition.load_image(x)
            class_local.encodings = face_recognition.face_encodings(CWD + class_local.images[count])
            count ++
    except Exception as e:
        U.Error(e)

    if input("[USER] Do you wish to encode new faces using the camera now? y/n "):
        #Import or camera
        LoadNewFace()

    return class_local, data_local

def LoadNewFace():
    name = input("[USER] What is the name of this face? ")
    print("[INFO] Taking image to load into known faces.")
    for num in range(1, 2):
        print("[INFO] {countdown}...".format(countdown=num))
        sleep(0.5)
    #take image with picam and give it the filename of name

#
#Setup
T = Timed
T.start()

try:
    print("[INFO] Setting up the Raspberry Pi camera.")
    camera = picamera.PiCamera()
    camera.resolution(1920, 1080)
    output = np.empty((1080, 1920, 3), dtype = np.uint8)    #np.empty(shape[int or tuple], datatype[data type for output array])

except Exception as e:
    U.Error(e)

#Setup variables and load data
print("[INFO] Finishing setup and gathering data.")
stream = file("Data.yaml", "r")
data = yaml.load(stream)
stream.close()

Known = FRVars
Current = FRVars
Known, data = PullPredefined(Known, data)`

T.stop()
print("[Time] Setup took: {sec}s".format(sec=T.end_time))

#
#main program loop
try:
    while True:
        T.start()
        print("[INFO] Entering main loop.")
        #Grab newest fram from webcam
        ret, frame = video_capture.read()

        #Find all faces within the frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        #Loop through each face found
        for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            print("[Face Recognition] Coordinates of found face: Top:{t} Right:{r} Bottom:{b} Left:{l}".format(t=top, r=right, b=bottom, l=left))
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                print("[Face Recognition] Found a match for {n}.\n".format(n=name))

            print("[Face Recognition] Unable to find a macth. Person {n}\n".format(n=name))

            T.stop()
            print("[Time] Single loop took: {sec}s".format(sec=T.end_time))


except KeyboardInterrupt:
    print("[KEY] Terminating...")
    #Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

    stream = file("Data.yaml", "w")
    yaml.dump(data, stream)
