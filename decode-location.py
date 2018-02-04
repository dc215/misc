# Decode the location, python3
import binascii as bin
import base64

location='add encoded text here'

# location looks like hex so lets unhexlify it
l = bin.unhexlify(location)

'''
>>> l
b'MjEwIFNvdXRoIDMzcmQgU1QsIFNLSDExNA=='

hmm, is this base64 encoded?
'''

l2 = base64.b64decode(l)

print("Location: ", l2)
