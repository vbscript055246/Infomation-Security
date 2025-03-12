import requests
from tqdm import tqdm
import threading
cipher_text = [
    '00112233445566778899aabbccddeeff',
    'f9473924bd62ba19f2dd19c309289477',
    '65786c8d4972fd132ec97a3a3e518191',
    '7652a0dc44cb493881bdd841103b8bca',
    '2d4824eef54b306f093bdc5a17dc9f46',
    'a862217ecb6b80244fdba90fbb13c72b',
    'ab3de8d9653be21d635a0f8d59712836',
    '06eb64c0fbb922afd9db007f94fb9e24',
    'a899a6c0a65b687b85f45d4840d47df4'
]

decrypt_CT2 = []

return_value_collector = [None] * 256


def job(sf, sb, n):
    global return_value_collector
    for i in range(n, n+32):
        try:
            r = requests.get(f"http://140.122.185.210:8080/oracle/{sf + f'{i:0>2x}' + sb}")
            if 'valid' == r.text:
                return_value_collector[i] = i
                break
        except:
            exit(66)


def padding_fit(decrypt_CT2, index):
    CT1_pb = ''
    for byte in decrypt_CT2[::-1]:
        CT1_pb += f'{int(byte, 16) ^ index:0>2x}'
    return CT1_pb


def brute_froce(CT1, CT2, index):
    global decrypt_CT2, return_value_collector
    CT1_pf = CT1[:-2 * index]
    # print(CT1_pf, end='__')

    CT1_pb = padding_fit(decrypt_CT2, index)
    # print(CT1_pb, CT2)

    for i in tqdm(range(256)):
        s = CT1_pf + f'{i:0>2x}' + CT1_pb + CT2
        try:
            r = requests.get(f"http://140.122.185.210:8080/oracle/{s}")
            if 'valid' == r.text:
                # print("valid CT1 after padding", CT1_pf + f'{i:0>2x}' + CT1_pb)
                # print("get byte", f'{i ^ index:0>2x}')
                return f'{i ^ index:0>2x}'
        except:
            exit(66)

    # threads = []
    # return_value_collector = [None] * 256
    # for i in range(0, 256, 32):
    #     threads.append(threading.Thread(target=job, args=(CT1_pf, CT1_pb + CT2, i,)))
    #     threads[-1].start()
    # for i in tqdm(range(len(threads))):
    #     threads[i].join()
    #
    # for i in range(256):
    #     if return_value_collector[i] is not None:
    #         print("valid CT1 after padding", CT1_pf + f'{i:0>2x}' + CT1_pb)
    #         print("get byte", f'{i ^ index:0>2x}')
    #         return f'{i ^ index:0>2x}'

    exit(87)


if __name__ == '__main__':

    for j in range(6, len(cipher_text)-1):
        CT1 = cipher_text[j]
        CT2 = cipher_text[j+1]
        print("Decoding~", CT2)
        for i in range(1, 17):
            decrypt_CT2.append(brute_froce(CT1, CT2, i))

        paint_text = []
        for ind, byte in enumerate(decrypt_CT2[::-1]):
            paint_text.append(f'{int(byte, 16) ^ int(CT1[ind:ind+2], 16):0>2x}')
        decrypt_CT2.clear()
        print(f'cipher{j} decode is ', ''.join(paint_text))

print('done')
