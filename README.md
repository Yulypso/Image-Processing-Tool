# Digital Image - Bitmap processing tool

## Author

[Thierry Khamphousone](https://www.linkedin.com/in/tkhamphousone/)

<br>

## Introduction 

This project is about creating a tool that reads an image in a given format (bitmap or jpeg), process this image (enlarge, shrink ...), save the image in an output file different from the one given as input ( same format as input or different) to never corrupt the original files. 

<br>

__Note__: This Bitmap Processing tool cannot process:

- Due to RLE compression (Run length encoding)
  - bitmap v3 
  - bitmap v5
  - bitmap v7 
- Due to bits per pixels < 8
  - bitmap v6
  - bitmap v7
  - bitmap v8

<br>

## Features implemented

- __Display bitmap header__
- __Rotate image__ [90, 180, 270]
- __Resize image__ \<ratio> or \<width> \<height>
- __Contrast adjustment__ [-255, +255]
- __Brightness adjustment__ [-255, +255]
- __Color image to Grayscale image__ \<mean> method or \<luminance> method or \<atget> method
- __Flip image__
- __Color image to 1 or 2 colors channel__ (blue/red/green/blue-green/blue-red/green-red)
- __Negative image__
- __Black & white image__
- __Verbose__
- __Display Pixels__ \<all> or \<position x> \<positon y>
- __Display image histogram__
- __Overlay two images__ 
- __Filter:__ 
  - __Sobel edge detection__
  - __Edge reinforcement__
  - __Blur__
  - __Emboss__

<br>

## Get Started

__Setup__
```bash
> git clone https://github.com/Yulypso/Imagerie_Numerique.git
> cd Imagerie_numerique
> python3 -m venv .venv

# for MacOs/Linux
> source .venv/bin/activate

#for Windows
> py -3 -m venv .venv
> .venv\scripts\activate

# to install requirements 
> pip3 install -r requirements.txt
```

__[Check Dependency Graph](https://github.com/Yulypso/Imagerie_Numerique/network/dependencies)__

<br>

__Note__: In Visual Studio Code, don't forget to select the correct Python interpreter. <br>

[CMD + SHIFT + P] > select Interpreter > Python 3.9.0 64-bits ('.venv') [./.venv/bin/python]

<br>

__Run the code__
```bash
> cd project/bitmapProcessing
> python3 main.py [-h] --bmp <file_name.bmp> [--rotate <rotation degree>]
                  [--overlay <file_name.bmp>, <option>][--blackwhite] 
                  [--resize <resizing ratio> or [<width> <height>]] 
                  [--verbose] [--flip] [--grayscale <grayscale method>] [--negative] 
                  [--colorchannel <color channel>][--brightness <brightness value>]
                  [--pixels <all> or [<position x> <position y>]] [--histogram] 
                  [--contrast <contrast value>] [--filter <filter type>] 
                  [--output <file_name.bmp>]
```

```bash
--Bitmap processing tool--

optional arguments:
  -h, --help            show this help message and exit
  --bmp <file_name.bmp>
                        image file to parse and displays header information
  --overlay, -ov <file_name.bmp>, <option>
                        image file to overlay the input image, <maximum> or <minimum>
  --rotate, -rt <rotation degree>
                        degree of image rotation [90, 180, 270]
  --resize, -rs <resizing ratio> or [<width> <height>]
                        ratio of image resizing
  --contrast, -ct <contrast value>
                        image contrast [-255, +255]
  --brightness <brightness value>, -bn <brightness value>
                        image brightness [-255, +255]
  --verbose, -v         get more information
  --flip, -fp           image flip
  --grayscale, -gs <grayscale method>
                        image grayscale <mean> or <luminance> or <atget>
  --negative, -n        image negative
 --colorchannel, -cc <color channel>
                        image color adjustment ['r', 'g', 'b', 'rg', 'rb', 'gb']
  --blackwhite, -bw     image black & white
  --pixels, -p <display option>     
                        display input image pixels <all> or [<position x> <position y>]
  --histogram, -hg      display input image histogram
  --filter, -ft <filter type>
                        image filter ['edge-detection', 'blur', 'edge-reinforcement', 'emboss']
  --output, -o <file_name.bmp>
                        generated file
```


__Stop the code__
```bash
#don't forget to deactivate the virtual environement (.venv)
> deactivate
```

__Unit Test__
```bash
> cd project/bitmapProcessing
> python3 unitTest.py

....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
<br>

## Feature Explanations

We will mainly use __Colored Lena__ to explain the features.
<p align="center" width="100%">
    <img align="center" width="300" height="300" src="https://user-images.githubusercontent.com/59794336/104903744-b6a6c200-5980-11eb-829c-8e4878cfa487.png"/>
</p>

<br>

### Dashboard

Each feature applied on the input bitmap has a checkbox to know easily which feature has been chosen

```bash
> python3 main.py --bmp lena_couleur.bmp --rotate 90 -hg -rs 400 400 -fp -ct +80 --pixels all -o generated.bmp -cc rb
```

<p align="center" width="100%">
    <img align="center" width="808" height="260" src="https://user-images.githubusercontent.com/59794336/104905977-6846f280-5983-11eb-9ff7-c58e5a3c6f46.png"/>
</p>

<br>

### Display Bitmap header

Display information inside the bitmap byte header

```bash
> python3 main.py --bmp lena_couleur.bmp
```

<p align="center" width="100%">
    <img align="center" width="880" height="254" src="https://user-images.githubusercontent.com/59794336/104903889-db9b3500-5980-11eb-9c2b-4d00b3c7764d.png"/>
</p>

<br>

### Display pixels

Display pixel colors at specific position, here x=128 and y=192

```bash
> python3 main.py --bmp lena_couleur.bmp --pixels 128 292
```

<p align="center" width="100%">
    <img align="center" width="808" height="25" src="https://user-images.githubusercontent.com/59794336/104905129-3bdea680-5982-11eb-9a17-bc3cdfa331f5.png"/>
</p>

Display each bitmap pixel colors, here [ 55 81 158 ] is the first pixel value in the first row and first column of the matrix. (it refers to the real bitmap pixel at the last row and first column)

```bash
> python3 main.py --bmp lena_couleur.bmp all
```

<p align="center" width="100%">
    <img align="center" width="808" height="400" src="https://user-images.githubusercontent.com/59794336/104905128-3b461000-5982-11eb-97ff-37c67934d9f2.png"/>
</p>

<br>

### Rotate image

Rotate the bitmap to 90° or 180° or 270°

```bash
> python3 main.py --bmp lena_couleur.bmp --rotate 90 --output generated.bmp --verbose 
```

<p align="center" width="100%">
    <img align="center" width="270" height="270" src="https://user-images.githubusercontent.com/59794336/104903946-ec4bab00-5980-11eb-91a9-7a99b86fe0c6.png"/>
    <img align="center" width="270" height="270" src="https://user-images.githubusercontent.com/59794336/104903950-ece44180-5980-11eb-9c1b-83743b51c733.png"/>
    <img align="center" width="270" height="270" src="https://user-images.githubusercontent.com/59794336/104903953-ee156e80-5980-11eb-9110-04e4368c9122.png"/>
</p>
<div align="center">
  <p style='display:inline; padding-right:17em'>90°</p>
  <p style='display:inline'>180°</p>
  <p style='display:inline; margin-left:17em'>270°</p>
</div>

<br>

### Resize image

<br>

### Contrast adjustment

<br>

### Color to grayscale 

<br>

### Color to black & white (binary)

<br>

### Color to negative

<br>

### Keep color channel

<br>

### Brightness adjustment

<br>

### Flip image

<br>

### Filter: Edge-detection 

<br>

### Filter: Edge-reinforcement

<br> 

### Filter: Blur

<br>

### Filter: Emboss

<br>

### Color channel Histogram

<br>

### Overlay two images 



