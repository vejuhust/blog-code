

# Implementations

def compress_right_v1(x, mask):
    """ Hacker's Delight 2e - Figure 7-5 : while loop """
    res, shift, mask_bit = 0, 0, 0
    while (mask != 0):
        mask_bit = mask & 0x1
        res |= (x & mask_bit) << shift
        shift += mask_bit
        x >>= 1
        mask >>= 1
    return res



def compress_right_v2(x, mask):
    """ Stackoverflow Version """
    res = 0
    bb = 1
    while (mask != 0):
        if x & mask & -mask:
            res |= bb
        mask &= (mask - 1)
        bb += bb
    return res



def compress_right_v3(num, mask):
    """ Hacker's Delight 2e - Figure 7-10 : 32-bit """
    x = num & mask              # clear irrelevant bits
    m = mask
    mk = ~m << 1                # bits of mask that have a 0 immediately to the right
    for i in range(5):
        mp = mk ^ (mk << 1)     # parallel suffix operation
        mp = mp ^ (mp << 2)
        mp = mp ^ (mp << 4)
        mp = mp ^ (mp << 8)
        mp = mp ^ (mp << 16)    # bits of mask that have an odd number of 0’s to the right
        mv = mp & m             # mask of bits to move
        m = m ^ mv | (mv >> (1 << i))   # compress m
        t = x & mv                      # bits to move
        x = x ^ t | (t >> (1 << i))     # compress x
        mk &= ~mp                       # bits of revised mask that have a 0 to the immediate right and an even number of 0’s to the right
    return x



def compress_right_v4(num, mask):
    """ 128-bit extension for Hacker's Delight 2e - Figure 7-10 """
    x = num & mask              # clear irrelevant bits
    m = mask
    mk = ~m << 1                # bits of mask that have a 0 immediately to the right
    for i in range(7):
        mp = mk ^ (mk << 1)     # parallel suffix operation
        mp = mp ^ (mp << 2)
        mp = mp ^ (mp << 4)
        mp = mp ^ (mp << 8)
        mp = mp ^ (mp << 16)
        mp = mp ^ (mp << 32)
        mp = mp ^ (mp << 64)    # bits of mask that have an odd number of 0’s to the right
        mv = mp & m             # mask of bits to move
        m = m ^ mv | (mv >> (1 << i))   # compress m
        t = x & mv                      # bits to move
        x = x ^ t | (t >> (1 << i))     # compress x
        mk &= ~mp                       # bits of revised mask that have a 0 to the immediate right and an even number of 0’s to the right
    return x





# Helpers

def printb(num, max_length = 32, limit = 4):
    mask = (1 << max_length) - 1
    num &= mask
    numstr = "{:0MAXb}".replace("MAX", str(max_length)).format(num)
    i = 0
    outstr = ""
    while i < len(numstr):
        outstr += numstr[i:i+limit] + " "
        i += limit
    outstr += "- {:0MAXx}".replace("MAX", str(max_length >> 2)).format(num)
    print(outstr)



def compare_compress_function(func, x, m, r, verbose=False):
    global test_idx
    test_idx += 1
    y = globals()[func](x, m)
    if verbose:
        print("# Test: {:03d}".format(test_idx))
        printb(x, 32)
        printb(m, 32)
        printb(y, 32)
    else:
        print("# Test: {:03d} {:x} ❤ {:x} -> {:x} ".format(test_idx, x, m, y), end=" ...")
    if y == r:
        print("\033[92m" + "ok" + "\033[0m")
    else:
        print("\033[91m" + "failed" + "\033[0m")
        # exit()



def run_test_cases(cases):
    global test_idx
    for v in range(1, 5):
        test_idx = 0
        func_name = "compress_right_v{}".format(v)
        if func_name in globals():
            print("=== {} ===".format(func_name))
            for case in cases:
                compare_compress_function(func_name, case[0], case[1], case[2], False)
        else:
            break
        print()
    print("\033[94m" + "\033[4m" + "Done!" + "\033[0m")



# Cases

test_cases = [
    (0b0, 0b0, 0b0),
    (0b1000, 0b111, 0b0),
    (0b1101, 0b10, 0b0),
    (0b1101, 0b0011, 0b1),
    (0b1111, 0b10, 0b1),
    (0b1111, 0b1111, 0b1111),
    (0xf, 0x5555, 0x3),
    (0b11101110, 0b1001, 0b10),
    (0b00110100, 0b11000011, 0b0),
    (0xf000, 0x5555, 0xc0),
    (0xcc00, 0x5555, 0xa0),
    (0xffff, 0x5555, 0xff),
    (0b0, 0b11111111111111111111111111111111, 0b0),
    (0b10, 0b11111111111111111111111111111111, 0b10),
    (0b11111111111111111111111111111111, 0b0, 0b0),
    (0b11111111111111111111111111111111, 0b11111111111111111111111111111111, 0b11111111111111111111111111111111),
    (0b11111111111111111111111111111111, 0b00001111001100111010101001010101, 0b00000000000000001111111111111111),
    (0b00000000000000001111111111111111, 0b00000000000000000111111111111111, 0b00000000000000000111111111111111),
    (0b00000000000000001111111111111000, 0b00000000000000000111111111111001, 0b00000000000000000001111111111110),
    (0b00000001001100111010101001010101, 0b00001111001100111010101001010101, 0b00000000000000000001111111111111),
    (0b00001111001100111010101001010101, 0b11111111111111111111111111111111, 0b00001111001100111010101001010101),
    (0b00001111001100111010101001010101, 0b11111111111111111111111111111000, 0b00000001111001100111010101001010),
    (0b00001111001100111010101001010101, 0b11110000111111111111111111111000, 0b00000000000001100111010101001010),
    (0b111111111111111111111111111111111, 0b100000000000000000000000000000000, 0b1),
    (0b111111111111111111111111111111111, 0b100000000000000000000010000000000, 0b11),
    (0b111111111111111111111111111111111, 0b101010000000000000000000000000000, 0b111),
    (0b1111111111111111111111111111111111, 0b1100000000000000000000000000000000, 0b11),
    (0xffff0000000000000000, 0x555555550000000000000000, 0xff),
    (0x5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f, 0x55555555555555555555555555555555, 0x0000000000000000ffffffffffffffff),
    (0xffffffffffffffffffffffffffffffff, 0x55555555555555555555555555555555, 0xffffffffffffffff),
    (0xffffffffffffffff0000000000000000, 0x55555555555555555555555555555555, 0xffffffff00000000),
    (0x0000ffffffffffffffff000000000000, 0x55555555555555555555555555555555, 0xffffffff000000),
    (0x0000ffffffffffffffff000000000000, 0x55555555555555555555555555555555, 0xffffffff000000),
    (0xaec54f1fb5de4ca08cb8e15431749952, 0x55555555555555555555555555555555, 0x2bb77ea0249e5e5c),
    (0xbe73b91e973f4070bde43bac60384274, 0x55555555555555555555555555555555, 0x6d56778c7a52848e),
    (0x39556de6eac342c5a1994d305a9541e2, 0x55555555555555555555555555555555, 0x5fba898b15b4c798),
    (0xfc2a3684e37a3cc19e909164b7a, 0x1593e43462e8ee0056950d4f621, 0x6233dce7c346),
    (0x50e598819f5c4de1b297c93b9c3ef899, 0x6fa5c7fe2c1f430fb7dbb7e5b89dd702, 0x83e101f28f55c25b770),
    (0xd8a916c8, 0x5fe4c76f0f42497db9990a370a5bd108, 0x8a5),
    (0xdda0ef0d1ccf444fb2c7680797406598, 0xf985e, 0xc),
]



# Run Tests

if __name__ == '__main__':
    run_test_cases(test_cases)
