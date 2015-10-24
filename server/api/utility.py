import ctypes

# Utility functions

def obfuscate_id(val):
    """
    Obfuscates the row of the table to
    create an obfuscated id
    """
    a = ctypes.c_int32((val << 12) & int(2147479552)).value
    b = ctypes.c_int32((val >> 19) & int(4095)).value
    return ctypes.c_int32(int(a | b) ^ int(0x541C6A3E)).value
