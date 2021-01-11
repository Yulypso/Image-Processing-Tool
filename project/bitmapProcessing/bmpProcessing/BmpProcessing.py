#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

class BmpProcessing: 
    '''
    Implementation of an BMP format image
    '''

    def __init__(self, img, verbose):
        '''
        Initialisation of the bitmap header in ndarray
        img: ../path/to/image.bmp
        '''
        self.img = img
        self.verbose = verbose
        #whole bytes from bitmap
        self.octets = []
        #image bytes from bitmap into matrix
        self.image_matrix = None 
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
        #Palette de couleur
        self.b_palette = []


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
        self.b_palette = self.octets[54:self.get_int_from_bytes(
            self.bf_offbits.tolist())]
            
        #Afin de tenir compte des offbits
        self.image_matrix = self.octets[
                self.get_int_from_bytes(self.bf_offbits.tolist()):
            ].reshape(
            self.get_int_from_bytes(self.bi_height.tolist()),
            self.get_int_from_bytes(self.bi_width.tolist()), 
            int(self.get_int_from_bytes(self.bi_bitcount.tolist())/8))

        if self.verbose:
            print('image successfully loaded\n')
        

    def contrast_image(self, contrast):
        #calcul du facteur de contrast
        factor = (259 * (contrast + 255)) / (255 * (259 - contrast))
        for row in self.image_matrix:
            for pixel in row:
                pixel[0] = round(factor * (pixel[0] - 128) + 128) #bleu
                pixel[1] = round(factor * (pixel[1] - 128) + 128) #vert
                pixel[2] = round(factor * (pixel[2] - 128) + 128) #rouge
                #Si le pixel calculé n'appartient pas à [0, 255] on le truncate
                if pixel[0] > 255:
                    pixel[0] = 255
                elif pixel[0] < 0:
                    pixel[0] = 0
                if pixel[1] > 255:
                    pixel[1] = 255
                elif pixel[1] < 0:
                    pixel[1] = 0
                if pixel[2] > 255:
                    pixel[2] = 255
                elif pixel[2] < 0:
                    pixel[2] = 0
        
                        
    def resize_image(self, factor):
        if len(factor) == 2:
            new_width = int(factor[0])
            new_height = int(factor[1])
        else:
            new_width = factor[0] * self.get_int_from_bytes(self.bi_width.tolist())
            new_height = factor[0] * self.get_int_from_bytes(self.bi_height.tolist())

        nb_cols = np.shape(self.image_matrix)[1] #width
        nb_rows = np.shape(self.image_matrix)[0] #height

        self.image_matrix = [
            [self.image_matrix[int(nb_rows * a / new_height)]
                              [int(nb_cols * b / new_width)]
                    for b in range(new_width)
            ] for a in range(new_height)
        ]

        self.bf_size = []
        for i in (  int(
                        (np.shape(self.image_matrix)[1]) 
                    ) * 
                    int(
                            (np.shape(self.image_matrix)[0]) 
                    ) * 
                    int(self.get_int_from_bytes(self.bi_bitcount.tolist())/8) 
                    + int(self.get_int_from_bytes(self.bf_offbits.tolist()))
                ).to_bytes(4, byteorder='little'):
            self.bf_size.append(i)
        self.bf_size = np.array(self.bf_size)

        self.bi_sizeimage = []
        for i in (  int(
                        (np.shape(self.image_matrix)[1]) 
                    ) * 
                    int(
                        (np.shape(self.image_matrix)[0]) 
                    ) * 
                    int(self.get_int_from_bytes(self.bi_bitcount.tolist())/8) 
                ).to_bytes(4, byteorder='little'):
            self.bi_sizeimage.append(i)
        self.bi_sizeimage = np.array(self.bi_sizeimage)

        if self.verbose:
            print("{} has been resized to {} x {}".format(
                             self.img.replace('../images/',''),
                                                    new_width, 
                                                    new_height))
        

    def rotate_image(self, degree):
        '''
        Rotate an image by a degree
        '''
        if degree == 0: 
            nb_rot = 0
        elif degree == 90: 
            nb_rot = 1
        elif degree == 180:
            nb_rot = 2
        elif degree == 270:
            nb_rot = 3
        else:
            raise Exception("Invalid rotation degree, Try Again")

        self.image_matrix = np.rot90(self.image_matrix, k=nb_rot)

        if self.verbose:
            print("{} has been rotated to {} degree".format(self.img, degree))


    def save_image(self, output):
        bi_width = []
        for i in np.shape(self.image_matrix)[1].to_bytes(4, byteorder='little'):
            bi_width.append(i)
        self.bi_width = np.array(bi_width)

        bi_height = []
        for i in np.shape(self.image_matrix)[0].to_bytes(4, byteorder='little'):
            bi_height.append(i)
        self.bi_height = np.array(bi_height)

        flattened = np.array(self.image_matrix).flatten().tolist()
        octets = self.octets[
            :self.get_int_from_bytes(self.bf_offbits.tolist())].tolist()
        [octets.append(i) for i in flattened]
        self.octets = np.array(octets)

        f_output = open(output, 'wb')
        f_output.write(bytearray(self.bf_type.tolist()))
        f_output.write(bytearray(self.bf_size.tolist()))
        f_output.write(bytearray(self.bf_reserved1.tolist()))
        f_output.write(bytearray(self.bf_reserved2.tolist()))
        f_output.write(bytearray(self.bf_offbits.tolist()))
        f_output.write(bytearray(self.bi_size.tolist()))
        f_output.write(bytearray(self.bi_width.tolist()))
        f_output.write(bytearray(self.bi_height.tolist()))
        f_output.write(bytearray(self.bi_planes.tolist()))
        f_output.write(bytearray(self.bi_bitcount.tolist()))
        f_output.write(bytearray(self.bi_compression.tolist()))
        f_output.write(bytearray(self.bi_sizeimage.tolist()))
        f_output.write(bytearray(self.bi_xpelspermeter.tolist()))
        f_output.write(bytearray(self.bi_ypelspermeter.tolist()))
        f_output.write(bytearray(self.bi_clrused.tolist()))
        f_output.write(bytearray(self.bi_clrimportant.tolist()))
        f_output.write(bytearray(self.b_palette.tolist()))
        f_output.write(bytearray(self.octets[self.get_int_from_bytes(
            self.bf_offbits.tolist()):].tolist()))
        f_output.close
        print('generated image has been saved to {}'.format(output))


    def display_pixels(self):
        '''
        Display pixels of image
        '''
        if self.verbose:
            print("\nAffichage de la matrice de pixel [ Bleu Vert Rouge ]")
        print(self.image_matrix)
        

    def display_header(self):
        '''
        Display information about the bitmap header 
        '''
        print('Bitmap header information')
        print (" dec=",self.bf_type[0], 
                " hexa=", hex(self.bf_type[0])[2:].upper()) 
        print (" dec=",self.bf_type[1], 
                " hexa=", hex(self.bf_type[1])[2:].upper())

        print(" =>Magic Number =", self.bf_type, " BM => BitMap signature", 
        "\n\n\t --BITMAP FILE HEADER--")

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

        print("\n\t --BITMAP INFO HEADER--")
        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_size], 
            end=' ')
        print("\t\t=>Taille de l'entête BITMAP INFO HEADER = {} octets".format(
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
        str(int.from_bytes(self.bi_xpelspermeter.tolist(), 
            byteorder='little'))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_ypelspermeter], 
            end=' ')
        print("\t\t=>Résolution verticale axe Y = {} pixels/mètre".format(
        str(int.from_bytes(self.bi_ypelspermeter.tolist(), 
            byteorder='little'))))

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
        str(int.from_bytes(self.bi_clrimportant.tolist(), 
            byteorder='little'))))


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
