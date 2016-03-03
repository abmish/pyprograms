"""
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
"""

import zlib
lstring = "hello world!hello world!hello world!hello world!"
compressed_string = zlib.compress(lstring)

print compressed_string
print zlib.decompress(compressed_string)