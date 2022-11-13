from random import randrange
from turtle import right
import numpy as np
import cv2
import subprocess
import sys
from moviepy.editor import *
from random import randrange
start = 0

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    length = 60
    #trim video and save to vOutput as cutInput.mp4
    inputFile = str("vInput/input9.mp4")

    command = ("ffmpeg -ss %d -i %s -t %g -c copy vOutput/tmp/cutInput.mp4 -y" % (start, inputFile, length))

    subprocess.call(command, shell=True)

    # Open cutINput.mp4
    cap = cv2.VideoCapture('vOutput/tmp/cutInput.mp4')

    # Initialize frame counter
    cnt = 0
    # Some characteristics from the original video
    w_frame, h_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps, frames = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)

    print (str(cv2.CAP_PROP_FRAME_COUNT))


    w = 960
    h = 1080

    # output
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('vOutput/tmp/crop.mp4', fourcc, fps, (w, h))
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        ENDC = '\033[0m'
    # Now we start
    while(cap.isOpened()):
        ret, frame = cap.read()

        cnt += 1 # Counting frames

        # Avoid problems when video finish
        if ret==True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=1,
                minSize=(20, 20),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            for (x, y, w, h) in faces:
                    #720 x 360
                x2,y2,h2,w2 = (x+500),0,720,380
                x3,y3,h3,w3 = (x+500),0,720,380
                print(bcolors.OKGREEN + 'face found at %d' % x)

            else:
                x2,y2,h2,w2 = 240,0,720,380
                x3,y3,h3,w3 = 240,0,720,380
            # Croping the frame
            cropfr = frame[y2:y2+h2, x2:x2+w2]

            # Percentage
            xx = cnt *100/frames

            command = ("clear")
            subprocess.call(command, shell=True)
            print(bcolors.OKGREEN + 'cropping %d...' % (start))
            print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            print(bcolors.OKGREEN + str(int(xx)),'%' + bcolors.ENDC, end='\r')

            # Saving from the desired frames
            #if 15 <= cnt <= 90:
            #    out.write(crop_frame)

            # I see the answer now. Here you save all the video
            out.write(cropfr)

            # Just to see the video in real time          

        else:
            break


    cap.release()
    out.release()


    cv2.destroyAllWindows()

    # split Cropped files further
    #command = ("ffmpeg -ss %d -i vOutput/tmp/crop.mp4 -t %f -c copy vOutput/tmp/right2.mp4 -y" % (0, 2.5))
    
    #subprocess.call(command, shell=True)
   

    #get audio from cutInput.mp4 with moviepy   
    original = VideoFileClip("vOutput/tmp/cutInput.mp4")
    audioclip = original.audio
    audioclip.write_audiofile("vOutput/tmp/audio.mp3")
    clip_1 = VideoFileClip("vOutput/tmp/crop.mp4")
    
    #final_clip_notext = concatenate_videoclips([clip_1,clip_2,clip_3,clip_4,clip_5,clip_6,clip_7,clip_8,clip_9,clip_10,clip_11,clip_12,clip_13,clip_14,clip_15,clip_16,clip_17,clip_18,clip_19,clip_20,clip_21,clip_22,clip_23,clip_24])

    title = ImageClip("vInput/overlays/nathanfielder.png").set_start(0).set_duration(2.3).set_pos(("center","center"))
            #.resize(height=50) # if you need to resize...
            

    final_clip = CompositeVideoClip([clip_1, title])
    final_clip.write_videofile("vOutput/tmp/finalVideo.mp4")

    command41 = ("ffmpeg  -i vOutput/tmp/finalVideo.mp4 -i vOutput/tmp/audio.mp3 -map 0 -map 1 -c copy vOutput/tmp/ffinalVideo%d.mp4 -y && ffmpeg -i vOutput/tmp/ffinalVideo%d.mp4 -c:v copy vOutput/final/finalVideo%d.mp4" % (start, start, start) )


    subprocess.call(command41, shell=True)
    start += 60



