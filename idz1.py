#!/usr/bin/env python3
# -*- coding: utf-8 -*-

text = input("Введите предложение: ")

x1 = text.index("с")
x2 = text.index("т")

if x1 > x2:
    print("Бурква 'с' встречается позже")
else:
    print("Бурква 'т' встречается позже")
