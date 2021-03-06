#!/usr/bin/python
import time

def xor (m1, m2):
    return "".join(map(lambda a: chr(ord(a[0])^ord(a[1])), zip(m1, m2)))
   
def xor2 (l):
    return "".join(map(lambda a: chr(a[0]^a[1]), l))
       
def findEqualWord(wordList, m1xm2):
    for w1 in wordList:
        for w2 in wordList:
            xored =  xor(w1, w2)
            if xored == m1xm2:
                return w1 + " und " + w2
       
m1 = [0xC2, 0x68, 0x32, 0x5C, 0xD2, 0xC3, 0x85, 0x73]
m2 = [0xC5, 0x63, 0x23, 0x5D, 0xDE, 0xCC, 0x87, 0x7D]

t0 = time.time()

print findEqualWord (open('8_letter_words.txt').read().split('\n'), xor2(zip(m1, m2)))

print time.time() - t0





