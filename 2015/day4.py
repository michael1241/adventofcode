#! /usr/bin/env python3

import hashlib

#print(hashlib.md5(f'yzbqklnj282749'.encode('utf-8')).hexdigest()[:5])

n = 0
while True:
	if hashlib.md5(f'yzbqklnj{n}'.encode('utf-8')).hexdigest()[:6] == "000000":
		print(n)
		break
	n += 1