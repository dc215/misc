# Decode the location, python3
import binascii as bin
import base64

location='4d6a457749464e766458526f49444d7a636d51675531517349464e4c534445784e413d3d'

# location looks like hex so lets unhexlify it
l = bin.unhexlify(location)

'''
>>> l
b'MjEwIFNvdXRoIDMzcmQgU1QsIFNLSDExNA=='

hmm, is this base64 encoded?
'''

l2 = base64.b64decode(l)

print("Location: ", l2)
