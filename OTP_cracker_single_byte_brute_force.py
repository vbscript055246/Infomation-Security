from ciphertexts import *
from key_text import *

result = 0
column = []
char_list = [ord(' '), ord(','), ord('.'), ord("'")] + [i + ord('a') for i in range(26)] + [i + ord('A') for i in range(26)]


# for k, c in enumerate(key.split()):
#     if c == '_':
k = 107
cipher_set = [4, 7]

column.clear()
for ind, cipher in enumerate(CT):  # 0 4 6 7 8
    if ind in cipher_set:
        column.append(cipher.split()[k])

f = open('output.txt', 'w')
for OTP in range(256):
    flag = 1
    for byte in column:
        if not (chr(OTP ^ int(byte, 16)).isascii() and (OTP ^ int(byte, 16)) in char_list):
            flag = 0
            break
    if flag:
        f.write("{:02x}".format(OTP).upper() + '\n')
        print("{:02x}".format(OTP).upper())
        kt = ' '.join(key.split()[:k] + ["{:02x}".format(OTP).upper()] + key.split()[k+1:])
        for i in cipher_set:
            f.write(''.join(decode(cipher=CT[i], _key=kt)) + '\n')
            print(''.join(decode(cipher=CT[i], _key=kt)))

        f.write(''.join(decode(cipher=Challenge_Ciphertext, _key=kt)) + '\n')
        print(''.join(decode(cipher=Challenge_Ciphertext, _key=kt)))
        print()
f.close()
print('done')