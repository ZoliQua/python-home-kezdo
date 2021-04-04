import zlib

h = " Hello, it is me, you're friend Emmett!"
print(len(h))
t = zlib.compress(h.encode("UTF-8"))
print(len(t))
z = zlib.decompress(t)
print(len(z))