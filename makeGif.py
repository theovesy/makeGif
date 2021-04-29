#!/usr/bin/python3

#   makeGIF by Theo Vesy    ###############
#
#   makes a gif with every image of a given format in alphabetical order from the folder
#   arguments : name (without .gif extension), duration (duration of each image), format (png, jpg, format of the frames)
#   to set fps instead of image duration add -fps
#

from PIL import Image
import glob
import sys

# Returns command arguments
def parseArgs():
    arg = sys.argv
    if arg[1] == '-fps':
        frames = getFrames(arg[4])
        duration = int(1/arg[3]*1000)
        name = arg[2]
    else:
        frames = getFrames(arg[3])
        duration = int(arg[2])
        name = arg[1]

    return name, duration, frames

# Returns the list of frames to use
def getFrames(format):
    frames = []
    images = glob.glob(f"*.{format}")
    images.sort()
    for i in images:
        new_frame = Image.open(i)
        frames.append(new_frame)

    return frames

# Main function
def saveGif(name, duration, frames):
    frames[0].save(f"{name}.gif", format='GIF', append_images=frames[1:], save_all=True, duration=duration, loop=0)
    print(f"{len(frames)} frames successfuly compiled as {name}.gif !")

name, duration, frames = parseArgs()
saveGif(name, duration, frames)


