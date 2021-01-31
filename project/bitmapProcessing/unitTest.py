#!/usr/bin/env python3
import unittest
import argparse 
import os 
import sys
import numpy as np
from main import check_interval
from main import check_resize_ratio
from main import check_display_pixel_option
import bmpProcessing.BmpProcessing as BmpProcessing
from bmpProcessing.utils.Utils import get_int_from_bytes
from bmpProcessing.utils.Utils import printProgressBar

class bitmapProcessingTest(unittest.TestCase):
    def test_check_interval(self):
        '''
        unit test for check_interval
        '''
        # Test if it raises exception
        with self.assertRaises(Exception) as context: check_interval(-256)
        with self.assertRaises(Exception) as context: check_interval(+256)
        # Test if it return int value between -255 and 255
        self.assertTrue(isinstance(check_interval(128), int))


    def test_check_resize_ratio(self):
        '''
        unit test for check_resize_ratio
        '''
        # Test if it raises exception
        with self.assertRaises(Exception) as context: check_resize_ratio(-1)

        # Test if it return positive float value
        self.assertTrue(isinstance(check_resize_ratio(1.5), float))
        self.assertFalse(isinstance(check_resize_ratio('1.5'), float))


    def test_check_display_pixel_option(self):
        '''
        unit test for check_display_pixel_option
        '''
        # Test if it raises exception
        with self.assertRaises(Exception) as context: check_display_pixel_option(-256)
        with self.assertRaises(Exception) as context: heck_display_pixel_option(+256)

        # Test if it return positive str value if 'all'
        self.assertTrue(isinstance(check_display_pixel_option('all'), str))
        
        # Test if it return int type
        self.assertFalse(isinstance(check_display_pixel_option(2), float))
        self.assertTrue(isinstance(check_display_pixel_option(2), int))


    def test_get_int_from_bytes(self):
        '''
        unit test for get_int_from_bytes
        '''

        # Test if it return int value from array of bytes
        self.assertTrue(isinstance(get_int_from_bytes([ord(b'\x00'), ord(b'\x02'), ord(b'\x00'), ord(b'\x00')]), int))
        self.assertTrue(isinstance(get_int_from_bytes([0, 2, 0, 0]), int))
        
def test_all(input_file_name, verbose):
    printProgressBar(0, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test Rotation 90 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.rotate_image(90)
    if not os.path.exists('../../images/test/rotation/'):
        os.makedirs('../../images/test/rotation/')
    pandaBmp.save_image("../../images/test/rotation/rotation90.bmp")

    printProgressBar(1, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test Rotation 180 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.rotate_image(180)
    pandaBmp.save_image("../../images/test/rotation/rotation180.bmp")

    printProgressBar(2, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test Rotation 270 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.rotate_image(270)
    pandaBmp.save_image("../../images/test/rotation/rotation270.bmp")

    printProgressBar(3, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test Resize ratio x2 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.resize_image([2])
    if not os.path.exists('../../images/test/resize/'):
        os.makedirs('../../images/test/resize/')
    pandaBmp.save_image("../../images/test/resize/resize_x2.bmp")

    printProgressBar(4, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test Resize ratio x0.5 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.resize_image([0.5])
    pandaBmp.save_image("../../images/test/resize/resize_x05.bmp")

    printProgressBar(5, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test Resize width height 800 400 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.resize_image([800, 400])
    pandaBmp.save_image("../../images/test/resize/resize_ratio_800_400.bmp")

    printProgressBar(6, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test contrast adjustment -255 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.contrast_image(-255)
    if not os.path.exists('../../images/test/contrast/'):
        os.makedirs('../../images/test/contrast/')
    pandaBmp.save_image("../../images/test/contrast/contrast-255.bmp")

    printProgressBar(7, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test contrast adjustment -180 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.contrast_image(-180)
    pandaBmp.save_image("../../images/test/contrast/contrast-180.bmp")

    printProgressBar(8, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test contrast adjustment -80 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.contrast_image(-80)
    pandaBmp.save_image("../../images/test/contrast/contrast-80.bmp")

    printProgressBar(9, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test contrast adjustment +80 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.contrast_image(+80)
    pandaBmp.save_image("../../images/test/contrast/contrast+80.bmp")

    printProgressBar(10, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test contrast adjustment +180 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.contrast_image(+180)
    pandaBmp.save_image("../../images/test/contrast/contrast+180.bmp")

    printProgressBar(11, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test contrast adjustment +255 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.contrast_image(+255)
    pandaBmp.save_image("../../images/test/contrast/contrast+255.bmp")

    printProgressBar(12, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test brightness adjustment -255 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.brightness_image(-255)
    if not os.path.exists('../../images/test/brightness/'):
        os.makedirs('../../images/test/brightness/')
    pandaBmp.save_image("../../images/test/brightness/brightness-255.bmp")

    printProgressBar(13, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test brightness adjustment -180 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.brightness_image(-180)
    pandaBmp.save_image("../../images/test/brightness/brightness-180.bmp")

    printProgressBar(14, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test brightness adjustment -80 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.brightness_image(-80)
    pandaBmp.save_image("../../images/test/brightness/brightness-80.bmp")

    printProgressBar(15, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test brightness adjustment +80 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.brightness_image(+80)
    pandaBmp.save_image("../../images/test/brightness/brightness+80.bmp")

    printProgressBar(16, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test brightness adjustment +180 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.brightness_image(+180)
    pandaBmp.save_image("../../images/test/brightness/brightness+180.bmp")

    printProgressBar(17, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test brightness adjustment +255 #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.brightness_image(+255)
    pandaBmp.save_image("../../images/test/brightness/brightness+255.bmp")

    printProgressBar(18, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test grayscale mean #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.grayscale_image('mean')
    if not os.path.exists('../../images/test/grayscale/'):
        os.makedirs('../../images/test/grayscale/')
    pandaBmp.save_image("../../images/test/grayscale/grayscale-mean.bmp")

    printProgressBar(19, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test grayscale luminance #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.grayscale_image('luminance')
    pandaBmp.save_image("../../images/test/grayscale/grayscale-luminance.bmp")

    printProgressBar(20, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test grayscale sepia Eugene Atget #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.grayscale_image('atget')
    pandaBmp.save_image("../../images/test/grayscale/grayscale-atget-sepia.bmp")

    printProgressBar(21, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test flip #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.flip_image()
    if not os.path.exists('../../images/test/flip/'):
        os.makedirs('../../images/test/flip/')
    pandaBmp.save_image("../../images/test/flip/flip.bmp")

    printProgressBar(22, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test color image red #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.color_image(['r'])
    if not os.path.exists('../../images/test/color/'):
        os.makedirs('../../images/test/color/')
    pandaBmp.save_image("../../images/test/color/color-red.bmp")

    printProgressBar(23, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test color image green #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.color_image(['g'])
    pandaBmp.save_image("../../images/test/color/color-green.bmp")

    printProgressBar(24, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test color image blue #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.color_image(['b'])
    pandaBmp.save_image("../../images/test/color/color-blue.bmp")

    printProgressBar(25, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test color image red green #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.color_image(['r','g'])
    pandaBmp.save_image("../../images/test/color/color-yellow.bmp")

    printProgressBar(26, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test color image red blue #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.color_image(['r','b'])
    pandaBmp.save_image("../../images/test/color/color-magenta.bmp")

    printProgressBar(27, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test color image green blue #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.color_image(['g','b'])
    pandaBmp.save_image("../../images/test/color/color-cyan.bmp")

    printProgressBar(28, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test negative image #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.negative_image()
    if not os.path.exists('../../images/test/negative/'):
        os.makedirs('../../images/test/negative/')
    pandaBmp.save_image("../../images/test/negative/negative.bmp")

    printProgressBar(29, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test black and white image #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.blackwhite_image()
    if not os.path.exists('../../images/test/blackwhite/'):
        os.makedirs('../../images/test/blackwhite/')
    pandaBmp.save_image("../../images/test/blackwhite/blackwhite.bmp")

    printProgressBar(30, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test overlay two images maximum #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.fit_overlay('../../images/bitmap512x512.bmp')
    pandaBmp.overlay('maximum')
    if not os.path.exists('../../images/test/overlay/'):
        os.makedirs('../../images/test/overlay/')
    pandaBmp.save_image("../../images/test/overlay/overlay-maximum.bmp")

    printProgressBar(31, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test overlay two images minimum #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.fit_overlay('../../images/bitmap512x512.bmp')
    pandaBmp.overlay('minimum')
    pandaBmp.save_image("../../images/test/overlay/overlay-minimum.bmp")

    printProgressBar(32, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test Sobel edge detection filter #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.filter_image('edge-detection')
    if not os.path.exists('../../images/test/filter/'):
        os.makedirs('../../images/test/filter/')
    pandaBmp.save_image("../../images/test/filter/filter-sobel-edge-detection.bmp")

    printProgressBar(33, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test emboss filter #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.filter_image('emboss')
    pandaBmp.save_image("../../images/test/filter/filter-emboss.bmp")

    printProgressBar(34, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test edge reinforcement filter #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.filter_image('edge-reinforcement')
    pandaBmp.save_image("../../images/test/filter/filter-edge-reinforcement.bmp")

    printProgressBar(35, 397, prefix='Progress:', suffix='Complete', length=50)
    # Test blur filter #
    pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
    pandaBmp.fit(True)
    pandaBmp.filter_image('blur')
    pandaBmp.save_image("../../images/test/filter/filter-blur.bmp")

    # Test colorize image #
    if not os.path.exists('../../images/test/colorize/'):
        os.makedirs('../../images/test/colorize/')
    for i in range(0, 360):
        printProgressBar(i+36, 397, prefix='Progress:', suffix='Complete', length=50)
        pandaBmp = BmpProcessing.BmpProcessing(input_file_name, verbose)
        pandaBmp.fit(True)
        pandaBmp.colorize_image(i)
        pandaBmp.save_image("../../images/generated/generated.bmp")
        pandaBmp.save_image("../../images/test/colorize/colorize-{}.bmp".format(i))

    printProgressBar(397, 397, prefix='Progress:', suffix='Complete', length=50)
if __name__ == '__main__':
    unittest.main()