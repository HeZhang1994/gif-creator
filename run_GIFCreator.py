### Task description: Create GIF image with each frame has same or different duration time.

import imageio, os
import re  # Regular expression is required for split file name.


# User Settings
input_path = 'Img_Frames/'  # Input image folder.
img_extension = '.png'  # Format of input image frames.
duration_time = 0.5  # Duration time of each frame.
tag_type = 1  # Set the type of created GIF.
# tag_type = 1 - Generate GIF image with each frame has same duration.
# tag_type = 2 - Generate GIF image with each frame has different duration.
num_repeat = 3  # The repeating time of the first and last frames (time x3).

if tag_type == 1:
    ## Opt. 1 Generate GIF image with each frame has SAME duration.
    imgGIF = []
    imgNames = sorted((iN for iN in os.listdir(input_path) if iN.endswith(img_extension)))
    # Note: 
    # The serial number of image name should has same length!!!
    # Or the sorted() function returns wrong order of images!!!
    # E.g., _01.png _02.png ... _12.png ...
    
    for imgName in imgNames:
        imgGIF.append(imageio.imread(input_path + imgName))
    imageio.mimsave(input_path + 'imgGIF_SAME.gif', imgGIF, duration=duration_time)
elif tag_type == 2:
    ## Opt. 2 Generate GIF image with each frame has DIFF duration.
    input_path = 'Img_Frames/'  # Input image folder.
    img_extension = '.png'  # Format of input image frames.
    duration_time = 0.5  # Duration time of each frame.
    
    imgGIF = []
    imgNames = sorted((iN for iN in os.listdir(input_path) if iN.endswith(img_extension)))
    # Note: 
    # The serial number of image name should has same length!!!
    # Or the sorted() function returns wrong order of images!!!
    # E.g., _01.png _02.png _12.png ...
    
    for imgName in imgNames:
        tmpName = re.split(r"[_.]", imgName)[2]  # Split image file name by "_" and ".".
        if tmpName == '00' or tmpName == '99':  # _00.png - first image, _99.png - last image.
            tt = 0
            while tt < num_repeat:
                imgGIF.append(imageio.imread(input_path + imgName))
                tt += 1
        else:
            imgGIF.append(imageio.imread(input_path + imgName))
    imageio.mimsave(input_path + 'imgGIF_DIFF.gif', imgGIF, duration=duration_time)
