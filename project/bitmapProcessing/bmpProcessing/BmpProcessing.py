#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from bmpProcessing.utils.Utils import get_int_from_bytes
import timeit

class BmpProcessing: 
    '''
    Implementation of an BMP format image
    '''

    def __init__(self, img, verbose):
        '''
        Initialisation BmpProcessing variables
        '''
        # input file name
        self.img = img

        # verbose to display more information
        self.verbose = verbose

        # all bitmap bytes 
        self.octets = []

        # bitmap image bytes in matrix format
        self.image_matrix = None 

        #BITMAP FILE HEADER 
        self.bf_type = None
        self.bf_size = None
        self.bf_reserved1 = None
        self.bf_reserved2 = None
        self.bf_offbits = None

        #BITMAP INFO HEADER
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

        # Bitmap palette
        self.b_palette = []


    def fit(self, is_processing):
        '''
        Fit the bitmap header
        1. if output is required we fit the bitmap palette and image bytes
        '''
        if self.verbose:
            #-------performance calculation--------
            starttime = timeit.default_timer()
            print("Start fitting time:", starttime)
            #--------------------------------------

        # fit all bitmap bytes into self.octets
        self.ouverture_fichiers_image()

        #file header
        self.bf_type = self.octets[0:2]
        self.bf_size = self.octets[2:6]
        self.bf_reserved1 = self.octets[6:8]
        self.bf_reserved2 = self.octets[8:10]
        self.bf_offbits = self.octets[10:14]

        #file info
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

        # if output or histogram is required
        if is_processing:
            # fit bitmap palette
            self.b_palette = self.octets[54:get_int_from_bytes(self.bf_offbits.tolist())]

            # fit image matrix with bitmap image bytes
            self.image_matrix = self.octets[get_int_from_bytes(self.bf_offbits.tolist()):].reshape(
                    get_int_from_bytes(self.bi_height.tolist()),
                    get_int_from_bytes(self.bi_width.tolist()), 
                    int(get_int_from_bytes(self.bi_bitcount.tolist())/8)
                )

        if self.verbose:
            print('image successfully loaded\n')
            #-------performance calculation--------
            print("Fitting duration:", timeit.default_timer() - starttime)
            #--------------------------------------


    def filter_image(self, filter_type):
        '''
        Filter application with convoluted matrix
        1. sobel filter, edge detection
        '''
        def filter(matrix, kernel):
            '''
            The goal of this function is to make 9 shifted copies where the kernel is applied of the original matrix
            Then we just sum up these 9 matrix together and finally optimized the convolution algorithm
            '''
            # initialize list of matrix copies 
            copies = np.empty((len(kernel)*len(kernel), len(matrix), len(matrix[1]), int(get_int_from_bytes(self.bi_bitcount)/8)), dtype='int64') 
            # Go through the kernel (size: 3x3)
            for i in range(np.shape(kernel)[1]):
                for j in range(np.shape(kernel)[0]):
                    # Save copies of the original image shifted by 1 pixel around + kernel value application 
                    copies[i*3 + j] = np.roll(matrix.copy(), (i-(len(kernel)//2), j-(len(kernel)//2)), (0,1)) * kernel[i][j] 
            # return the sum of each copies to get back our new matrix with kernel value applied
            return copies.sum(axis=0)

        kernel = np.empty((3, 3))
        if 'edge' == filter_type:
            print('Sobel edge detection')
            if self.verbose:
                #-------performance calculation--------
                starttime = timeit.default_timer()
                print("Start Sobel edge detection time:", starttime)
                #--------------------------------------

            # Gradient horizontal
            kernel1 = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
            # Gradient vertical
            kernel2 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
            res1 = filter(self.image_matrix, kernel1)
            res2 = filter(self.image_matrix, kernel2)
            self.image_matrix = np.sqrt(res1**2 + res2**2).astype('uint8')

            if self.verbose:
                #-------performance calculation--------
                print("Sobel edge detection duration:", timeit.default_timer() - starttime)
                #--------------------------------------

        #self.image_matrix = filter(self.image_matrix, kernel)
        #kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
        #kernel = np.array([[1, 0, -1], [0, 0, 0], [-1, 0, 1]])

    def brightness_image(self, brightness):
        '''
        Image brightness adjustment
        '''
        # Applying brightness formula for each pixels (RGB) in matrix
        for row in self.image_matrix:
            for pixel in row:
                pixel[0] = round(brightness + pixel[0]) #blue
                pixel[1] = round(brightness + pixel[1]) #green
                pixel[2] = round(brightness + pixel[2]) #red

        # truncate after calculation if the byte value is greater than 255 or lesser than 0
        self.image_matrix[self.image_matrix > 255] = 255
        self.image_matrix[self.image_matrix < 0] = 0


    def display_histogram(self):
        '''
        Display the color histogram of the input bitmap
        '''
        # get total channel, red channel, green channel and blue channel
        total_pixels = self.image_matrix[:,:,:].flatten()
        red_pixels = self.image_matrix[:,:,2].flatten()
        green_pixels = self.image_matrix[:,:,1].flatten()
        blue_pixels = self.image_matrix[:,:,0].flatten()

        # start plotting the color histogram
        fig, ax = plt.subplots()
        ax.hist(total_pixels, bins=256, color='orange', alpha=0.5)

        # grayscale bitmap doesn't need red/green/blue channel to be displayed but only total channel 
        if not (red_pixels.all() == green_pixels.all() == blue_pixels.all()):  
            ax.hist(red_pixels, bins=256, color='red', alpha=0.5)
            ax.hist(green_pixels, bins=256, color='green', alpha=0.5)
            ax.hist(blue_pixels, bins=256, color='blue', alpha=0.5)
            ax.set_title('Color channel Histogram')
            ax.set_xlabel('Channel intensity value')
            ax.set_ylabel('Counter')
            plt.legend(['Total', 'Red_Channel', 'Green_Channel', 'Blue_Channel'])
        else:
            ax.hist(red_pixels, bins=256, color='gray', alpha=0.5)
            ax.set_title('Color channel Histogram for Grayscale')
            ax.set_xlabel('Channel intensity value')
            ax.set_ylabel('Counter')
            plt.legend(['Total', 'Each color channel'])
        fig.tight_layout()
        plt.show()


    def negative_image(self):
        '''
        Turn color image into negative image
        '''
        # Applying negative formula for each pixels (RGB) in matrix
        for row in self.image_matrix:
            for pixel in row:
                pixel[0] = 255 - pixel[0] # blue
                pixel[1] = 255 - pixel[1] # green
                pixel[2] = 255 - pixel[2] # red


    def blackwhite_image(self):
        '''
        Turn color image into black and white image
        '''
        # Applying black and white formula for each pixels (RGB) in matrix
        for row in self.image_matrix:
            for pixel in row:
                temp_mean = (pixel[0] + pixel[1] + pixel[2])/3
                if temp_mean > 127: 
                    pixel[0] = 255 #bleu
                    pixel[1] = 255 #vert
                    pixel[2] = 255 #rouge
                else:
                    pixel[0] = 0 #bleu
                    pixel[1] = 0 #vert
                    pixel[2] = 0 #rouge


    def color_image(self, color_array): 
        '''
        Turn color image into only 1 or 2 primary colors image
        '''
        def keep_color_channel(blue=0, green=0, red=0):
            '''
            1. inhibit color channel by setting up channel value to 0
            2. keep color channel by setting up channel value to None
            '''
            # Applying keep primary color formula for each pixels (RGB) in matrix
            for row in self.image_matrix:
                for pixel in row:
                    # inhibit color 
                    if blue != None:
                        pixel[0] = 0
                    if green != None:
                        pixel[1] = 0
                    if red != None:
                        pixel[2] = 0
            
        if len(color_array) == 2:
            if 'b' in color_array and 'g' in color_array: #cyan
                keep_color_channel(blue=None, green=None)
            elif 'b' in color_array and 'r' in color_array: #magenta
                keep_color_channel(blue=None, red=None)
            elif 'g' in color_array and 'r' in color_array: #yellow
                keep_color_channel(green=None, red=None)
        elif len(color_array) == 1:
            if 'b' in color_array: #blue
                keep_color_channel(blue=None)
            elif 'g' in color_array: #green
                keep_color_channel(green=None)
            elif 'r' in color_array: #red
                keep_color_channel(red=None)


    def grayscale_image(self, grayscale_method):
        '''
        Turn color image into grayscale image depending on 
        1. mean method
        2. luminance method (more accurate)
        '''
        def channel_luminance(channel):
            '''
            get channel color within a linear colorspace
            '''
            if channel <= 0.04045:
                return (channel/12.92) 
            else:
                return (((channel+0.055)/(1+0.055))**2.4)

        # Applying grayscale formula for each pixels (RGB) in matrix
        for row in self.image_matrix:
            for pixel in row:
                if 'mean' in grayscale_method:
                    pixel_value = (pixel[0] + pixel[1] + pixel[2])/3
                elif 'luminance' in grayscale_method:
                    pixel_value = (0.0722*channel_luminance(pixel[0]/255) + 
                                   0.7152*channel_luminance(pixel[1]/255) + 
                                   0.2126*channel_luminance(pixel[2]/255)) * 255
                pixel[0] = round(pixel_value)
                pixel[1] = round(pixel_value)
                pixel[2] = round(pixel_value)


    def contrast_image(self, contrast):
        '''
        Bitmap contrast adjustment
        '''
        #contrast factor calculation
        factor = (259 * (contrast + 255)) / (255 * (259 - contrast))

        # Applying contrast formula for each pixels (RGB) in matrix
        for row in self.image_matrix:
            for pixel in row:
                pixel[0] = round(factor * (pixel[0] - 128) + 128) # blue
                pixel[1] = round(factor * (pixel[1] - 128) + 128) # green
                pixel[2] = round(factor * (pixel[2] - 128) + 128) # red

        # truncate after calculation if the byte value is greater than 255 or lesser than 0
        self.image_matrix[self.image_matrix > 255] = 255
        self.image_matrix[self.image_matrix < 0] = 0

                        
    def resize_image(self, factor):
        '''
        Resize bitmap 
        1. with dimension (width x height) 
        2. with ratio value (strictly positive integer)
        '''
        # get current width and current height
        width = np.shape(self.image_matrix)[1] 
        height = np.shape(self.image_matrix)[0] 

        # get new width and new height with dimension values
        if len(factor) == 2:
            new_width = int(factor[0])
            new_height = int(factor[1])
        # get new width and new height with ratio value
        elif len(factor) == 1:
            new_width = int(float(factor[0]) * get_int_from_bytes(self.bi_width.tolist()))
            new_height = int(float(factor[0]) * get_int_from_bytes(self.bi_height.tolist()))

        # resizing procedure 
        # if new dimension is greater than the current dimension, we simply duplicate pixels
        # if new dimension is lesser than the current dimension, we simply get less pixels (and lose information)
        self.image_matrix = [
            [self.image_matrix[int(height * a / new_height)]
                              [int(width * b / new_width)]
                    for b in range(new_width)
            ] for a in range(new_height)
        ]

        if self.verbose:
            print("{} has been resized to {} x {}".format(self.img.replace('../images/',''), new_width, new_height))
        

    def rotate_image(self, degree):
        '''
        Rotate an image by a degree value
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

        # k is the number of 90° rotation 
        self.image_matrix = np.rot90(self.image_matrix, k=nb_rot)
        
        if self.verbose:
            print("{} has been rotated to {} degree".format(self.img, degree))


    def flip_image(self):
        '''
        Flip an image (mirror effect)
        '''
        self.image_matrix = np.flip(self.image_matrix, 1)


    def save_image(self, output):
        '''
        Adjust header bytes and save image
        '''
        if self.verbose:
            #-------performance calculation--------
            starttime = timeit.default_timer()
            print("Start saving time:", starttime)
            #--------------------------------------

        # Adjust bf_size within header bytes (width x length x bitperpixel/8 + offbits)
        self.bf_size = []
        for i in (int(np.shape(self.image_matrix)[1]) * 
                  int(np.shape(self.image_matrix)[0]) * 
                  int(get_int_from_bytes(self.bi_bitcount.tolist())/8) +
                  int(get_int_from_bytes(self.bf_offbits.tolist()))
                ).to_bytes(4, byteorder='little'):
            self.bf_size.append(i)
        self.bf_size = np.array(self.bf_size)

        # Adjust bi_sizeimage within header bytes (width x length x bitperpixel/8)
        self.bi_sizeimage = []
        for i in (int(np.shape(self.image_matrix)[1]) * 
                  int(np.shape(self.image_matrix)[0]) * 
                  int(get_int_from_bytes(self.bi_bitcount.tolist())/8) 
                ).to_bytes(4, byteorder='little'):
                self.bi_sizeimage.append(i)
        self.bi_sizeimage = np.array(self.bi_sizeimage)

        # Adjust bi_width within header bytes 
        bi_width = []
        for i in np.shape(self.image_matrix)[1].to_bytes(4, byteorder='little'):
            bi_width.append(i)
        self.bi_width = np.array(bi_width)

        # Adjust bi_width within header bytes 
        bi_height = []
        for i in np.shape(self.image_matrix)[0].to_bytes(4, byteorder='little'):
            bi_height.append(i)
        self.bi_height = np.array(bi_height)

        # convert image matrix back into array of bytes
        flattened = np.array(self.image_matrix).flatten().tolist()
        # append header bytes into octets
        octets = self.octets[:get_int_from_bytes(self.bf_offbits.tolist())].tolist()
        # append image bytes into octets
        [octets.append(i) for i in flattened]
        self.octets = np.array(octets)

        # write bytes into output file
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
        f_output.write(bytearray(self.octets[get_int_from_bytes(self.bf_offbits.tolist()):].tolist()))
        f_output.close
        print('generated image has been saved to {}'.format(output))

        if self.verbose:
            #-------performance calculation--------
            print("Saving duration:", timeit.default_timer() - starttime)
            print("Total process time", timeit.default_timer())
            #--------------------------------------


    def display_pixels(self, option):
        '''
        1. Display all pixels of the image (display truncated by Numpy)
        2. Display a specific pixel of the image depending on its position
        '''
        if self.verbose:
            print("\nAffichage de la matrice de pixel [ Bleu Vert Rouge ]")

        if len(option) == 1:
            # display all pixels
            print(self.image_matrix)
        elif len(option) == 2:
            # display pixel value at position (x, y)
            print("Displaying pixel at position: ({}, {})".format(option[0], option[1]))
            print("Blue: "  + str(self.image_matrix[option[0]][option[1]][0]), 
                  "Green: " + str(self.image_matrix[option[0]][option[1]][1]), 
                  "Red: "   + str(self.image_matrix[option[0]][option[1]][2])) 
        

    def display_header(self):
        '''
        Display information about the bitmap header 
        '''
        print('Bitmap header information')
        print (" dec=",self.bf_type[0], " hexa=", hex(self.bf_type[0])[2:].upper()) 
        print (" dec=",self.bf_type[1], " hexa=", hex(self.bf_type[1])[2:].upper())

        print(" =>Magic Number =", self.bf_type, " BM => BitMap signature", "\n\n\t --BITMAP FILE HEADER--")

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bf_size], end=' ')
        print("\t\t=>Taille de Fichier = {} octets".format(str(get_int_from_bytes(self.bf_size.tolist()))))

        print(self.bf_size.tolist(), end=' ')
        print("\t=>Taille de Fichier = {} octets".format(str(get_int_from_bytes(self.bf_size.tolist()))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bf_reserved1], end=' ')
        print("\t\t\t=>Application image (champ réservé 1) = {} noms".format(str(get_int_from_bytes(self.bf_reserved1.tolist()))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bf_reserved2], end=' ')
        print("\t\t\t=>Application image (champ réservé 2) = {} noms".format(str(get_int_from_bytes(self.bf_reserved2.tolist()))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bf_offbits], end=' ')
        print("\t\t=>Off Bits (adresse zone definition image) = {} octets".format(str(get_int_from_bytes(self.bf_offbits.tolist()))))

        print("\n\t --BITMAP INFO HEADER--")
        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_size], end=' ')
        print("\t\t=>Taille de l'entête BITMAP INFO HEADER = {} octets".format(str(get_int_from_bytes(self.bi_size.tolist()))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_width], end=' ')
        print("\t\t=>Largeur image = {} octets".format(str(get_int_from_bytes(self.bi_width.tolist()))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_height], end=' ')
        print("\t\t=>Hauteur image = {} octets".format(str(get_int_from_bytes(self.bi_height.tolist()))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_planes], end=' ')
        print("\t\t\t=>NB plan image = {} plan".format(str(get_int_from_bytes(self.bi_planes.tolist()))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_bitcount], end=' ')
        print("\t\t\t=>Nombre de bits par pixel = {} bits/pixel".format(str(get_int_from_bytes(self.bi_bitcount.tolist()))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_compression], end=' ')
        print("\t\t=>Type de compression = {}\
               \n\t\t\t\t->0=pas de compression\
               \n\t\t\t\t->1=compressé à 8 bits par pixel\
               \n\t\t\t\t->2=compressé à 4 bits par pixel".format(str(get_int_from_bytes(self.bi_compression.tolist()))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_sizeimage], end=' ')
        print("\t\t=>Taille des données de l'image = {} octets".format(str(get_int_from_bytes(self.bi_sizeimage.tolist()))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_xpelspermeter], end=' ')
        print("\t\t=>Résolution horizontale axe X = {} pixels/mètre".format(str(get_int_from_bytes(self.bi_xpelspermeter.tolist()))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_ypelspermeter], end=' ')
        print("\t\t=>Résolution verticale axe Y = {} pixels/mètre".format(str(get_int_from_bytes(self.bi_ypelspermeter.tolist()))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_clrused], end=' ')
        print("\t\t=>Nombre de couleurs dans l'image = {}\
               \n\t\t\t\t->0=maximum possible\
               \n\t\t\t\t->Si une palette est utilisée, ce nombre indique\
               \n\t\t\t\t  le nombre de couleurs de la palette".format(str(get_int_from_bytes(self.bi_clrused.tolist()))))

        print(*[hex(x)[2:].upper().zfill(2) for x in self.bi_clrimportant], end=' ')
        print("\t\t=>Nombre de couleurs importantes dans l'image = {}\
               \n\t\t\t\t->0=toutes importantes".format(str(get_int_from_bytes(self.bi_clrimportant.tolist()))))


    def ouverture_fichiers_image(self):
        '''
        1. Open the image
        2. Get the size of the image
        3. Get all bytes of the image
        '''
        f_lecture = open(self.img,'rb')

        # read file size from header
        i = 0
        while (i < 6):
            octet = f_lecture.read(1) 
            self.octets.append(ord(octet))
            i += 1
        self.bf_size = get_int_from_bytes([k for k in self.octets[2:]])

        # get every image bytes 
        while i < self.bf_size:
            octet = f_lecture.read(1) 
            self.octets.append(ord(octet))
            i += 1
        self.octets = np.array(self.octets)
        f_lecture.close



