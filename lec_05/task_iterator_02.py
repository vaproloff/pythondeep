"""iter(object[, sentinel])"""

data = [2, 4, 6, 8]
# list_iter = iter(data, 6)

import functools

f = open('mydata.bin', 'rb')
for block in iter(functools.partial(f.read, 16), b''):
    print(block)
f.close()
