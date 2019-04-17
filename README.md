# GIF Image Creator

[![image](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/HeZhang1994/gif-creator/blob/master/LICENSE)
[![image](https://img.shields.io/badge/python-3.7-blue.svg)]()
[![image](https://img.shields.io/badge/status-stable-brightgreen.svg)]()
[![image](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

This is a **Python** implementation of creating the **GIF** image with a collection of static images (e.g., PNG/JPG images).

## Functions

- Creating a **GIF** image with each frame having the **same** duration.

- Creating a **GIF** image with the first and the last frames having **different** (longer) duration.

## Dependency

* __imageio 2.4.1__

## Usage

1. Prepare a collection of static images with ordered names (e.g., `01.png`, `02.png`, ...) in a folder (e.g., `IMAGE/`).

2. Specify user settings (`DURATION_FRAME`, `PATTERN`, etc.) in the code (see comments).

2. Run `run_GIFCreator.py` or `run_GIFCreator.ipynb` to create the GIF image with static images.

3. The created GIF image will be saved in the pre-specified folder (e.g., `IMAGE_GIF/`).

## Results

- The GIF image with **SAME** frame duration (`PATTERN = 1, DURATION_FRAME = 0.5`).

![Equivariance](https://github.com/HeZhang1994/gif-creator/blob/master/IMAGE_GIF/imgGIF_SAME.gif)

- The GIF image with **DIFFERENT** frame duration (`PATTERN = 2, DURATION_FRAME = 0.5/1.5`).

![Equivariance](https://github.com/HeZhang1994/gif-creator/blob/master/IMAGE_GIF/imgGIF_DIFF.gif)

<br>

<i>Please star this repository if you found its content useful. Thank you very much. ^_^</i>

<i>如果该程序对您有帮助，请为该程序加星支持哈，非常感谢。^_^</i>

<i>Last updated: /04/2019</i>
