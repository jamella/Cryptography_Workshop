#!/usr/bin/env python2
#
# In this exercise, you will mount a pre-image and a collision attack
# on SHA-256. Since SHA-256 is not broken, you will mount the attack
# on the first bytes of the hash only.

import random
import Crypto.Hash.SHA256
import hashlib
import pdb
import os
import binascii

blockSize = 64 # 64 * 8 = 512 bit

def prettyPrintHexList(l):
    numbersPerLine = 16
    i = 0
    s = ''
    for c in l:
        s += '%02X' % ord(c)
        i += 1
        if(i == numbersPerLine):
            s += '\n'
            i = 0
        else:
            s += ' '
    if((len(l) % numbersPerLine) != 0):
       s += '\n'
    return(s)
   
# In this exercise, we only use the first three bytes of SHA-256 hashs,
# i.e. when calculating a hash, we cut it after the third byte.
#
# Your goal is to mount a pre-image attack on the hash
#
# FF FF FF
#
# I.e. find a byte sequence (message) with a SHA-256 hash starting with
# FF FF FF.
def preimage(digest):
   
    digestString = prettyPrintHexList(digest).lower().replace(" ", "").strip()
    preimageLen  = len(digestString)   
   
    while True:
        tmpMessage = binascii.b2a_hex(os.urandom(32))
        shaString  = hashlib.sha256(tmpMessage).hexdigest()
        if shaString[:preimageLen] == digestString:
            #print "found Message: " + tmpMessage
            #print "found Hash   : " + shaString
            return (tmpMessage.decode("hex"), shaString.decode("hex"))
       
   
    #found Message: 0c898c2e4104215e6cea58bbd54b0d
    #found Hash   : ffffff3637df235dbccd748a3eacdc9615299007336b9eae4b00fdc990636f93
   
    return ("","")
   
# In this exercise, we only use the first five bytes of SHA-256 hashs,
# i.e. when calculating a hash, we cut it after the fifth byte.
#
# Your goal is to mount a collision attack, i.e. find two byte
# sequences (messages) for which the first five bytes of the SHA-256
# hash are identical.
def collision(digestLength):
    dictionary = dict()
   
    while True:
        tmpMessage = binascii.b2a_hex(os.urandom(32))
        shaString  = hashlib.sha256(tmpMessage).hexdigest()
        key = shaString[:digestLength*2]
       
        if key in dictionary:
            #print (tmpMessage, shaString)
            #print dictionary[key]
            return (tmpMessage.decode("hex"), shaString.decode("hex"), dictionary[key][0].decode("hex"), dictionary[key][1].decode("hex"))
       
        dictionary[key] = (tmpMessage, shaString)
       
    #('494883bfee7d3b63f985dcdc25cf97efd5e0056745f5e3f95f337e7cacde7cfa', '846d80c00b8689d43ff1984260e950b8ba0e4dc6a797044bfb161c64438f213e')
    #('86e7520ef01dd57be5cd946256d73a07d2427084e407070412c17e456a0ded67', '846d80c00b9b827fd586b65410f16cdf2c16a626c8400527d442ca73bd225dcc')   
   
    return ("","","","")

def test():
    print('********')
    print('Preimage')
    print('********\n')
    (msg, digest) = preimage('\xFF\xFF\xFF')
    print('Message:')
    print(prettyPrintHexList(list(msg)))
    print('Digest:')
    print(prettyPrintHexList(list(digest)))

    print('*********')
    print('Collision')
    print('*********\n')
    (m0, d0, m1, d1) = collision(5)
    print('First Message:')
    print(prettyPrintHexList(list(m0)))
    print('Digest:')
    print(prettyPrintHexList(list(d0)))
    print('Second Message:')
    print(prettyPrintHexList(list(m1)))
    print('Digest:')
    print(prettyPrintHexList(list(d1)))

test()
