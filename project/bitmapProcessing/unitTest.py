import unittest
from main import check_interval
from main import check_resize_ratio
from main import check_display_pixel_option
from bmpProcessing.utils.Utils import get_int_from_bytes

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
        
        
if __name__ == '__main__':
    unittest.main()