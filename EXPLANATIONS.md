# Digital Image - Bitmap processing tool

To go back to the description of those features **->** __[Click here](./README.md)__

## Table of Contents

- __[Digital Image - Bitmap processing tool](#digital-image---bitmap-processing-tool)__
  - __[Table of Contents](#table-of-contents)__
  - __[Feature Implementations](#feature-implementations)__
    - [Generate each feature within a test directory](#generate-each-feature-within-a-test-directory)
    - [Display Bitmap header](#display-bitmap-header)
    - [Rotate image](#rotate-image)
    - [Resize image](#resize-image)
    - [Contrast adjustment](#contrast-adjustment)
    - [Color to grayscale](#color-to-grayscale)
    - [Color to black & white (binary)](#color-to-black--white-binary)
    - [Color to negative](#color-to-negative)
    - [Keep color channel](#keep-color-channel)
    - [Brightness adjustment](#brightness-adjustment)
    - [Flip image](#flip-image)
    - [Convolution matrix](#convolution-matrix)
      - [General intuition](#general-intuition)
      - [My implementation](#my-implementation)
    - [Filter: Edge-detection](#filter-edge-detection)
    - [Filter: Edge-reinforcement](#filter-edge-reinforcement)
    - [Filter: Blur](#filter-blur)
    - [Filter: Emboss](#filter-emboss)
    - [Overlay two images](#overlay-two-images)
    - [Image colorization](#image-colorization)
    - [Photomaton](#photomaton)

## Feature Implementations

We will mainly use __Colored Lena__ to explain the features.
<p align="center" width="100%">
    <img align="center" width="300" height="300" src="https://user-images.githubusercontent.com/59794336/104903744-b6a6c200-5980-11eb-829c-8e4878cfa487.png"/>
</p>

We don't need to specify the image directory wether it is located within <samp><strong>images</strong></samp> directory.

<code>--bmp image_name.bmp</code> 

Each bitmap images has 1 or 3 color channels. It means that we have 2-dimensional arrays or 3-dimensional arrays. 
- The first dimension contains the image height
- The second dimension contains the image width
- The third dimension contains pixels written on 3 bytes <samp>[255 255 255] (blue green red)</samp> 

<br/>

### Generate each feature within a test directory
[Back to description](./README.md#generate-each-feature-within-a-test-directory)

<code>--test_features</code> command allows you to generated all features that requires output.

It automatically saves every generated images to this path: <samp><strong>images/test/{feature-name}/{image-name}</strong></samp> 

<br/>

### Display Bitmap header
[Back to description](./README.md#display-bitmap-header)

<code>--bmp image_name.bmp</code> command displays the input bitmap image header which contains information about its signature, file size, image size, image height, image length, color palette and so on. 

bitmap order and size: 
- The header size (offbits) is 54 bytes. 
- The palette size is variable.
- The image part starts after the palette size if it exists.

<br/>

### Rotate image
[Back to description](./README.md#rotate-image)

<code>--rotate {90, 180, 270}</code> command allows you to rotate an image by rotating bytes along its axis 0 and 1 (height and width) by 90° or 190° or 270°. 

<br/>

### Resize image
[Back to description](./README.md#resize-image)

<code>--resize ratio_value</code> command allows you to resize an image by a ratio value. It means that the new image size will be: <var><strong>(height x ratio_value, width x ratio_value)</strong></var>

<code>--resize height_value width_value</code> command allows to resize an image by specifying a dimension. It means that the new image dimension will be: <var><strong>(height_value, width_value)</strong></var> 

to resize the image, we browse the entire original image and copy the pixels into the new image of different dimensions. 

<br/>

### Contrast adjustment
[Back to description](./README.md#contrast-adjustment)

<code>--contrast contrast_value</code> command allows you to generate a new image after modifying the contrast of the image by updating each color channel of each pixel through this formula: 

<var><pre>factor = (259 * (contrast + 255)) / (255 * (259 - contrast))</pre></var> 

contrast value is defined within [0, 255] interval

<br/>

### Color to grayscale
[Back to description](./README.md#color-to-grayscale)

<code>--grayscale sepia</code> command allows you to generated a new sepia image by applying a specific formula for each color channels. 

<pre>
<var>green channel = round(0.272*pixel[2] + 0.534*pixel[1] + 0.131*pixel[0])</var>

<var>blue channel = round(0.349*pixel[2] + 0.686*pixel[1] + 0.168*pixel[0])</var>

<var>red channel = round(0.393*pixel[2] + 0.769*pixel[1] + 0.189*pixel[0])</var></pre>


<code>--grayscale mean</code> command allows you to generated a new mean grayscale image by applying a specific formula for each color channels. 

<var><pre>all channels = (pixel[0] + pixel[1] + pixel[2])/3</pre></var>


<code>--grayscale luminance</code> command allows you to generated a new grayscale image depending on luminance by applying a specific formula for each color channels. 

<var><pre>all channels = (0.0722*channel_luminance(pixel[0]/255) + 0.7152*channel_luminance(pixel[1]/255) + 0.2126*channel_luminance(pixel[2]/255)) * 255 </pre></var>

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

<br/>

### Color to black & white (binary)
[Back to description](./README.md#color-to-black--white-binary)

<code>--blackwhite</code> command allows you to generated a new binary (Black=0, White=255) image by applying a specific formula for each color channels. 

<var><pre>all channels = 255 if mean(pixel[0] + pixel[1] + pixel[2]) > 127</var>

<var>all channels = 0 if mean(pixel[0] + pixel[1] + pixel[2]) <= 127</pre></var>

<br/>

### Color to negative
[Back to description](./README.md#color-to-negative)

<code>--negative</code> command allows you to generated a new negative image by applying a specific formula for each color channels. 

<var><pre>all channels = 255 - pixel_value</pre></var>

<br/>

### Keep color channel
[back to description](./README.md#keep-color-channel)

<code>--colorchannel {g, b, r, gb, gr, br}</code> command allows you to generated a new image where only 1 or 2 color channels are kept by inhibiting color channels that are not wanted. That is to say by setting up inhibited color to 0 value (black).

<var><pre>green-image = inhibit blue + red channels</var>

<var>blue-image = inhibit red + green channels</var>

<var>red-image = inhibit green + blue channels</var>

<var>green-blue-image = inhibit red channel</var>

<var>green-red-image = inhibit blue channel</var>

<var>red-blue-image = inhibit green channel</pre></var>

<br/>

### Brightness adjustment
[back to description](./README.md#brightness-adjustment)

<code>--brightness brightness_value</code> command allows you to generate a new image after modifying the brightness of the image by updating each color channel of each pixel through this formula: 

<var><pre>all pixels = brightness + pixel</pre></var> 

brightness value is defined within [0, 255] interval

<br/>

### Flip image
[back to description](./README.md#flip-image)

<code>--flip</code> command allows you to generate a new flipped image by flipping every image pixels along its axis=1 (vertical).

<br/>

### Convolution matrix

#### General intuition
[Convolution matrices](https://fr.wikipedia.org/wiki/Noyau_(traitement_d%27image)) allow you to apply filters in image processing. For example the edge detection filter, blur filter, edge reinforcement filter or even the emboss filter.


The principle of the convolution matrix is ​​to go through all the pixels of the original image (except the pixels located at the edge of the image) and to apply the “kernel” or “mask” matrix.

For each kernel applied, the value of the new pixel is recalculated for each of its channels. In this example, we apply the same kernel for each of these channels.

<pre>The 3x3 kernel applied in this example is: <strong>
[[0 1 2],
 [2 2 0],
 [0 1 2]]</strong>

Considering that the image covered by the kernel is: <strong>
[[a b c],
 [d e f],
 [g h i]]</strong>

The calculation for each new pixels goes like this:
new pixel = <strong>0</strong>*a + <strong>1</strong>*b + <strong>2</strong>*c + <strong>2</strong>*d + <strong>2</strong>*e + <strong>0</strong>*f + <strong>0</strong>*g + <strong>1</strong>*h + <strong>2</strong>*i
</pre>

<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/106818689-ecce8c00-6678-11eb-9130-7a4b6d84e987.gif"/>
</p>

<br/>

#### My implementation 

My method is much faster than general intuition. Let's start by giving you some intuition. 

As before, in order to apply the convolution, we will scan the original image pixel by pixel and calculate the convolution product. This method is long, especially as the image is large!

<u>So how can you speed up the process?</u>

I chose to use memory. Actually, if the original image is of width w and height h, I decided not to do <var><strong>(w-2) * (h-2) iterations</strong></var> to which is multiplied by <var><strong>3 * 3 iterations</strong></var> for each image pixel iterations to apply the kernel but <strong>I instead chose to only do 9 iterations</strong>.

<pre>
<h3>Let's take an example</h3><hr/>
Imagine having an image which is: <var><strong>2400 x 1600 (width x height)</strong></var>. 

Convolution matrix application would have needed: <var><strong>((2400-2) * (1600-2)) * (3*3) = 34 488 036 total iterations</strong></var>.
</pre>

<u>How does it works?</u>

<pre>
<h3>Convolution matrix | filter(input_image, kernel)</h3><hr/>

1. Take an image of dimension 2400 x 1600 (width x height) as input.
   
2. Initialize a list of 9 empty 3-dimension array of the size of the input image.
   -> The shape of this list would be a 4-dimension array such as (9, 2400, 1600, 3).
      - 9 copies
      - 2400 width
      - 1600 height
      - 3 color channels
  
3. Kernel application
   a. for each kernel indexes (i,j) make a copy of the input image shifted by 1 pixel depending on kernel indexes (i,j).
   b. during this process, add also the kernel value by multiplying all the copied image by the value of the kernel at index (i, j).
      -> By creating shifted image copies, pixels end up outside the image.
         There are several methods to manage the edges.
            - add black pixels (pixel value = 0) along the edges of the image.
            - use the carousel method by rolling pixels. 
      -> I chose to use the carousel method. It means that the convolution matrix which use pixels located on the edge of the image will depend on the pixels located opposite the image.
   c. Finally, sum the 9 copies of shifted images in order to obtain our input image again but with the application of the convolution matrix with the kernel.
</pre>


<br/>

### Filter: Edge-detection 
[back to description](./README.md#filter-edge-detection)

<code>--filter edge-detection</code> command allows you to apply the edge detection filter on the input image through convolution matrix application.

In order to correctly detect the edges of the image, you need to apply two kernels to detect horizontal edges and vertical edges of the image.

[See my convolution matrix filter implementation](#my-implementation)

<pre>
horizontal_kernel: [[1, 2, 1], 
                    [0, 0, 0], 
                    [-1, -2, -1]]
          
Vertical_kernel: [[-1, 0, 1], 
                  [-2, 0, 2], 
                  [-1, 0, 1]]

<h3>Edge-detection filter application:</h3><hr/>
1. Apply filter function with horizontal and vertical kernel
res1 = filter(input_image, horizontal_kernel)
res2 = filter(input_image, vertical_kernel)

2. combine both res1 and res2 in order to get the edge-detected image generated by applying this formula:
new_image = <var><strong>sqrt(res1<sup>2</sup> + res2<sup>2</sup>)</strong></var>
</pre>

- Horizontal kernel and Vertical kernel separated
<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/106925363-5057c880-6710-11eb-8223-940865dbd068.png"/>
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/106925425-5f3e7b00-6710-11eb-8794-84f1de20ddcb.png"/>
</p>

- Horizontal kernel and Vertical kernel combined
<p align="center" width="100%">
    <img align="center" width="300" src="https://user-images.githubusercontent.com/59794336/106925476-6bc2d380-6710-11eb-91c0-db71a8fb0c08.png"/>
</p>

<br/>

### Filter: Edge-reinforcement
[back to description](./README.md#filter-edge-reinforcement)

<code>--filter edge-reinforcement</code> command allows you to apply the edge reinforcement filter on the input image through convolution matrix application.

[See my convolution matrix filter implementation](#my-implementation)

<pre>
reinforcement_kernel: [[0, -1, 0], 
                       [-1, 5, -1], 
                       [0, -1, 0]]
              
<h3>Edge-reinforcement filter application:</h3><hr/>
1. Apply filter function with reinforcement kernel
new_image = filter(input_image, reinforcement_kernel)
</pre>

<br/> 

### Filter: Blur
[back to description](./README.md#filter-blur)

<code>--filter blur</code> command allows you to apply the blur filter on the input image through convolution matrix application.

[See my convolution matrix filter implementation](#my-implementation)

<pre>
blur_kernel: [[1/256, 4/256, 6/256, 4/256, 1/256],
              [4/256, 16/256, 24/256, 16/256, 4/256],
              [6/256, 24/256, 36/256, 24/256, 6/256],
              [4/256, 16/256, 24/256, 16/256, 4/256],
              [1/256, 4/256, 6/256, 4/256, 1/256]]
              
<h3>blur filter application:</h3><hr/>
1. Apply filter function with blur kernel
new_image = filter(input_image, blur_kernel)
</pre>

<br/>

### Filter: Emboss
[back to description](./README.md#filter-emboss)

<code>--filter emboss</code> command allows you to apply the emboss filter on the input image through convolution matrix application.

[See my convolution matrix filter implementation](#my-implementation)

<pre>
emboss_kernel: [[-2, -1, 0], 
                [-1, -1, -1], 
                [0, 1, 2]]
              
<h3>Emboss filter application:</h3><hr/>
1. Apply filter function with emboss kernel
new_image = filter(input_image, emboss_kernel)
</pre>

<br/>

### Overlay two images 
[back to description](./README.md#overlay-two-images)

<code>--overlay {maximum, minimum}</code> command allows you to mix two images together.

<pre>
1. Before covering one image with another, they must have the same dimension. 
   To do this, we do a preprocessing step to resize one image so that it is the same size as the other. 
2. We go through the whole dimension of an image and we recover either the maximum or the minimum of the two images depending on the {option} in order to build the new image. 
</pre>

<br/>

### Image colorization
[back to description](./README.md#image-colorization)

<code>--colorize {hue_value}</code> command allows you to colorize an image by changing its hue. Hue value is a number defined within [0°, 360°] interval. 

In order to be able to modify the hue parameter of an image, we must change the base and switch from the RGB color space to HSV color space.

- byte order within a pixel for RGB color space: [Blue, Green, Red]
- byte order within a pixel for HSV color space: [Brightness, Saturation, Hue]

<p align="center" width="100%">
    <img align="center" width="500" src="https://user-images.githubusercontent.com/59794336/106936903-6d46c880-671d-11eb-89b0-e7bc31d59683.png"/>
</p>

<pre>
<h3>Image colorization application:</h3><hr/>
1. Convert RGB color space to HSV color space
2. Edit Hue channel of each pixel by hue_value
3. Convert back from HSV color space to RGB color space
</pre>

<br/>

### Photomaton
[back to description](./README.md#photomaton)

<code>--photomaton {value}</code> command allows you to create a 'Photomaton' from an image by shifting pixels on the new image.

The images must be square, that is to say <var><strong>image height = image width</strong></var>

<var><strong>{value}</strong></var> corresponds to the number of time we will split the image into 4 parts. 

<br/>

<h4><strong>New pixel position table</strong></h4>

Position in line | Position in column | New pixel position
| :---: | :---: | :---:
Even  | Even | Top Left
Even  | Odd | Top Right
Odd  | Even | Bottom Left
Odd  | Odd | Bottom Right

<br/>

<p align="center" width="100%">
    <img align="center" width="350" src="https://user-images.githubusercontent.com/59794336/106942838-ee558e00-6724-11eb-955d-c70eb7b80e70.png"/>
    <img align="center" width="350" src="https://user-images.githubusercontent.com/59794336/106942851-f0b7e800-6724-11eb-9eb7-30d6c07e54b4.png"/>
</p>

<pre>
<h3>Photomaton application:</h3><hr/>
1. Let's do some preprocessing, you have to resize the input image in square shape.
2. Browse every pixel of the original image and a new pixel will be appened to the new image according to the <strong>New pixel position table</strong>.
</pre>
