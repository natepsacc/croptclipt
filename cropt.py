from random import randrange
from turtle import right
import numpy as np
import cv2
import subprocess
import sys
from moviepy.editor import *
from random import randrange
start = int(sys.argv[1])
length = int(sys.argv[2])
#trim video and save to vOutput as cutInput.mp4
command = ("ffmpeg -ss %d -i vInput/input.mp4 -t %f -c copy vOutput/tmp/cutInput.mp4 -y" % (start, length))

subprocess.call(command, shell=True)


# Open cutINput.mp4
cap = cv2.VideoCapture('vOutput/tmp/cutInput.mp4')

# Initialize frame counter
cnt = 0

# Some characteristics from the original video
w_frame, h_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps, frames = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)

print (str(cv2.CAP_PROP_FRAME_COUNT))

# Here you can define your croping values
left=0
right=960
side=right
x,y,h,w = randrange(300,420),0,1014,720
x2,y2,h2,w2 = randrange(440,910),0,1014,720

# output
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('vOutput/tmp/right.mp4', fourcc, fps, (w, h))
out2 = cv2.VideoWriter('vOutput/tmp/left.mp4', fourcc, fps, (w, h))
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
        # Croping the frame
        cropLeft = frame[y:y+h, x:x+w]
        cropRight = frame[y2:y2+h2, x2:x2+w2]

        # Percentage
        xx = cnt *100/frames

        command = ("clear")
        subprocess.call(command, shell=True)
        print(bcolors.OKGREEN + str(int(xx)),'%' + bcolors.ENDC, end='\r')

        # Saving from the desired frames
        #if 15 <= cnt <= 90:
        #    out.write(crop_frame)

        # I see the answer now. Here you save all the video
        out.write(cropRight)
        out2.write(cropLeft)

        # Just to see the video in real time          

    else:
        break


cap.release()
out.release()
out2.release()


cv2.destroyAllWindows()

# split Cropped files further
command = ("ffmpeg -ss %d -i vOutput/tmp/right.mp4 -t %f -c copy vOutput/tmp/right2.mp4 -y" % (0, 2.5))
command1 = ("ffmpeg -ss %d -i vOutput/tmp/left.mp4 -t %f -c copy vOutput/tmp/left2.mp4 -y" % (2.5, 2.5))
command2 = ("ffmpeg -ss %d -i vOutput/tmp/right.mp4 -t %f -c copy vOutput/tmp/right3.mp4 -y" % (5, 2.5))
command3 = ("ffmpeg -ss %d -i vOutput/tmp/left.mp4 -t %f -c copy vOutput/tmp/left3.mp4 -y" % (7.5, 2.5))
command4 = ("ffmpeg -ss %d -i vOutput/tmp/right.mp4 -t %f -c copy vOutput/tmp/right4.mp4 -y" % (10, 2.5))
command5 = ("ffmpeg -ss %d -i vOutput/tmp/left.mp4 -t %f -c copy vOutput/tmp/left4.mp4 -y" % (12.5, 2.5))
command6 = ("ffmpeg -ss %d -i vOutput/tmp/right.mp4 -t %f -c copy vOutput/tmp/right5.mp4 -y" % (15, 2.5))
command7 = ("ffmpeg -ss %d -i vOutput/tmp/left.mp4 -t %f -c copy vOutput/tmp/left5.mp4 -y" % (17.5, 2.5))
command8 = ("ffmpeg -ss %d -i vOutput/tmp/right.mp4 -t %f -c copy vOutput/tmp/right6.mp4 -y" % (20, 2.5))
command9 = ("ffmpeg -ss %d -i vOutput/tmp/left.mp4 -t %f -c copy vOutput/tmp/left6.mp4 -y" % (22.5, 2.5))
command10 = ("ffmpeg -ss %d -i vOutput/tmp/right.mp4 -t %f -c copy vOutput/tmp/right7.mp4 -y" % (25, 2.5))
command11 = ("ffmpeg -ss %d -i vOutput/tmp/left.mp4 -t %f -c copy vOutput/tmp/left7.mp4 -y" % (27.5, 2.5))
command12 = ("ffmpeg -ss %d -i vOutput/tmp/right.mp4 -t %f -c copy vOutput/tmp/right8.mp4 -y" % (30, 2.5))
command13 = ("ffmpeg -ss %d -i vOutput/tmp/left.mp4 -t %f -c copy vOutput/tmp/left8.mp4 -y" % (32.5, 2.5))
command14 = ("ffmpeg -ss %d -i vOutput/tmp/right.mp4 -t %f -c copy vOutput/tmp/right9.mp4 -y" % (35, 2.5))
command15 = ("ffmpeg -ss %d -i vOutput/tmp/left.mp4 -t %f -c copy vOutput/tmp/left9.mp4 -y" % (37.5, 2.5))
command16 = ("ffmpeg -ss %d -i vOutput/tmp/right.mp4 -t %f -c copy vOutput/tmp/right10.mp4 -y" % (40, 2.5))
command17 = ("ffmpeg -ss %d -i vOutput/tmp/left.mp4 -t %f -c copy vOutput/tmp/left10.mp4 -y" % (42.5, 2.5))
command18 = ("ffmpeg -ss %d -i vOutput/tmp/right.mp4 -t %f -c copy vOutput/tmp/right11.mp4 -y" % (45, 2.5))
command19 = ("ffmpeg -ss %d -i vOutput/tmp/left.mp4 -t %f -c copy vOutput/tmp/left11.mp4 -y" % (47.5, 2.5))
command20 = ("ffmpeg -ss %d -i vOutput/tmp/right.mp4 -t %f -c copy vOutput/tmp/right12.mp4 -y" % (50, 2.5))
command21 = ("ffmpeg -ss %d -i vOutput/tmp/left.mp4 -t %f -c copy vOutput/tmp/left12.mp4 -y" % (52.5, 2.5))
command22 = ("ffmpeg -ss %d -i vOutput/tmp/right.mp4 -t %f -c copy vOutput/tmp/right13.mp4 -y" % (55, 2.5))
command23 = ("ffmpeg -ss %d -i vOutput/tmp/left.mp4 -t %f -c copy vOutput/tmp/left13.mp4 -y" % (57.5, 2.5))

subprocess.call(command, shell=True)
subprocess.call(command1, shell=True)
subprocess.call(command2, shell=True)
subprocess.call(command3, shell=True)
subprocess.call(command4, shell=True)
subprocess.call(command5, shell=True)
subprocess.call(command6, shell=True)
subprocess.call(command7, shell=True)
subprocess.call(command8, shell=True)
subprocess.call(command9, shell=True)
subprocess.call(command10, shell=True)
subprocess.call(command11, shell=True)
subprocess.call(command12, shell=True)
subprocess.call(command13, shell=True)
subprocess.call(command14, shell=True)
subprocess.call(command15, shell=True)
subprocess.call(command16, shell=True)
subprocess.call(command17, shell=True)
subprocess.call(command18, shell=True)
subprocess.call(command19, shell=True)
subprocess.call(command20, shell=True)
subprocess.call(command21, shell=True)
subprocess.call(command22, shell=True)
subprocess.call(command23, shell=True)

#get audio from cutInput.mp4 with moviepy   
original = VideoFileClip("vOutput/tmp/cutInput.mp4")
audioclip = original.audio
audioclip.write_audiofile("vOutput/tmp/audio.mp3")
clip_1 = VideoFileClip("vOutput/tmp/right2.mp4")
clip_2 = VideoFileClip("vOutput/tmp/left2.mp4")
clip_3 = VideoFileClip("vOutput/tmp/right3.mp4")
clip_4 = VideoFileClip("vOutput/tmp/left3.mp4")
clip_5 = VideoFileClip("vOutput/tmp/right4.mp4")
clip_6 = VideoFileClip("vOutput/tmp/left4.mp4")
clip_7 = VideoFileClip("vOutput/tmp/right5.mp4")
clip_8 = VideoFileClip("vOutput/tmp/left5.mp4")
clip_9 = VideoFileClip("vOutput/tmp/right6.mp4")
clip_10 = VideoFileClip("vOutput/tmp/left6.mp4")
clip_11 = VideoFileClip("vOutput/tmp/right7.mp4")
clip_12 = VideoFileClip("vOutput/tmp/left7.mp4")
clip_13 = VideoFileClip("vOutput/tmp/right8.mp4")
clip_14 = VideoFileClip("vOutput/tmp/left8.mp4")
clip_15 = VideoFileClip("vOutput/tmp/right9.mp4")
clip_16 = VideoFileClip("vOutput/tmp/left9.mp4")
clip_17 = VideoFileClip("vOutput/tmp/right10.mp4")
clip_18 = VideoFileClip("vOutput/tmp/left10.mp4")
clip_19 = VideoFileClip("vOutput/tmp/right11.mp4")
clip_20 = VideoFileClip("vOutput/tmp/left11.mp4")
clip_21 = VideoFileClip("vOutput/tmp/right12.mp4")
clip_22 = VideoFileClip("vOutput/tmp/left12.mp4")
clip_23 = VideoFileClip("vOutput/tmp/right13.mp4")
clip_24 = VideoFileClip("vOutput/tmp/left13.mp4")
final_clip = concatenate_videoclips([clip_1,clip_2,clip_3,clip_4,clip_5,clip_6,clip_7,clip_8,clip_9,clip_10,clip_11,clip_12,clip_13,clip_14,clip_15,clip_16,clip_17,clip_18,clip_19,clip_20,clip_21,clip_22,clip_23,clip_24])


final_clip.write_videofile("vOutput/tmp/finalVideo.mp4")
print(bcolors.OKGREEN)
command41 = ("ffmpeg  -i vOutput/tmp/finalVideo.mp4 -i vOutput/tmp/audio.mp3 -map 0 -map 1 -c copy vOutput/tmp/ffinalVideo%d.mp4 -y && ffmpeg -i vOutput/tmp/ffinalVideo%d.mp4 -c:v copy vOutput/finalVideo%d.mp4" % (start, start, start) )
print(bcolors.ENDC)

subprocess.call(command41, shell=True)




