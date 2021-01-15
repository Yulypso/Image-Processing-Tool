#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse 
import os 
import sys
import numpy as np
import bmpProcessing.BmpProcessing as BmpProcessing

def check_interval(value):
    '''
    Check argument parser if value belongs to [-255, +255] interval
    '''
    if (int(value) < -255) or (int(value) > 255):
        raise argparse.ArgumentTypeError(
            "{} is an incorrect value. Please ".format(value)+
            "choose a value between [-255, +255]")
    return int(value)


def check_resize_ratio(value):
    '''
    Check argument parser if value belongs to ]0, +inf[ interval
    '''
    if float(value) <= 0:
        raise argparse.ArgumentTypeError(
            "{} is an incorrect ratio value. \n\t\tPlease ".format(value)+
            "choose a strictly positive ratio value (float)")
    return value


def check_display_pixel_option(value):
    '''
    check display pixel option
    1. if display all pixels, return str
    2. if position option : value must belongs to [-255, +255] inteval
    '''
    if 'all' in str(value): 
        return str(value)
    else:
        if (int(value) < -255) or (int(value) > 255):
            raise argparse.ArgumentTypeError(
            "{} is an incorrect value. Please ".format(value)+
            "choose a value between [-255, +255]")
        return int(value)


def process_bmp():
    '''
    Bitmap processing
    1. get argument from Argument Parser
    2. verify if the input bitmap file exists or not
    3. features application on the input bitmap file
    '''
    # Adding argument in the parser
    parser = argparse.ArgumentParser(description='--Bitmap processing tool--')
    parser.add_argument('--bmp', 
                        metavar = '<file_name.bmp>', 
                        help = 'image file to parse and gives header information', 
                        required = True)
    parser.add_argument('--rotate',
                        '-rt',
                        metavar = '<rotation degree>',
                        help = 'degree of image rotation [90, 180, 270]',
                        type = int,
                        choices = [0, 90, 180, 270],
                        required = False)
    parser.add_argument('--resize',
                        '-rs',
                        metavar = '<resizing ratio> or [<width> <height>]',
                        type = check_resize_ratio,
                        help = 'ratio of image resizing',
                        required = False,
                        nargs='+')
    parser.add_argument('--contrast',
                        '-ct',
                        metavar = '<contrast value>',
                        type = check_interval,
                        help = 'image contrast [-255, +255]',
                        required = False)
    parser.add_argument('--brightness',
                        '-bn',
                        metavar = '<brightness value>',
                        type = check_interval,
                        help = 'image brightness [-255, +255]',
                        required = False)
    parser.add_argument('--verbose',
                        '-v',
                        help = 'get more information',
                        action='store_true',
                        required = False)
    parser.add_argument('--flip',
                        '-fp',
                        help = 'image flip',
                        action='store_true',
                        required = False)
    parser.add_argument('--grayscale',
                        '-gs',
                        metavar = '<grayscale method>',
                        help = 'image grayscale <mean> or <luminance>',
                        type = str,
                        choices = ['mean', 'luminance'],
                        required = False)
    parser.add_argument('--negative', 
                        '-n',
                        help = 'image negative',
                        action='store_true',
                        required = False)
    parser.add_argument('--color', 
                        '-cl',
                        metavar = '<color>',
                        choices = ['r', 'g', 'b', 'rg', 'rb', 'gb', 'gr', 'br', 'bg'],
                        type = str,
                        help = "image color adjustment ['r', 'g', 'b', 'rg', 'rb', 'gb']",
                        required = False)
    parser.add_argument('--blackwhite', 
                        '-bw',
                        help = 'image black & white',
                        action='store_true',
                        required = False)
    parser.add_argument('--pixels',
                        '-p',
                        metavar = '<display option>',
                        help = '<all> or <pos x> <pos y>',
                        type = check_display_pixel_option,
                        required = False,
                        nargs='+')
    parser.add_argument('--histogram',
                        '-hg',
                        help = 'display input image histogram',
                        action='store_true',
                        required = False)
    parser.add_argument('--filter', 
                        '-ft',
                        metavar = '<filter type>',
                        choices = ['edge'],
                        type = str,
                        help = "image filter ['edge']",
                        required = False)
    parser.add_argument('--output',
                        '-o',
                        help = 'generated file',
                        metavar = '<file_name.bmp>',
                        required = '--resize' in sys.argv or 
                                   '-rs' in sys.argv or
                                   '--rotate' in sys.argv or
                                   '-rt' in sys.argv or
                                   '--contrast' in sys.argv or
                                   '-c' in sys.argv or
                                   '--brightness' in sys.argv or
                                   '-bn' in sys.argv or
                                   '--rotate' in sys.argv or
                                   '-rt' in sys.argv or
                                   '--flip' in sys.argv or
                                   '-fp' in sys.argv or
                                   '--blackwhite' in sys.argv or
                                   '-bw' in sys.argv or
                                   '--color' in sys.argv or
                                   '-cl' in sys.argv or
                                   '--negative' in sys.argv or
                                   '-n' in sys.argv or
                                   '--filter' in sys.argv or
                                   '-ft' in sys.argv or
                                   '--grayscale' in sys.argv or
                                   '-gs' in sys.argv 
                        )

    # get arguments from parser
    args = parser.parse_args()
    input_file_name = args.bmp
    pixels = args.pixels
    rotation_degree = args.rotate
    ratio_resize = args.resize
    contrast_value = args.contrast
    brightness_value = args.brightness
    flip = args.flip
    grayscale = args.grayscale
    blackwhite = args.blackwhite
    negative = args.negative
    color = args.color
    filter_type = args.filter
    verbose = args.verbose
    histogram = args.histogram
    output_file_name = args.output

    # Display which argument have been selected
    print('--- Bitmap processing tool ---')
    if input_file_name:
        if '.bmp' not in input_file_name: 
            # add .bmp extension on input file if it has been forgotten
            input_file_name = input_file_name + '.bmp'
    
        print('[X] input file name:       ', input_file_name)
        input_file_name = '../../images/' + input_file_name

    print('[X] rotation degree:       ', rotation_degree) if rotation_degree else print('[ ] rotation degree:        Default')
    print('[X] contrast value:        ', contrast_value) if contrast_value else print('[ ] contrast value:         Default')
    print('[X] brightness value:      ', brightness_value) if brightness_value else print('[ ] brightness value:       Default')
    print('[X] flip image:            ', flip) if flip else print('[ ] flip image:             False')
    print('[X] grayscale image:       ', grayscale) if grayscale else print('[ ] grayscale image:        False')
    print('[X] black & white image:   ', blackwhite) if blackwhite else print('[ ] black & white image:    False')
    print('[X] negative image:        ', negative) if negative else print('[ ] negative image:         False')
    print('[X] image color adjustment:', color) if color else print('[ ] image color adjustment: None')
    print('[X] image filter:          ', filter_type) if filter_type else print('[ ] image filter:           None')
    print('[X] verbose:               ', verbose) if verbose else print('[ ] verbose:                False')
    print('[X] histogram:             ', histogram) if histogram else print('[ ] histogram:              False')
    
    if pixels:
        if len(pixels) == 2:
            print('[X] display pixels:         ({}, {})'.format(pixels[0], pixels[1]))
        elif len(pixels) == 1:
            print('[X] display pixels:         {}'.format(pixels[0]))
    else:
        print('[ ] display pixels:         False')

    if ratio_resize:
        if len(ratio_resize) == 2:
            print('[X] ratio size:             {} x {}'.format(ratio_resize[0], ratio_resize[1]))
        elif len(ratio_resize) == 1:
            print('[X] ratio size:             {}'.format(ratio_resize[0]))
    else:
        print('[ ] ratio size:             Default')
   
    if output_file_name:
        if '.bmp' not in output_file_name:
            # add .bmp extension on output file if it has been forgotten
            output_file_name = output_file_name + '.bmp'
        print('[X] output file name:      ', output_file_name)
        output_file_name = '../../images/generated/' + output_file_name
    else:
        print('[ ] output file name:       None')
        
    print('------------------------------\n')

    # verify if input file exists or not
    if not os.path.isfile(input_file_name):
        print('Error: "{}" does not exist'.format(input_file_name), file=sys.stderr)
        sys.exit(-1)
    else:
        print('Opening {} successfully\n'.format(input_file_name))

    # Features application if arguments exists in parser
    my_bmp = BmpProcessing.BmpProcessing(input_file_name, verbose)

    #processing only if output file or histogram needed
    if output_file_name or histogram or pixels:
        is_processing = True
    else:
        is_processing = False
    my_bmp.fit(is_processing)

    # display bitmap header
    my_bmp.display_header()

    if histogram:
        my_bmp.display_histogram()
    if pixels:
        my_bmp.display_pixels(pixels)
    if grayscale:
        my_bmp.grayscale_image(grayscale)
    if filter_type:
        my_bmp.filter_image(filter_type)
    if blackwhite:
        my_bmp.blackwhite_image()
    if color:
        my_bmp.color_image(color)
    if contrast_value:
        my_bmp.contrast_image(contrast_value)
    if brightness_value:
        my_bmp.brightness_image(brightness_value)
    if negative:
        my_bmp.negative_image()
    if ratio_resize:
        my_bmp.resize_image(ratio_resize)
    if flip:
        my_bmp.flip_image()
    if rotation_degree:
        my_bmp.rotate_image(rotation_degree)
    if output_file_name:
        my_bmp.save_image(output_file_name)


def main():
    process_bmp() 
    sys.exit(0)


if __name__ == "__main__":
    main()