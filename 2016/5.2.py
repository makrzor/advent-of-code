#!/usr/bin/env python
import hashlib

DOOR_ID = "cxdnnyjw"

index = 0
password = ['g'] * 8
password_ro = ['g'] * 8
hashee = DOOR_ID + str(index)
hash = hashlib.md5(hashee.encode('utf-8')).hexdigest()
while 'g' in password:
    while hash[:5] != "00000" or "89abcdef".find(hash[5:6]) != -1:
        index += 1
        hashee = DOOR_ID + str(index)
        hash = hashlib.md5(hashee.encode('utf-8')).hexdigest()
    password[int(hash[5:6])] = hash[6:7]
    if password_ro[int(hash[5:6])] == 'g':
        password_ro[int(hash[5:6])] = hash[6:7]
    index += 1
    hashee = DOOR_ID + str(index)
    hash = hashlib.md5(hashee.encode('utf-8')).hexdigest()
print("".join(password))
print("".join(password_ro))
# The second one is the proper one
