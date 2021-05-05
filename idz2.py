'''
Дано слово. Поменять местами его третью и последнюю буквы.
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    slovo = input("Введите слово: ")

    x = [slovo[-1], slovo[2],]
    y = slovo[0:2] + x[0] + slovo[3:-1] + x[1]

    print (y)
