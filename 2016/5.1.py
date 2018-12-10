#!/usr/bin/env python
import hashlib

DOOR_ID = "cxdnnyjw"

index = 0
password = ""
hashee = DOOR_ID + str(index)
hash = hashlib.md5(hashee.encode('utf-8')).hexdigest()
for i in range(8):
    while hash[:5] != "00000":
        index += 1
        hashee = DOOR_ID + str(index)
        hash = hashlib.md5(hashee.encode('utf-8')).hexdigest()
    password += hash[5:6]
    index += 1
    hashee = DOOR_ID + str(index)
    hash = hashlib.md5(hashee.encode('utf-8')).hexdigest()
print(password)
