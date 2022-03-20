import string
from collections import deque
t = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def decrypt(x):
    d = deque(string.ascii_lowercase)
    d.rotate(-2)
    table = x.maketrans(string.ascii_lowercase, "".join(d))
    return x.translate(table)


print(decrypt(t))
print(decrypt("map"))
