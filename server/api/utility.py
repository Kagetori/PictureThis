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

def unobfuscate_id(val):
    """
    Reverse obfuscation of id
    """
    x = ctypes.c_int32(val ^ int(0x541C6A3E)).value
    a = ctypes.c_int32((x & int(2147479552)) >> 12).value
    b = ctypes.c_int32((x & int(4095)) << 19).value
    return int(a | b)
