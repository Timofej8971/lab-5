'''
Дан текст. Найти наибольшее количество идущих подряд цифр.
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    text = input("Введите текст, содержащий символы: ")

    i = 0
    otvet = 0
    for simvol in " "+text+" ":
        if (simvol.isdigit()):
            i += 1
        else:
            if otvet < i:
                otvet = i
            i = 0

    print(otvet)
