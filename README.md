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
    <img align="center" width="808" src="https://user-images.githubusercontent.com/59794336/104905129-3bdea680-5982-11eb-9a17-bc3cdfa331f5.png"/>
</p>

Display each bitmap pixel colors, here [ 55 81 158 ] is the first pixel value in the first row and first column of the matrix. (it refers to the real bitmap pixel at the last row and first column)

```bash
> python3 main.py --bmp lena_couleur.bmp all
```

<p align="center" width="100%">
    <img align="center" width="808" src="https://user-images.githubusercontent.com/59794336/104905128-3b461000-5982-11eb-97ff-37c67934d9f2.png"/>
</p>

<br>

### Rotate image

Rotate the bitmap to 90° or 180° or 270°

```bash
> python3 main.py --bmp lena_couleur.bmp --rotate 90 --output generated.bmp --verbose 
```

<p align="center" width="100%">
    <img align="center" width="270"src="https://user-images.githubusercontent.com/59794336/104903946-ec4bab00-5980-11eb-91a9-7a99b86fe0c6.png"/>
    <img align="center" width="270" src="https://user-images.githubusercontent.com/59794336/104903950-ece44180-5980-11eb-9c1b-83743b51c733.png"/>
    <img align="center" width="270" src="https://user-images.githubusercontent.com/59794336/104903953-ee156e80-5980-11eb-9110-04e4368c9122.png"/>
</p>

<br>

### Resize image

Resize the bitmap to a ratio value or specific dimensions
- The bitmap has been resized to 256x256 with ratio value=0.5

```bash
> python3 main.py --bmp lena_couleur.bmp --resize 0.5 --output generated.bmp --verbose
```

<p align="center" width="100%">
    <img align="center" width="1000" src="https://user-images.githubusercontent.com/59794336/104905240-5d3f9280-5982-11eb-8e6e-a759bdcb5754.png"/>
</p>

- The bitmap has been resized to dimension 500x300 (width x height)

```bash
> python3 main.py --bmp lena_couleur.bmp --resize 500 300 --output generated.bmp --verbose
```

<p align="center" width="100%">
    <img align="center" width="1000" src="https://user-images.githubusercontent.com/59794336/104905247-616bb000-5982-11eb-9112-5868a63c8fc4.png"/>
</p>

<br>

### Contrast adjustment

Adjust the contrast parameter of the bitmap

```bash
> python3 main.py --bmp lena_couleur.bmp --contrast +180 --output generated.bmp --verbose
```

- Negative adjustment (-255, -180, -80, -0)
<p align="center" width="100%">
    <img align="center" width="189" src="https://user-images.githubusercontent.com/59794336/104904029-04232f00-5981-11eb-8ec4-234dace928b5.png"/>
    <img align="center" width="189" src="https://user-images.githubusercontent.com/59794336/104904030-04232f00-5981-11eb-80b8-ebd6c3606513.png"/>
    <img align="center" width="189" src="https://user-images.githubusercontent.com/59794336/104904036-04bbc580-5981-11eb-842c-c343a448b9de.png"/>
    <img align="center" width="189" src="https://user-images.githubusercontent.com/59794336/104904037-05545c00-5981-11eb-8e13-455c25e5fd7a.png"/>
</p>

- Positive adjustment (+0, +80, +180, +255)
  
<p align="center" width="100%">
    <img align="center" width="189" src="https://user-images.githubusercontent.com/59794336/104904037-05545c00-5981-11eb-8e13-455c25e5fd7a.png"/>
    <img align="center" width="189" src="https://user-images.githubusercontent.com/59794336/104904044-06858900-5981-11eb-9a1f-0be609ebe420.png"/>
    <img align="center" width="189" src="https://user-images.githubusercontent.com/59794336/104904047-071e1f80-5981-11eb-957a-dd8c453517b4.png"/>
    <img align="center" width="189" src="https://user-images.githubusercontent.com/59794336/104904052-071e1f80-5981-11eb-966c-775ff80f16a8.png"/>
</p>

<br>

### Color to grayscale 

Changes a colored bitmap into a grayscale image

- With Eugène Atget method

```bash
> python3 main.py --bmp lena_couleur --grayscale atget --output generated.bmp --verbose
```

<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904210-3765be00-5981-11eb-9e21-0ba18fe03e99.png"/>
</p>

- With mean method (average)

```bash
> python3 main.py --bmp lena_couleur --grayscale mean --output generated.bmp --verbose
```

<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904217-39c81800-5981-11eb-8275-c424ca3a91d4.png"/>
</p>

- With depending on luminance method (more accurate than mean method)

```bash
> python3 main.py --bmp lena_couleur --grayscale luminance --output generated.bmp --verbose
```

<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904223-3af94500-5981-11eb-846e-b3168f0c3cf0.png"/>
</p>

__To better understand the difference between mean and luminance method__

<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904220-39c81800-5981-11eb-9eae-8132672ac7dc.png"/>
</p>
<p align='center'>Original</p>

<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904222-3a60ae80-5981-11eb-90e0-aa6cc0b83a55.png"/>
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904228-3b91db80-5981-11eb-8e91-5ae55b9f9f4f.png"/>
</p>

<p align='center'>Mean method and Luminance method</p>

Luminance method is much more accurate than mean method. 

<br>

### Color to black & white (binary)

Changes a colored bitmap into a black and white image

```bash
> python3 main.py --bmp lena_couleur.bmp --blackwhite --output generated.bmp --verbose
```

<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904285-4c425180-5981-11eb-99cc-697b45c08731.png"/>
</p>

<br>

### Color to negative

Changes a colored bitmap into a negative image

```bash
> python3 main.py --bmp lena_couleur.bmp --negative --output generated.bmp --verbose
```

<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904306-51070580-5981-11eb-9dab-786d12ff7fbe.png"/>
</p>

<br>

### Keep color channel

Keep one-color or two-color channel of the bitmap 
- Red
- Green
- Blue
- Red/Blue (Magenta)
- Red/Green (Yellow)
- Blue/Green (Cyan)

```bash
> python3 main.py --bmp lena_couleur.bmp --colorchannel rg --output generated.bmp --verbose
```

<p align="center" width="100%">
    <img align="center" width="250" src="https://user-images.githubusercontent.com/59794336/104904334-57957d00-5981-11eb-9efd-b0de5ac87f25.png"/>
    <img align="center" width="250" src="https://user-images.githubusercontent.com/59794336/104904340-582e1380-5981-11eb-9077-6e5eec130da0.png"/>
    <img align="center" width="250" src="https://user-images.githubusercontent.com/59794336/104904348-59f7d700-5981-11eb-94bb-783821dc8be4.png"/>
</p>

<p align="center" width="100%">
    <img align="center" width="250" src="https://user-images.githubusercontent.com/59794336/104904350-5a906d80-5981-11eb-9b80-17d83938d613.png"/>
    <img align="center" width="250" src="https://user-images.githubusercontent.com/59794336/104904355-5bc19a80-5981-11eb-94f8-f970f237a4bb.png"/>
    <img align="center" width="250" src="https://user-images.githubusercontent.com/59794336/104904361-5c5a3100-5981-11eb-92bf-9ad5f239e317.png"/>
</p>

<br>

### Brightness adjustment

Adjust the brightness parameter of the bitmap

```bash
> python3 main.py --bmp lena_couleur.bmp --brightness +80 --output generated.bmp --verbose
```

- Negative adjustment (-255, -180, -80, -0)
<p align="center" width="100%">
    <img align="center" width="189" src="https://user-images.githubusercontent.com/59794336/104904452-7431b500-5981-11eb-8b67-f6c106e8f1e6.png"/>
    <img align="center" width="189" src="https://user-images.githubusercontent.com/59794336/104904453-74ca4b80-5981-11eb-8bf0-ce0b9df13ada.png"/>
    <img align="center" width="189" src="https://user-images.githubusercontent.com/59794336/104904454-74ca4b80-5981-11eb-9cc6-6c9021707c06.png"/>
    <img align="center" width="189" src="https://user-images.githubusercontent.com/59794336/104904457-7562e200-5981-11eb-8df5-8df87dad842a.png"/>
</p>

- Positive adjustment (+0, +80, +180, +255)
  
<p align="center" width="100%">
    <img align="center" width="189" src="https://user-images.githubusercontent.com/59794336/104904457-7562e200-5981-11eb-8df5-8df87dad842a.png"/>
    <img align="center" width="189" src="https://user-images.githubusercontent.com/59794336/104904465-76940f00-5981-11eb-808e-e6372af42bd1.png"/>
    <img align="center" width="189" src="https://user-images.githubusercontent.com/59794336/104904465-76940f00-5981-11eb-808e-e6372af42bd1.png"/>
    <img align="center" width="189" height='189'src="https://user-images.githubusercontent.com/59794336/104904466-772ca580-5981-11eb-877b-d47ab6abdef3.png"/>
</p>

<br>

### Flip image

Flip the bitmap along its vertical axis (along its horizontal axis is the same as a rotation 180°)

```bash
> python3 main.py --bmp lena_couleur.bmp --flip --output generated.bmp --verbose
```

<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904489-7eec4a00-5981-11eb-9d76-2a7b6480add6.png"/>
</p>

<br>

### Filter: Edge-detection 

filter to detect the edges of the image

```bash
> python3 main.py --bmp lena_couleur.bmp --filter edge-detection --output generated.bmp --verbose
```

<p align="center" width="100%">
    <img align="center" width="270"src="https://user-images.githubusercontent.com/59794336/104904522-86abee80-5981-11eb-9259-d11dcd66aef4.png"/>
    <img align="center" width="270" src="https://user-images.githubusercontent.com/59794336/104904539-8ca1cf80-5981-11eb-88f0-967be5787ca9.png"/>
    <img align="center" width="270" src="https://user-images.githubusercontent.com/59794336/104904543-8e6b9300-5981-11eb-86fa-90630d5478de.png"/>
</p>

<br>

### Filter: Edge-reinforcement

filter to reinforce the edges of the image

```bash
> python3 main.py --bmp lena_couleur.bmp --filter edge-reinforcement --output generated.bmp --verbose
```

<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904608-a2af9000-5981-11eb-85e0-8e32fd6f64ab.png"/>
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904626-a6dbad80-5981-11eb-80ad-6cd917af6a28.png"/>
</p>

<br> 

### Filter: Blur

filter to blur the image

```bash
> python3 main.py --bmp lena_couleur.bmp --filter blur --output generated.bmp --verbose
```

<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904576-988d9180-5981-11eb-8f04-ca586e92d982.png"/>
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904577-9a575500-5981-11eb-8e34-75eea1b0ce59.png"/>
</p>

<br>

### Filter: Emboss

filter to emboss the image

```bash
> python3 main.py --bmp lena_couleur.bmp --filter emboss --output generated.bmp --verbose
```

<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904641-ad6a2500-5981-11eb-8724-bcf9eb2fc74e.png"/>
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904658-b1964280-5981-11eb-95b6-70aee570fa62.png"/>
</p>

<br>

### Color channel Histogram

Display color channel histogram

```bash
> python3 main.py --bmp lena_couleur.bmp --histogram --output generated.bmp --verbose
```

- Color channel histogram for colored image
  
<p align="center" width="100%">
    <img align="center" width="500" src="https://user-images.githubusercontent.com/59794336/104904391-667c2f80-5981-11eb-8cb4-e6eadc69a0a5.png"/>
</p>

- Color channel histogram for grayscale image

<p align="center" width="100%">
    <img align="center" width="500" src="https://user-images.githubusercontent.com/59794336/104904394-67ad5c80-5981-11eb-8975-336081ea4ca7.png"/>
</p>

<br>

### Overlay two images 

Feature to superimpose one image to another

- The output image is generated by obtaining the darkest pixel between the two images

```bash
> python3 main.py --bmp lena_couleur.bmp --overlay generated/bitmap512-512.bmp maximum --output generated.bmp --verbose
```

<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904692-be1a9b00-5981-11eb-8179-78dc5e11e94a.png"/>
</p>

- The output image is generated by obtaining the lightest pixel between the two images

```bash
> python3 main.py --bmp lena_couleur.bmp --overlay generated/bitmap512-512.bmp minimum --output generated.bmp --verbose
```

<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/104904699-bfe45e80-5981-11eb-9232-aa19feefb991.png"/>
</p>

--- 

<br>

### Fun zone

<p align="center" width="100%">
    <img align="center" width="300" height="300" src="https://user-images.githubusercontent.com/59794336/104904726-ca9ef380-5981-11eb-986d-55b6dd9baa5d.png"/>
</p>

