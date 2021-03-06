#!/usr/bin/env python3
# bmpProcessing.utils.Utils module
import numpy as np

def get_int_from_bytes(b_array):
    '''
    convert array of bytes into integer value
    '''
    return int.from_bytes(b_array, byteorder='little')


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def im2double(image):
    '''
    convert image from [0, 255] to [0, 1] interval
    '''
    return (image/255)


def double2im(image):
    '''
    convert iamge from [0, 1] to [0, 255] interval 
    '''
    return (image*255).astype('uint8')

def clamp(pixel):
    '''
    to truncate pixels within [0, 1] interval
    '''
    for i in range(0,len(pixel)):
        if pixel[i]<0:
            pixel[i] = 0
        else:
            if pixel[i]>1:
                pixel[i] = 1
  
    return(pixel)

def rgb2hsl(pixel):
    '''
    pixel must be within [0, 1] interval
    rgb2hsl convert rgb pixel into hsl format 
    hue saturation lightness
    '''
    r=pixel[0]
    g=pixel[1]
    b=pixel[2]
    
    cmax=max(r,g,b)
    cmin=min(r,g,b)
    delta=cmax-cmin
    
    # Lightness calculation
    l=(cmax+cmin)/2
    
    # Saturation calculation
    s=0
    if delta!=0:
        s=delta/(1-abs(2*l-1))
    
    # Hue calculation
    h=0
    if delta!=0:
        if cmax==r:
            h=(((g-b)/delta)%6)*60
        
        if cmax==g:
            h=(2+(b-r)/delta)*60
        
        if cmax==b:
            h=(4+(r-g)/delta)*60
    
    return([h,s,l])


def hsl2rgb(pixel):
    '''
    pixel must be within [0, 1] interval
    hsl2rgb convert rgb pixel into hsl format 
    red green blue
    '''
    h=pixel[0]
    s=pixel[1]
    l=pixel[2]
    
    c=(1-abs(2*l-1))*s
    x=c*(1-abs((h/60)%2-1))
    
    r=0
    g=0
    b=0
    
    if h>=0 and h<60:
        r=c
        g=x
    
    if h>=60 and h<120:
        r=x
        g=c
    
    if h>=120 and h<180:
        g=c
        b=x
    
    if h>=180 and h<240:
        g=x
        b=c
    
    if h>=240 and h<300:
        r=x
        b=c
    
    if h>=300 and h<360:
        r=c
        b=x
    
    m=l-c/2
    return clamp([r+m,g+m,b+m])


def im_hsl2rgb(image):
    for row in image:
        for pixel in row:
            pixel = hsl2rgb(pixel)
    return image


def im_rgb2hsl(image):
    for row in image:
        for pixel in row:
            pixel = rgb2hsl(pixel)
    return image


def change_hue(image, angle):
    for row in image:
        for pixel in row:
            pixel[0] = (angle)/360 #pixel[0] = hue
                                            #pixel[1] = saturation
                                            #pixel[2] = lightness
    return image