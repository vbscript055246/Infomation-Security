from ciphertexts import *

special_char = ' '
result = 0

char_list = [ord(' '), ord(','), ord('.'), ord('!')] + [i + ord('a') for i in range(26)] + [i + ord('A') for i in range(26)]


def get_set(result):
    message_byte_possible_set = []
    if ord(special_char) ^ result in char_list:   # in char_list
        # print("\t", chr(ord(' ')), chr(ord(' ') ^ result))
        message_byte_possible_set.append([chr(ord(special_char)), chr(ord(special_char) ^ result)])
    return message_byte_possible_set


key = []
for k in range(106):
    column = []
    for ind, cipher in enumerate(CT):  # 0 4 6 7 8
        if ind in [0, 4, 6, 7, 8]:
            column.append(cipher.split()[k])

    have_space = []
    for i, b0 in enumerate(column):
        for j in range(i+1, len(column)):
            b1 = column[j]
            result = int(b0, 16) ^ int(b1, 16)
            if len(get_set(result)):
                have_space.append([i, j])
    # print(have_space)
    _set = [0 for i in range(10)]
    for set_item in have_space:
        _set[set_item[0]] += 1
        _set[set_item[1]] += 1
    print('{:<2}'.format(k), _set)
    try:
        index = _set.index(len(column)-1)
        OTP = int(column[index], 16) ^ ord(special_char)
        # print(hex(OTP).lstrip('0x').upper())
        key.append("{:02x}".format(OTP).upper())
    except:
        # try:
        #     index = _set.index(len(column)-2)
        #     OTP = int(column[index], 16) ^ ord(special_char)
        #     # print(hex(OTP).lstrip('0x').upper())
        #     key.append("{:02x}".format(OTP).upper())
        # except:
        print('{:<2}'.format(k), 'byte crack fail~')
        key.append('_')

print(" ".join(key))
print('done')