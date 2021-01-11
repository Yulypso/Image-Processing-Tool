# Digital Image

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

- Rotate image [90, 180, 270]
- Resize image \<ratio> or \<width> \<height>
- Contrast adjustment [-255, +255]
- Color image to Grayscale image
- Flip image
- Verbose
- Display Pixels

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

# to install requirements (here: numpy)
> pip3 install -r requirements.txt
```

__Note__: In Visual Studio Code, don't forget to select the correct Python interpreter. <br>

[CMD + SHIFT + P] > select Interpreter > Python 3.9.0 64-bits ('.venv') [./.venv/bin/python])

<br>

__Run the code__
```bash
> cd project/bitmapProcessing
> python3 main.py [-h] --bmp <file_name.bmp> [--rotate <rotation degree>]
               [--resize <resizing ratio> or [<width> <height>]
               [<resizing ratio> or [<width> <height>] ...]] [--contrast <contrast value>]
               [--verbose] [--flip] [--grayscale] [--pixels] [--output <file_name.bmp>]
```

```bash
--Bitmap processing tool--

optional arguments:
  -h, --help            show this help message and exit
  --bmp <file_name.bmp>
                        image file to parse
  --rotate <rotation degree>, -rt <rotation degree>
                        degree of image rotation
  --resize <resizing ratio> or [<width> <height>] [<resizing ratio> or [<width> <height>] ...], -rs <resizing ratio> or [<width> <height>] [<resizing ratio> or [<width> <height>] ...]
                        ratio of image resizing
  --contrast <contrast value>, -c <contrast value>
                        image contrast
  --verbose, -v         get more information
  --flip, -fp           image flip
  --grayscale, -gs      image grayscale
  --pixels, -p          display input image pixels
  --output <file_name.bmp>, -o <file_name.bmp>
                        generated file
```


__Stop the code__
```bash
#don't forget to deactivate the virtual environement (.venv)
> deactivate
```