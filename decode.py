import codecs


class Decode:
    def hex_to_str(self, hex_str, key):
        l1 = [int(key[i] + key[i + 1], 16) for i in range(0, len(key) - 1, 2)]
        print(l1)
        l2 = [int(hex_str[i] + hex_str[i + 1], 16) for i in range(0, len(hex_str) - 1, 2)]
        print(l2)
        print(i ^ j for (i, j) in zip(l1, l2))
        text = "".join(hex(x ^ y)[2:4] for (x, y) in zip(l1, l2))
        return "".join(chr(int(text[i] + text[i + 1], 16)) for i in range(0, len(text)-1, 2))



