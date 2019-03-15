# GIF Image Creator

[![image](https://img.shields.io/badge/license-MIT-lightgrey.svg)]()
[![image](https://img.shields.io/badge/python-3.7-blue.svg)]()
[![image](https://img.shields.io/badge/status-stable-brightgreen.svg)]()
[![image](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

This is a **Python** implementation of creating GIF image from a collection of static images (e.g., PNG images).

## Functions

- Creating GIF image with each frame having the **same** duration time.

- Creating GIF image with the first and the last frames having **different** (long) duration time.

## Dependency

* __imageio 2.4.1__

## Usage

1. Prepare a series of static images (with ordered names) in a folder (e.g., ```Img_Frames/```).

2. Specify user settings (e.g., duration time) in ```run_GIFCreator.py``` (see comments for details).

2. Run ```run_GIFCreator.py```.

3. The created GIF image will be saved in the pre-specified folder (i.e., ```Img_Frames/```).

## Results

- GIF image with **SAME** frame duration time.

![Equivariance](https://github.com/HeZhang1994/png-to-gif/blob/master/Img_Frames/imgGIF_SAME.gif)

- GIF image with **DIFFERENT** frame duration time.

![Equivariance](https://github.com/HeZhang1994/png-to-gif/blob/master/Img_Frames/imgGIF_DIFF.gif)

<br>

<i>Please star this repository if you found its content useful. Thank you very much.</i>

<i>如果该程序对您有帮助，请为该程序加星支持哈，非常感谢。</i>

<i>Last updated: 15/03/2019</i>

