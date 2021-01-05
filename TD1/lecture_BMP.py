#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--lecture_BMP.py
import argparse 
import os
import sys
#import numpy as np

def affichage_pixel_RGB(image_name, file_size):
    """
    Affichage de la couleur d'un pixel de la matrice de l'image
    """
    i = 0
    octets = []

    f_lecture =open(image_name,'rb') 
    file_opened = True

    #get all bytes from the image
    while i < file_size:
        octet=f_lecture.read(1) 
        octets.append(ord(octet))
        i=i+1

    #image_bytes = np.array(octets[55, 60])
    #print(len(image_bytes))





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
    #bfType (2 bytes) 2
    print(" =>Magic Number =", octets, " BM => BitMap signature", "\n\n\t --Début En-tête du fichier BITMAPFILEHEADER--")

    #BLOC ENTETE 54 octets en standard 
    while (i<=54):
        octet=f_lecture.read(1) 
        octets.append(ord(octet))
        i=i+1

    #bfSize (4 bytes) 6
    size = []
    for j in range(2, 6):
        size.append(octets[j])
        print(hex(octets[j])[2:].upper().zfill(2), end=' ')
    print("\t\t=>Taille de Fichier = {} octets".format(
        str(int.from_bytes(size, byteorder='little'))))
    size_table = []
    for k in range(2, 6):
        size_table.append(octets[k])
    print("{}\t\t=>Taille de Fichier = {} octets".format(
        size_table, 
        str(int.from_bytes(size, byteorder='little'))))
    file_size = int.from_bytes(size, byteorder='little')
        
    #bfReserved1 (2bytes) 8
    application_image_1 = []
    for l in range(6, 8):
        application_image_1.append(octets[l])
        print(hex(octets[l])[2:].upper().zfill(2), end=' ')
    print("\t\t\t=>Application image (champ réservé 1) = {} noms".format(
        str(int.from_bytes(application_image_1, byteorder='little'))))

    #bfReserved2 (2 bytes) 10
    application_image_2 = []
    for l in range(8, 10):
        application_image_2.append(octets[l])
        print(hex(octets[l])[2:].upper().zfill(2), end=' ')
    print("\t\t\t=>Application image (champ réservé 2) = {} noms".format(
        str(int.from_bytes(application_image_2, byteorder='little'))))
   
    #bfOffBits (4 bytes) 14
    off_bits = []
    for m in range (10, 14):
        off_bits.append(octets[m])
        print(hex(octets[m])[2:].upper().zfill(2), end=' ')    
    print("\t\t=>Off Bits (adresse zone definition image) = {} octets".format(
        str(int.from_bytes(off_bits, byteorder='little'))))
        
    print("\n\t --Début En-tête du bitmap BITMAPINFOEADER--")

    #biSize (4 bytes) 18
    bisize = []
    for n in range (14, 18):
        bisize.append(octets[n])
        print(hex(octets[n])[2:].upper().zfill(2), end=' ')    
    print("\t\t=>Taille de l'entête BITMAPINFOHEADER = {} octets".format(
        str(int.from_bytes(bisize, byteorder='little'))))

    #biSize (4 bytes) 22
    largeur_image = []
    for n in range (18, 22):
        largeur_image.append(octets[n])
        print(hex(octets[n])[2:].upper().zfill(2), end=' ')    
    print("\t\t=>Largeur image = {} octets".format(
        str(int.from_bytes(largeur_image, byteorder='little'))))

    #biWidth (4 bytes) 26
    hauteur_image = []
    for o in range (22, 26):
        hauteur_image.append(octets[o])
        print(hex(octets[o])[2:].upper().zfill(2), end=' ')    
    print("\t\t=>Hauteur image = {} octets".format(
        str(int.from_bytes(hauteur_image, byteorder='little'))))

    #biPlanes (2 bytes) 28
    nb_plan_image = []
    for p in range (26, 28):
        nb_plan_image.append(octets[p])
        print(hex(octets[p])[2:].upper().zfill(2), end=' ')    
    print("\t\t\t=>NB plan image = {} plan".format(
        str(int.from_bytes(nb_plan_image, byteorder='little'))))

    #biBitCount (2 bytes) 30
    bit_count = []
    for p in range (28, 30):
        bit_count.append(octets[p])
        print(hex(octets[p])[2:].upper().zfill(2), end=' ')    
    print("\t\t\t=>Nombre de bits par pixel (couleur) = {} bits/pixel".format(
        str(int.from_bytes(bit_count, byteorder='little'))))

    #biCompression (4 bytes) 34
    compression = []
    for q in range (30, 34):
        compression.append(octets[q])
        print(hex(octets[q])[2:].upper().zfill(2), end=' ')    
    print("\t\t=>Type de compression = {}\
            \n\t\t\t\t->0=pas de compression\
            \n\t\t\t\t->1=compressé à 8 bits par pixel\
            \n\t\t\t\t->2=compressé à 4 bits par pixel".format(
        str(int.from_bytes(compression, byteorder='little'))))


    #biSizeImage (4 bytes) 38
    size_image = []
    for p in range (34, 38):
        size_image.append(octets[p])
        print(hex(octets[p])[2:].upper().zfill(2), end=' ')    
    print("\t\t=>Taille des données de l'image = {} octets".format(
        str(int.from_bytes(size_image, byteorder='little'))))

    #biXpelsPerMeter (4 bytes) 42
    xpels_per_meter = []
    for p in range (38, 42):
        xpels_per_meter.append(octets[p])
        print(hex(octets[p])[2:].upper().zfill(2), end=' ')    
    print("\t\t=>Résolution horizontale axe X = {} pixels/mètre".format(
        str(int.from_bytes(xpels_per_meter, byteorder='little'))))

    #biYpelsPerMeter (4 bytes) 46
    ypels_per_meter = []
    for p in range (42, 46):
        ypels_per_meter.append(octets[p])
        print(hex(octets[p])[2:].upper().zfill(2), end=' ')    
    print("\t\t=>Résolution verticale axe Y = {} pixels/mètre".format(
        str(int.from_bytes(ypels_per_meter, byteorder='little'))))

    #biClrUsed (4 bytes) 50
    clr_used = []
    for p in range (46, 50):
        clr_used.append(octets[p])
        print(hex(octets[p])[2:].upper().zfill(2), end=' ')    
    print("\t\t=>Nombre de couleurs dans l'image = {}\
            \n\t\t\t\t->0=maximum possible\
            \n\t\t\t\t->Si une palette est utilisée, ce nombre indique\
            \n\t\t\t\t  le nombre de couleurs de la palette".format(
        str(int.from_bytes(clr_used, byteorder='little'))))
    
    #biClrUsed (4 bytes) 54
    clr_important = []
    for p in range (50, 54):
        clr_important.append(octets[p])
        print(hex(octets[p])[2:].upper().zfill(2), end=' ')    
    print("\t\t=>Nombre de couleurs importantes dans l'image = {}\
            \n\t\t\t\t->0=toutes importantes".format(
        str(int.from_bytes(clr_important, byteorder='little'))))

    affichage_pixel_RGB(image_name, file_size)

    f_lecture.close