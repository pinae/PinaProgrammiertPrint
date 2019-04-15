#!/usr/bin/python3
# -*- coding: utf-8 -*-

a, f, r = ([109, 80, 110, 97], chr, 'r')
ぴ, な = f(a[1])+"i", ''.join([f(x) for x in a[2:]])
print(" ".join([ぴ + な, f(a[1]) + r]), end=str())
rg = ''.join(["OG".lower(), r, f(a[-1]), f(a[0])*2])
print(rg + "ie" + r + chr(bytes(r, 'utf-8')[0]+2))
