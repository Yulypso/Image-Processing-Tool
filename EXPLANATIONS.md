# Digital Image - Bitmap processing tool

To go back to the description of those features **->** __[Click here](./README.md)__

## Table of Contents

- __[Digital Image - Bitmap processing tool](#digital-image---bitmap-processing-tool)__
  - __[Table of Contents](#table-of-contents)__
  - __[Feature Implementations](#feature-implementations)__
    - [Dashboard](#dashboard)
    - [Generate each feature within a test directory](#generate-each-feature-within-a-test-directory)
    - [Display Bitmap header](#display-bitmap-header)
    - [Display pixels](#display-pixels)
    - [Rotate image](#rotate-image)
    - [Resize image](#resize-image)
    - [Contrast adjustment](#contrast-adjustment)
    - [Color to grayscale](#color-to-grayscale)
    - [Color to black & white (binary)](#color-to-black--white-binary)
    - [Color to negative](#color-to-negative)
    - [Keep color channel](#keep-color-channel)
    - [Brightness adjustment](#brightness-adjustment)
    - [Flip image](#flip-image)
    - [Filter: Edge-detection](#filter-edge-detection)
    - [Filter: Edge-reinforcement](#filter-edge-reinforcement)
    - [Filter: Blur](#filter-blur)
    - [Filter: Emboss](#filter-emboss)
    - [Color channel Histogram](#color-channel-histogram)
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

<code>--test_features</code> command allows us to generated all features that requires output.

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

<code>--rotate {90, 180, 270}</code> command allows us to rotate an image by rotating bytes along its axis 0 and 1 (height and width) by 90° or 190° or 270°. 

<br/>

### Resize image
[Back to description](./README.md#resize-image)

<code>--resize ratio_value</code> command allows us to resize an image by a ratio value. It means that the new image size will be: <var><strong>(height x ratio_value, width x ratio_value)</strong></var>

<code>--resize height_value width_value</code> command allows to resize an image by specifying a dimension. It means that the new image dimension will be: <var><strong>(height_value, width_value)</strong></var> 

to resize the image, we browse the entire original image and copy the pixels into the new image of different dimensions. 

<br/>

### Contrast adjustment
[Back to description](./README.md#contrast-adjustment)

<code>--contrast contrast_value</code> command allows us to generate a new image after modifying the contrast of the image by updating each color channel of each pixel through this formula: 

<var><pre>factor = (259 * (contrast + 255)) / (255 * (259 - contrast))</pre></var> 

contrast value is defined within [0, 255] interval

<br/>

### Color to grayscale
[Back to description](./README.md#color-to-grayscale)

<code>--grayscale sepia</code> command allows us to generated a new sepia image by applying a specific formula for each color channels. 

<pre>
<var>green channel = round(0.272*pixel[2] + 0.534*pixel[1] + 0.131*pixel[0])</var>

<var>blue channel = round(0.349*pixel[2] + 0.686*pixel[1] + 0.168*pixel[0])</var>

<var>red channel = round(0.393*pixel[2] + 0.769*pixel[1] + 0.189*pixel[0])</var></pre>


<code>--grayscale mean</code> command allows us to generated a new mean grayscale image by applying a specific formula for each color channels. 

<var><pre>all channels = (pixel[0] + pixel[1] + pixel[2])/3</pre></var>


<code>--grayscale luminance</code> command allows us to generated a new grayscale image depending on luminance by applying a specific formula for each color channels. 

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

<code>--blackwhite</code> command allows us to generated a new binary (Black=0, White=255) image by applying a specific formula for each color channels. 

<var><pre>all channels = 255 if mean(pixel[0] + pixel[1] + pixel[2]) > 127</var>

<var>all channels = 0 if mean(pixel[0] + pixel[1] + pixel[2]) <= 127</pre></var>

<br/>

### Color to negative
[Back to description](./README.md#color-to-negative)

<code>--negative</code> command allows us to generated a new negative image by applying a specific formula for each color channels. 

<var><pre>all channels = 255 - pixel_value</pre></var>

<br/>

### Keep color channel
[back to description](./README.md#keep-color-channel)

<code>--colorchannel {g, b, r, gb, gr, br}</code> command allows us to generated a new image where only 1 or 2 color channels are kept by inhibiting color channels that are not wanted. That is to say by setting up inhibited color to 0 value (black).

<var><pre>green-image = inhibit blue + red channels</var>

<var>blue-image = inhibit red + green channels</var>

<var>red-image = inhibit green + blue channels</var>

<var>green-blue-image = inhibit red channel</var>

<var>green-red-image = inhibit blue channel</var>

<var>red-blue-image = inhibit green channel</pre></var>

<br/>

### Brightness adjustment
[back to description](./README.md#brightness-adjustment)

<code>--brightness brightness_value</code> command allows us to generate a new image after modifying the brightness of the image by updating each color channel of each pixel through this formula: 

<var><pre>all pixels = brightness + pixel</pre></var> 

brightness value is defined within [0, 255] interval

<br/>

### Flip image
[back to description](./README.md#flip-image)

<code>--flip</code> command allows us to generate a new flipped image by flipping every image pixels along its axis=1.

<br/>

### Filter: Edge-detection 
[back to description](./README.md#filter-edge-detection)

<br/>

### Filter: Edge-reinforcement
[back to description](./README.md#filter-edge-reinforcement)

<br/> 

### Filter: Blur
[back to description](./README.md#filter-blur)

<br/>

### Filter: Emboss
[back to description](./README.md#filter-emboss)

<br/>

### Color channel Histogram
[back to description](./README.md#color-channel-histogram)

<br/>

### Overlay two images 
[back to description](./README.md#overlay-two-images)

<br/>

### Image colorization
[back to description](./README.md#image-colorization)

<br/>

### Photomaton
[back to description](./README.md#photomaton)
