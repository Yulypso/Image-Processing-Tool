#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

class imageBmp: 
    '''
    Implementation of an BMP format image
    img: ../path/to/image.bmp
    '''

    def __init__(self, img):
        '''
        Initialisation of the bitmap header in ndarray
        '''
        self.img = img
        self.octets = []
        #BITMAP FILE HEADER (ascii bytes)
        self.bf_type = None
        self.bf_size = None
        self.bf_reserved1 = None
        self.bf_reserved2 = None
        self.bf_offbits = None
        #BITMAP INFO HEADER (ascii bytes)
        self.bi_size = None
        self.bi_width = None
        self.bi_height = None
        self.bi_planes = None
        self.bi_bitcount = None
        self.bi_compression = None
        self.bi_sizeimage = None
        self.bi_xpelspermeter = None
        self.bi_ypelspermeter = None
        self.bi_clrused = None
        self.bi_clrimportant = None

    def fit(self):
        self.ouverture_fichiers_image()
        self.bf_type = self.octets[0:2]
        self.bf_size = self.octets[2:6]
        self.bf_reserved1 = self.octets[6:8]
        self.bf_reserved2 = self.octets[8:10]
        self.bf_offbits = self.octets[10:14]
        self.bi_size = self.octets[14:18]
        self.bi_width = self.octets[18:22]
        self.bi_height = self.octets[22:26]
        self.bi_planes = self.octets[26:28]
        self.bi_bitcount = self.octets[28:30]
        self.bi_compression = self.octets[30:34]
        self.bi_sizeimage = self.octets[34:38]
        self.bi_xpelspermeter = self.octets[38:42]
        self.bi_ypelspermeter = self.octets[42:46]
        self.bi_clrused = self.octets[46:50]
        self.bi_clrimportant = self.octets[50:54]

    def display_header(self):
        '''
        Display information about the bitmap header 
        '''
        print (" dec=",self.bf_type[0], 
                " hexa=", hex(self.bf_type[0])[2:].upper()) 
        print (" dec=",self.bf_type[1], 
                " hexa=", hex(self.bf_type[1])[2:].upper())

        print(" =>Magic Number =", self.bf_type, " BM => BitMap signature", 
        "\n\n\t --Début En-tête du fichier BITMAPFILEHEADER--")

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bf_size], end=' ')
        print("\t\t=>Taille de Fichier = {} octets".format(
        str(int.from_bytes(self.bf_size.tolist(), byteorder='little'))))

        print(self.bf_size.tolist(), end=' ')
        print("\t=>Taille de Fichier = {} octets".format(
        str(int.from_bytes(self.bf_size.tolist(), byteorder='little'))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bf_reserved1], 
            end=' ')
        print("\t\t\t=>Application image (champ réservé 1) = {} noms".format(
        str(int.from_bytes(self.bf_reserved1.tolist(), byteorder='little'))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bf_reserved2], 
            end=' ')
        print("\t\t\t=>Application image (champ réservé 2) = {} noms".format(
        str(int.from_bytes(self.bf_reserved2.tolist(), byteorder='little'))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bf_offbits], 
            end=' ')
        print("\t\t=>Off Bits (adresse zone definition image) = {} octets\
            ".format(
        str(int.from_bytes(self.bf_offbits.tolist(), byteorder='little'))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_size], 
            end=' ')
        print("\t\t=>Taille de l'entête BITMAPINFOHEADER = {} octets".format(
        str(int.from_bytes(self.bi_size.tolist(), byteorder='little'))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_width], 
            end=' ')
        print("\t\t=>Largeur image = {} octets".format(
        str(int.from_bytes(self.bi_width.tolist(), byteorder='little'))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_height], 
            end=' ')
        print("\t\t=>Hauteur image = {} octets".format(
        str(int.from_bytes(self.bi_height.tolist(), byteorder='little'))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_planes], 
            end=' ')
        print("\t\t\t=>NB plan image = {} plan".format(
        str(int.from_bytes(self.bi_planes.tolist(), byteorder='little'))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_bitcount], 
            end=' ')
        print("\t\t\t=>Nombre de bits par pixel = {} bits/pixel".format(
        str(int.from_bytes(self.bi_bitcount.tolist(), byteorder='little'))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_compression], 
            end=' ')
        print("\t\t=>Type de compression = {}\
            \n\t\t\t\t->0=pas de compression\
            \n\t\t\t\t->1=compressé à 8 bits par pixel\
            \n\t\t\t\t->2=compressé à 4 bits par pixel".format(
        str(int.from_bytes(self.bi_compression.tolist(), byteorder='little'))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_sizeimage], 
            end=' ')
        print("\t\t=>Taille des données de l'image = {} octets".format(
        str(int.from_bytes(self.bi_sizeimage.tolist(), byteorder='little'))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_xpelspermeter], 
            end=' ')
        print("\t\t=>Résolution horizontale axe X = {} pixels/mètre".format(
        str(int.from_bytes(self.bi_xpelspermeter.tolist(), byteorder='little'))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_ypelspermeter], 
            end=' ')
        print("\t\t=>Résolution verticale axe Y = {} pixels/mètre".format(
        str(int.from_bytes(self.bi_ypelspermeter.tolist(), byteorder='little'))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_clrused], 
            end=' ')
        print("\t\t=>Nombre de couleurs dans l'image = {}\
            \n\t\t\t\t->0=maximum possible\
            \n\t\t\t\t->Si une palette est utilisée, ce nombre indique\
            \n\t\t\t\t  le nombre de couleurs de la palette".format(
        str(int.from_bytes(self.bi_clrused.tolist(), byteorder='little'))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_clrimportant], 
            end=' ')
        print("\t\t=>Nombre de couleurs importantes dans l'image = {}\
            \n\t\t\t\t->0=toutes importantes".format(
        str(int.from_bytes(self.bi_clrimportant.tolist(), byteorder='little'))))

    def ouverture_fichiers_image(self):
        '''
        1. Open the image
        2. Get the size of the image
        3. Get all bytes of the image
        '''
        f_lecture = open(self.img,'rb')
        i = 0
        while (i < 6):
            octet = f_lecture.read(1) 
            self.octets.append(ord(octet))
            i += 1
        self.bf_size = self.get_int_from_bytes([k for k in self.octets[2:]])

        while i < self.bf_size:
            octet = f_lecture.read(1) 
            self.octets.append(ord(octet))
            i += 1
        self.octets = np.array(self.octets)
        f_lecture.close

    def get_int_from_bytes(self, b_array):
        return int.from_bytes(b_array, byteorder='little')
