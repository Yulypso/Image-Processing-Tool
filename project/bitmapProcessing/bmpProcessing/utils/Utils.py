# bmpProcessing.utils.Utils module

def get_int_from_bytes(b_array):
    '''
    convert array of bytes into integer value
    '''
    return int.from_bytes(b_array, byteorder='little')