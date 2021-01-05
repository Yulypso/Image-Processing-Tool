#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse 
import os 
import sys

def ouverture_Fichiers_Image(image_name):
    """
    Analyse du header de l'image ouvert
    """
    #read in binary mode
    f_lecture =open(image_name,'rb') 
    i=1
    octet = bytes([0])
    octets=[]

    #Lecture du MAGIC NUMBER
    #lecture Magic number sur 2 octets
    while (i <=2): 
        #Lecture octet par octet 
        octet=f_lecture.read(1) 
        octets.append(ord(octet))
        print (octet.decode('utf-8'),
                            " dec=",ord(octet), 
                            " hexa=", 
                            hex(ord(octet))[2:].upper()) 
        i=i+1
    print(" =>Magic Number =", octets, " BM => BitMap")

    #BLOC ENTETE 54 octets en standard 
    while (i<=54):
        octet=f_lecture.read(1) 
        octets.append(ord(octet))
        i=i+1

    #line 1
    size = []
    for j in range(2, 6):
        size.append(octets[j])
        print(hex(octets[j])[2:].upper().zfill(2), end=' ')
    print("\t\t=>Taille de Fichier = {} octets".format(
        str(int.from_bytes(size, byteorder='little'))))

    #line 2
    size_table = []
    for k in range(2, 6):
        size_table.append(octets[k])
    print("{}\t\t=>Taille de Fichier = {} octets".format(
        size_table, 
        str(int.from_bytes(size, byteorder='little'))))
        
    #line 3
    application_image = []
    for l in range(6, 10):
        application_image.append(octets[l])
        print(hex(octets[l])[2:].upper().zfill(2), end=' ')
    print("\t\t=>Application image = {} noms".format(
        str(int.from_bytes(application_image, byteorder='little'))))
   
    #line 4
    taille_entete = []
    for m in range (10, 14):
        taille_entete.append(octets[m])
        print(hex(octets[m])[2:].upper().zfill(2), end=' ')    
    print("\t\t=>Taille entete = {} octets".format(
        str(int.from_bytes(taille_entete, byteorder='little'))))

    #line 5
    largeur_image = []
    for n in range (18, 22):
        largeur_image.append(octets[n])
        print(hex(octets[n])[2:].upper().zfill(2), end=' ')    
    print("\t\t=>Largeur image = {} octets".format(
        str(int.from_bytes(largeur_image, byteorder='little'))))

    #line 6
    hauteur_image = []
    for o in range (18, 22):
        hauteur_image.append(octets[o])
        print(hex(octets[o])[2:].upper().zfill(2), end=' ')    
    print("\t\t=>Hauteur image = {} octets".format(
        str(int.from_bytes(hauteur_image, byteorder='little'))))

    #line 7
    nb_plan_image = []
    for p in range (26, 28):
        nb_plan_image.append(octets[p])
        print(hex(octets[p])[2:].upper().zfill(2), end=' ')    
    print("\t\t\t=>NB plan image = {} plan".format(
        str(int.from_bytes(nb_plan_image, byteorder='little'))))

    #line 7
    couleur_image = []
    for q in range (28, 30):
        couleur_image.append(octets[q])
        print(hex(octets[q])[2:].upper().zfill(2), end=' ')    
    print("\t\t\t=>Couleur image = {} couleurs".format(
        str(int.from_bytes(couleur_image, byteorder='little'))))

    f_lecture.close


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
    if not os.path.isfile(file_name):
        print('"{}" does not exist'.format(file_name), file=sys.stderr)
        sys.exit(-1)
        
    print('Success Opening {}...'.format(file_name))
    ouverture_Fichiers_Image(file_name)


if __name__ == '__main__': 
    """
    To run: python3 lecture_BMP.py --bmp images/<IMAGE>
    """
    process_bmp() 
    sys.exit(0)