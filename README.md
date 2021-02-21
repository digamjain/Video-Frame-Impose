# Video-Frame-Impose

A small program written in Python 3 to export a video/media file into frames then using the exported images to create a superimposed image with varying alpha value and cutom frames as entered by user to form the final superimposed image.

## Original test file
  "Stock footage provided by Videvo, downloaded from www.videvo.net"	

https://user-images.githubusercontent.com/42437393/108641467-695cc980-74c5-11eb-9083-b89dee29b894.mp4

## Superimposed Imaged
This result was obtained by superimposing every 15th frame.

![Imp_image](https://user-images.githubusercontent.com/42437393/108641507-a3c66680-74c5-11eb-8f44-78e563b462d1.jpg)

## How To Use

To install all the required libraries for the project to run

	pip install -r requirements.txt
  
Final image will be saved as "Imp_image.jpg" in the same directory.

All exported frames from the video will be saved under the directory named "frames-{name}" where '{name}' is the name of the original file.

### Important
Please make sure the test file is in the same directory as the program.
