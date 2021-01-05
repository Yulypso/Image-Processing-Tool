#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse 
import os 
import sys

def ouverture_Fichiers_Image(image_name):
    #read in binary mode
    f_lecture =open(image_name,'rb') 
    i=1
    octet = bytes([0])
    octets=[]

    #Lecture du MAGIC NUMBER
    #lecture Magic number sur 2 octets
    while (i <=2): 
        #Lecture octet par octet 
        octets.append(ord(octet))
        octet=f_lecture.read(1) 
        print (octet.decode('utf-8')," dec=",ord(octet)) 
        i=i+1
    print(" =>Magic Number =", octets, " BM => BitMap")

    #BLOC ENTETE 54 octets en standard 
    while (i<=54):
        octet=f_lecture.read(1) 
        i=i+1

    f_lecture.close

def process_bmp():
    parser = argparse.ArgumentParser(description='BMP reader')
    parser.add_argument('--bmp', 
                        metavar='<bmp file name>', 
                        help='image file to parse', 
                        default= 'image.bmp',
                        required=True)
    args = parser.parse_args()
    
    file_name = args.bmp
    if not os.path.isfile(file_name):
        print('"{}" does not exist'.format(file_name), file=sys.stderr)
        sys.exit(-1)
        
    print('Success Opening {}...'.format(file_name))
    ouverture_Fichiers_Image(file_name)

if __name__ == '__main__': 
    process_bmp() 
    sys.exit(0)