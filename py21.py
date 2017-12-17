import zlib
import bz2

import sys
# sys.setdefaultencoding()
# sys.setdefaultencoding('utf-8')

def decompresses(path):
    s = open(path,'rb').read()
    print(s)
    zh = b'x\x9c'
    bh = b'BZ'

    logs = []
    while True:
        sh = s[:2]
        if sh == zh: ##zlib
            s = zlib.decompress(s)
            logs.append(" ")
        elif sh ==bh: ##bz2
            s = bz2.decompress(s)
            logs.append("#")
        elif s[-1:-3:-1] in [zh,bh]:
            print(s[-1:-3:-1])
            s = s[::-1] ##反转
            logs.append("\n")
        else:
            break
    print("".join(logs))


if __name__ == "__main__":
    path = "/Users/zzz/Documents/pycharm/challenge/unreal/package.pack"
    decompresses(path)
