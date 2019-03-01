### Task description: Create GIF image with each frame having user specified duration time.

import imageio, os
import re  # Regular expression is required for split file names.


## User Settings

input_path = 'Img_Frames/'  # Set input image folder.
img_extension = '.png'  # Set the format of input images.

duration_time = 0.5  # Set the duration time of each frame/image.
num_repeat = 3  # Set the repeating time of the first and the last frames/images (time x3).

tag_type = 1  # Set the pattern of creating GIF image.
# tag_type = 1 - Create GIF image with each frame having the same duration time.
# tag_type = 2 - Create GIF image with each frame having different duration time.


## Create GIF image.

print('\nStart creating GIF image...')

if tag_type == 1:
    ## Opt. 1 Create GIF image with each frame having the SAME duration time.
    
    print('\nPattern: %d - Each frame has same duration time.' % tag_type)
    
    imgGIF = []
    imgNames = sorted((iN for iN in os.listdir(input_path) if iN.endswith(img_extension)))
    # Note: 
    #     The serial number of image name should have same length.
    #     E.g., _01.png _02.png ... _12.png ...
    #     Or the sorted() function will return wrong order of image names.
    
    for imgName in imgNames:
        imgGIF.append(imageio.imread(input_path + imgName))
    imageio.mimsave(input_path + 'imgGIF_SAME.gif', imgGIF, duration=duration_time)

elif tag_type == 2:
    ## Opt. 2 Create GIF image with the first and the last frames having LONG duration time.
    
    print('\nPattern: %d - Each frame has different duration time.' % tag_type)
    
    imgGIF = []
    imgNames = sorted((iN for iN in os.listdir(input_path) if iN.endswith(img_extension)))
    # Note: 
    #     The serial number of image name should have same length.
    #     E.g., _01.png _02.png ... _12.png ...
    #     Or the sorted() function will return wrong order of image names.
    
    for imgName in imgNames:
        tmpName = re.split(r"[_.]", imgName)[2]  # Split image name by "_" and/or ".".
        if tmpName == '00' or tmpName == '99':  # _00.png - the first frame, _99.png - the last frame.
            tt = 0
            while tt < num_repeat:
                imgGIF.append(imageio.imread(input_path + imgName))
                tt += 1
        else:
            imgGIF.append(imageio.imread(input_path + imgName))
    imageio.mimsave(input_path + 'imgGIF_DIFF.gif', imgGIF, duration=duration_time)

print('\nComplete!\n')

