'''Create the GIF image with each frame having user specified duration.

Author: He Zhang @ University of Exeter
Date: 16th April 2019 (Update: 18th April 2019)
Contact: hz298@exeter.ac.uk zhangheupc@126.com

Copyright (c) 2019 He Zhang
'''

# Python 3.7

import os
import re
import shutil

import imageio


# 1. Specify user settings.

# Set the path of input/output images.
PATH_INPUT_IMAGE = 'IMAGE/'
PATH_OUTPUT_IMAGE = 'IMAGE_GIF/'

# Create the folder for saving output GIF images.
# Check if the folder exists. If so, delete it and create a new one.
if os.path.exists(PATH_OUTPUT_IMAGE) is True:
    shutil.rmtree(PATH_OUTPUT_IMAGE)
os.mkdir(PATH_OUTPUT_IMAGE)

# Set the format of input static images.
FORMAT_INPUT_IMAGE = '.png'

# Set the name of output GIF images.
GIF_NAME_SAME = "imgGIF_SAME.gif"
GIF_NAME_DIFF = "imgGIF_DIFF.gif"

# Set the duration of each frame in GIF images.
DURATION_FRAME = 0.5

# Set the repeat time of the first and the last frames in GIF images.
REPEAT_TIMES_FRAME = 3

# Set the pattern for creating GIF images.
PATTERN = 1
# Note:
#     PATTERN = 1 - Create GIF image with each frame having the same duration time.
#     PATTERN = 2 - Create GIF image with each frame having different duration time.


# 2. Create GIF image.

print('\nStart creating GIF image...')

if PATTERN == 1:
    # 2.1 Create the GIF image with each frame having the SAME duration.

    print('\nPattern %d - Each frame of GIF image has the same duration.' % PATTERN)

    imgGIF = []
    imgNames = sorted((iN for iN in os.listdir(PATH_INPUT_IMAGE) if iN.endswith(FORMAT_INPUT_IMAGE)))
    # Note:
    #     The serial number in the name of input images should have the same length (e.g., '00', '01', ...).
    #     If not, the 'sorted()' function will return the wrong order of images.

    for imgName in imgNames:
        imgGIF.append(imageio.imread(PATH_INPUT_IMAGE + imgName))

    imageio.mimsave(PATH_OUTPUT_IMAGE + GIF_NAME_SAME, imgGIF, duration=DURATION_FRAME)

elif PATTERN == 2:
    # 2.2 Create the GIF image with the first and the last frames having LONG duration.

    print('\nPattern %d - Each frame of GIF image has different duration.' % PATTERN)

    imgGIF = []
    imgNames = sorted((iN for iN in os.listdir(PATH_INPUT_IMAGE) if iN.endswith(FORMAT_INPUT_IMAGE)))
    # Note:
    #     The serial number in the name of input images should have the same length (e.g., '00', '01', ...).
    #     If not, the 'sorted()' function will return the wrong order of images.

    for imgName in imgNames:
        tmpName = re.split(r"[_.]", imgName)[2]  # 'tmpName' <str> of <list>
        # Note:
        #     Split image name string by '_' and '.'.
        #     Select the 2-nd part (serial number) of image name (i.e., '00', '01', ...).

        if tmpName == '00' or tmpName == '99':
            # '00' in _00.png - The first frame in GIF image.
            # '99' in _99.png - The last frame in GIF image.
            tt = 0
            while tt < REPEAT_TIMES_FRAME:
                imgGIF.append(imageio.imread(PATH_INPUT_IMAGE + imgName))
                tt += 1
        else:
            imgGIF.append(imageio.imread(PATH_INPUT_IMAGE + imgName))

    imageio.mimsave(PATH_OUTPUT_IMAGE + GIF_NAME_DIFF, imgGIF, duration=DURATION_FRAME)

print('\nComplete!\n')
