from zlib import crc32, adler32

for i in range(97, 97 + 26, +1):
    a = str(chr(i))
    b = len(a)
    tmp = []

    for i in range(b):
        new = ord(a[i]) + 2
        tmp.append(new)

    for i in tmp:
        if i > 110:
            print(crc32(bytes(i)))
        else:
            print(adler32(bytes(i)))
