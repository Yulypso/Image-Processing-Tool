class imageBmp: 
    '''
    Implementation of an BMP format image
    img: ../path/to/image.bmp
    '''

    def __init__(self, img):
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
        
        #self.get_int_from_bytes(self.octets[2:6])
        print(self.bf_type)
        print(self.bf_size)
        
    
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
        f_lecture.close

    def get_int_from_bytes(self, b_array):
        return int.from_bytes(b_array, byteorder='little')
