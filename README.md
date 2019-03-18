# GIF Image Creator

[![image](https://img.shields.io/badge/license-MIT-lightgrey.svg)]()
[![image](https://img.shields.io/badge/python-3.7-blue.svg)]()
[![image](https://img.shields.io/badge/status-stable-brightgreen.svg)]()
[![image](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

This is a **Python** implementation of creating GIF image from a collection of static images (e.g., PNG images).

## Functions

- Creating GIF image with each frame having the **same** duration time.

- Creating GIF image with the first and the last frames having **different** (longer) duration time.

## Dependency

* __imageio 2.4.1__

## Usage

1. Prepare a collection of static images with ordered names (e.g., `01.png`, `02.png`, etc.) in a folder (e.g., `IMAGE/`).

2. Specify user settings (e.g., `DURATION_TIME_FRAME`, `PATTERN_GIF_IMAGE`, etc.) in the code (see comments).

2. Run `run_GIFCreator.py` to create GIF image.

3. The created GIF image will be saved in the pre-specified folder (e.g., `IMAGE_GIF/`).

## Results

- GIF image with **SAME** frame duration time (`PATTERN_GIF_IMAGE = 1`).

![Equivariance](https://github.com/HeZhang1994/gif-creator/blob/master/IMAGE_GIF/imgGIF_SAME.gif)

- GIF image with **DIFFERENT** frame duration time (`PATTERN_GIF_IMAGE = 2`).

![Equivariance](https://github.com/HeZhang1994/gif-creator/blob/master/IMAGE_GIF/imgGIF_DIFF.gif)

<br>

<i>Please star this repository if you found its content useful. Thank you very much. ^_^</i>

<i>如果该程序对您有帮助，请为该程序加星支持哈，非常感谢。^_^</i>

<i>Last updated: 18/03/2019</i>
