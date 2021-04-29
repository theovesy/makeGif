# makeGIF

Easily make GIF from images.

## How to use

First make a folder with every frame of your gif in **alphabetical order and same format**. Make sure there are only images you want to include in the gif, the program will use every image of the selected format in the directory.

Then execute the script using you python interpreter and add the arguments :
* name of the gif without the .gif extension
* duration of each image in milliseconds
* format of the frames (png, jpg...)

Here is an exemple :
```bash
python3 makeGif.py name 100 png
```
You can also use frames per second instead of image duration. To do this, put -fps before other arguments like in the example below :
```bash
python3 makeGif.py -fps name 24 png
```

You can also add this script to your path to easily call it from anywhere. Below is a procedure to do this on linux.

## Install on Linux

* in the directory where makeGif is, run
```bash
sudo chmod +x makeGif.py
```
to make it executable.
* Create a symbolic link to the script in /usr/local/bin/ by running
```bash
sudo ln -s makeGif.py /usr/local/bin/makeGif
```
* Or simply put in the appropriate directory

Now you should be able to simply run the script in any directory like so
```bash
makeGif name 100 png
```





