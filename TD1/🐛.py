#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse 
import os 
import sys
import numpy as np
from imageBmp import ImageBmp 

def process_bmp():
    """
    Lecture et ouverture de l'image en format bmp
    """
    parser = argparse.ArgumentParser(description='BMP reader')
    parser.add_argument('--bmp', 
                        metavar='<bmp file name>', 
                        help='image file to parse', 
                        default= 'image.bmp',
                        required=True)
    args = parser.parse_args()
    
    file_name = args.bmp
    print(file_name)
    if not os.path.isfile(file_name):
        print('"{}" does not exist'.format(file_name), file=sys.stderr)
        sys.exit(-1)
        
    print('Success Opening {}...'.format(file_name))
    my_bmp = ImageBmp(file_name)
    my_bmp.fit()
    my_bmp.display_header()
    my_bmp.display_pixels()
    my_bmp.rotate_image(90)
    my_bmp.save_image('../images/🐼.bmp')


def main():
    """
    To run: python3 🐛.py --bmp ../images/<IMAGE_NAME>.bmp
    """
    process_bmp() 
    sys.exit(0)


if __name__ == "__main__":
    main()