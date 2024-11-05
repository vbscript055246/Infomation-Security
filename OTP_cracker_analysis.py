from ciphertexts import *
from key_text import key, decode

bytes = 70

temp = []
char_list = [ord(' '), ord(','), ord('.')]+ [i + ord('a') for i in range(26)] + [i + ord('A') for i in range(26)]
result = [0 for i in range(bytes)]

# for cipher in CT:
#     temp.append(cipher.split()[:47])
temp.append(CT[0].split()[:bytes])
temp.append(CT[4].split()[:bytes])

for item in temp:
    for i in range(len(item)):
        result[i] ^= int(item[i], 16)

def get_set(result):
    _possible_set = []
    for t in char_list:
        if t ^ result in char_list:
            # print("\t", chr(t), chr(t ^ result))
            _possible_set.append([chr(t), chr(t ^ result)])
    return _possible_set


message_byte_possible_set = {}
str_byte_locker = [0] * bytes
for i in range(len(result)):
    if key.split()[i] == '_':
        flag = 1
        print("cracking byte", i)
        message_byte_possible_set[i] = get_set(result[i])

print(message_byte_possible_set[60])
print(message_byte_possible_set[61])
print(message_byte_possible_set[63])
print(message_byte_possible_set[64])
print(message_byte_possible_set[64])
print(message_byte_possible_set[65])
# print(message_byte_possible_set[21])
# print(message_byte_possible_set[25])
# print(''.join(str_[0]))
# print(''.join(str_[1]))
#
AEIOU = [
    'e', 'ee', 'ea', 'ie', 'ei',
    'i', 'y', 'a', 'ai', 'ay',
    'ey', 'ar', 'uy', 'ou', 'ow',
    'o', 'or', 'au', 'aw', 'ought',
    'al', 'wa', 'oi', 'oy', 'oa',
    'ow', 'u', 'ew', 'eu', 'ui',
    'ue', 'oo', 'er', 'ur', 'ir',
    'or', 'ear'
]

def recursive_possible_set(n=0, strA = ['_' for i in range(bytes)], strB = ['_' for i in range(bytes)]):
    if n != bytes:
        if str_byte_locker[n]:
            recursive_possible_set(n + 1, strA, strB)
        else:
            for pair_arr in message_byte_possible_set[n]:
                strA[n] = pair_arr[0]
                strB[n] = pair_arr[1]
                recursive_possible_set(n + 1, strA, strB)
    else:
        SA, SB = ''.join(strA), ''.join(strB)
        if all([any([s in word.lower() for s in AEIOU]) for word in SA.split()]) and all([any([s in word.lower() for s in AEIOU]) for word in SB.split()]):
            # if not(any([strA[i] == ' ' and strA[i+1] == ' ' for i in range(len(strA)-1)]) or any([strB[i] == ' ' and strB[i+1] == ' ' for i in range(len(strB)-1)])):
            if SA[0].isupper() and SB[0].isupper():
                print("strA: ", SA)
                print("strB: ", SB)
                print()

# for ind, i in enumerate(key.split()):
#     if i != '_':
#         str_byte_locker[ind] = 1
#
# SA = decode(cipher=CT[0])
# SB = decode(cipher=CT[1])
# print(SA)
# print(SB)
# print(str_byte_locker)
# # recursive_possible_set()
# recursive_possible_set(0, SA, SB)
print('done')