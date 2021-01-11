#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse 
import os 
import sys
import numpy as np
import bmpProcessing.BmpProcessing as BmpProcessing

def check_contrast_interval(value):
    if (int(value) < -255) or (int(value) > 255):
        raise argparse.ArgumentTypeError(
            "{} is an incorrect contrast value. Please ".format(value)+
            "choose a value between [-255, +255]")
    return int(value)

def check_resize_ratio(value):
    if float(value) <= 0:
        raise argparse.ArgumentTypeError(
            "{} is an incorrect ratio value. \n\t\tPlease ".format(value)+
            "choose a strictly positive ratio value (float)")
    return value

def process_bmp():
    """
    Lecture et ouverture de l'image en format bmp
    """
    parser = argparse.ArgumentParser(description='--Bitmap processing tool--')
    parser.add_argument('--bmp', 
                        metavar = '<file_name.bmp>', 
                        help = 'image file to parse', 
                        required = True)
    parser.add_argument('--rotate',
                        '-rt',
                        metavar = '<rotation degree>',
                        help = 'degree of image rotation',
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
                        '-c',
                        metavar = '<contrast value>',
                        type = check_contrast_interval,
                        help = 'image contrast',
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
                        help = 'image grayscale',
                        action='store_true',
                        required = False)
    parser.add_argument('--pixels',
                        '-p',
                        help = 'display input image pixels',
                        action='store_true',
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
                                   '--rotate' in sys.argv or
                                   '-rt' in sys.argv or
                                   '--flip' in sys.argv or
                                   '-fp' in sys.argv or
                                   '--grayscale' in sys.argv or
                                   '-gs' in sys.argv 
                        )
    args = parser.parse_args()

    print('--- Bitmap processing tool ---')
    input_file_name = args.bmp
    if input_file_name:
        print('input file name:', input_file_name)
        input_file_name = '../../images/' + args.bmp

    pixels = args.pixels
    print('display pixels:', pixels) if pixels else print('display pixels: False')

    rotation_degree = args.rotate
    print('rotation degree:', rotation_degree) if rotation_degree else print('rotation degree: Default')
    
    ratio_resize = args.resize
    if ratio_resize:
        print('ratio size: {} x {}'.format(ratio_resize[0], ratio_resize[1])) if len(ratio_resize) == 2 else print('ratio size: Default')
        print('ratio size: {}'.format(ratio_resize[0])) if len(ratio_resize) == 1 else print('ratio size: Default')

    contrast_value = args.contrast
    print('contrast value:', contrast_value) if contrast_value else print('contrast value: Default')

    flip = args.flip
    print('flip image:', flip) if flip else print('flip image: False')

    grayscale = args.grayscale
    print('grayscale image:', grayscale) if grayscale else print('grayscale image: False')

    verbose = args.verbose
    print('verbose:', verbose) if verbose else print('verbose: False')

    output_file_name = args.output
    if output_file_name:
        if '.bmp' not in output_file_name:
            output_file_name = output_file_name + '.bmp'
        print('output file name:', output_file_name)
        output_file_name = '../../images/generated/' + output_file_name


    print('------------------------------\n')

    if not os.path.isfile(input_file_name):
        print('"{}" does not exist'.format(input_file_name), file=sys.stderr)
        sys.exit(-1)
        
    print('Opening {} successfully\n'.format(input_file_name))

    my_bmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    if output_file_name:
        is_processing = True
    else:
        is_processing = False
    my_bmp.fit(is_processing)
    my_bmp.display_header()
    if pixels:
        my_bmp.display_pixels()
    if contrast_value:
        my_bmp.contrast_image(contrast_value)
    if grayscale:
        my_bmp.grayscale_image()
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