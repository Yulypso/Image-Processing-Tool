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
    <img align="center" width="300" height="300" src="https://raw.githubusercontent.com/Yulypso/Imagerie_Numerique/feature/README-pictures/README-Pictures/0-lena_couleur.bmp?token=AOIGHIDDWVHLFQK5WRYIVMDAATDEY"/>
</p>

<br>

### Dashboard

<br>

### Display header

<br>

### Display pixels

<br>

### Rotate image

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



