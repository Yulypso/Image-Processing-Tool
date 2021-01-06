#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse 
import os 
import sys
import lecture_BMP as lecture_BMP
from imageBmp import imageBmp 

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
    #lecture_BMP.ouverture_Fichiers_Image(file_name)

    my_bmp = imageBmp(file_name)
    my_bmp.fit()


def main():
    """
    To run: python3 🐛.py --bmp ../images/<IMAGE_NAME>.bmp
    """
    process_bmp() 
    sys.exit(0)


if __name__ == "__main__":
    main()