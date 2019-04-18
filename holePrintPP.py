#!/usr/bin/python3
# -*- coding: utf-8 -*-

a, f, p, r, e = [109, 80, 110, 97], chr, print, 'r', 'utf-8'
ぴ,な,s=(f(a[1])+"i",        "".join([f(x) for x in
                                     a[2:]]), " ")
p(s.join([ぴ + な,              f(a[1])+r]),end='')
rg=str().join([             "OG".lower(), r,
                              f(a[-1]), f(a[0])*2])
p(rg+"ie", end='')
p(r +                         f(bytes(r,e)[0]+2))
