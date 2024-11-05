key = '''
21 B4 01 9D 82 2A 01 04 7A C3 E5 8C 25 91 B8 C6
75 96 3E 7E 6C BF 11 77 3D D1 9A 50 77 D4 78 3D
A6 82 7C C0 53 55 5C E7 B6 E7 C8 6E 32 D3 D0 6B
5E C9 BA 87 22 9D 07 55 21 E8 61 95 77 9F D4 54
91 C6 E5 8D C0 E7 C0 DF FC 9A 39 B5 43 57 0D 5D
7C F4 B2 69 39 94 7D 45 B6 68 7F 0E 61 C3 AA 6B
40 7C CB 39 99 15 50 55 36 05 27 AD
'''
# 0:  21
# 1:  B4
# 13: 91
# 21: BF
# 25: D1
# 52: 22
# 57: E8
# 59: 95
# 60: 77
# 61: 9F
# 63: 54
# 64: 91
# 65: C6
# 66: E5
# 67: 8D
# 70: C0
# 74: 39
# 75: B5
# 77: 57
# 78: 0D
# 85: 94
# 88: B6
# 91: 0E
# 93: C3
# 94: AA
# 95: 6B
# 100: 99
# 101: 15
# 104: 36
# 105: 05
# 106: 27
# 107: AD


from ciphertexts import *

def decode(cipher=CT[0], _key=key, length=len(key.split())):
    output = []
    for ind, byte in enumerate(cipher.split()):
        if ind >= length:
            return output
        if _key.split()[ind] == '_':
            # if ind == 25:
            # print(ind, byte)
            # print('_', end='')
            output.append('_')
        else:
            # print(chr(int(byte, 16) ^ int(_key.split()[ind], 16)), end = '')
            output.append(chr(int(byte, 16) ^ int(_key.split()[ind], 16)))
    return output

if __name__ == '__main__':
    print(len(Challenge_Ciphertext.split()))
    print(len(key.split()))
    # for i in range(10):
    #     print(''.join(decode(cipher=CT[i])))
    print(''.join(decode(cipher=Challenge_Ciphertext, length=len(key.split()))))
    print('done')