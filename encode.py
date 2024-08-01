import sys
import os
import codecs


class Encode:
    def __init__(self):
        pass

    def gen_key(self, n):
        # print(n)
        k = os.urandom(n)
        # print(k)
        str1 = codecs.encode(k, 'hex').decode('utf-8')
        # print(str1 + "\nThe end")
        return str1

    def str_enc(self, s1):
        # s1_len = sys.getsizeof(s1)
        s1_len = len(s1)
        key = self.gen_key(s1_len)
        hex_text = self.hexor(s1, key)
        return hex_text, key
        # plain_hex_text =

    def hexor(self, text, key):
        l1 = [int(key[i] + key[i + 1], 16) for i in range(0, len(key)-1, 2)]
        # print(l1)
        l2 = [ord(x) for x in text]
        # print(l2)
        # print(i^j for (i,j) in zip(l1,l2))
        enc_text = "".join(hex(x ^ y)[2:4] for (x, y) in zip(l1, l2))
        return enc_text
        # print(enc_text)


