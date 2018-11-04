import numpy as np
from bitstring import BitArray
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]
def init_permutaion(data):
    def convert_byte_to_bitarray(byte):
        mark = 1<<7
        res = []
        for _ in range(8):
            if mark & byte == 0:
                res.append(0)
            else:
                res.append(1)
            byte = byte<<1
        return res

    def to_binary(data):
        bytes_array = bytes(data,'utf-8')
        bit_array = to_bit_array(bytes_array)
        return bit_array
    def to_bit_array(bytes_array):
        res = []
        
        for byte in bytes_array:
            res += convert_byte_to_bitarray(byte)
        return res

    bits = to_binary(data)
    print(len(bits))

    if len(bits)!=64:
        raise Exception("data must be 64 bits!")
    res = []
    for i in range(64):
        res.append(bits[IP[i]-1])
    print(res)
    

    

if __name__ == "__main__":
    init_permutaion("abcdefgh")