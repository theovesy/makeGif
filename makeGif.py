#!/usr/bin/python3

#   makeGIF by Theo Vesy    ###############
#
#   makes a gif with every image of a given format in alphabetical order from the folder
#   arguments : name (without .gif extension), duration (duration of each image), format (png, jpg, format of the frames)
#

from PIL import Image
import glob
import sys

def getArgs():
    arg = sys.argv
    return arg[1], int(arg[2]), arg[3]

def getFrames(format):
    frames = []
    images = glob.glob(f"*.{format}")
    images.sort()
    for i in images:
        new_frame = Image.open(i)
        frames.append(new_frame)

    return frames

def saveGif(name, duration, format):
    frames = getFrames(format)
    frames[0].save(f"{name}.gif", format='GIF', append_images=frames[1:], save_all=True, duration=duration, loop=0)
    print(f"{len(frames)} frames successfuly compiled as {name}.gif !")

name, duration, format = getArgs()
saveGif(name, duration, format)


