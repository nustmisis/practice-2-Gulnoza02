# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:05:53 2023

@author: workk



Упражнение 61. Действительный номерной знак машины?
(Решено. 28 строк)
Допустим, в  нашей стране старый формат номерных знаков автомобилей состоял из трех заглавных букв, следом за которыми шли три цифры. 
После того как все возможные номера были использованы, формат был 
изменен на четыре цифры, предшествующие трем заглавным буквам.
Напишите программу, запрашивающую у пользователя номерной знак 
машины и оповещающую о том, для какого формата подходит данная последовательность символов: для старого или нового. Если введенная последовательность не соответствует ни одному из двух форматов, укажите 
это в сообщении
"""
number = input("Введите номерной знак машины:")
if len(number) ==6:
    # Проверка староо формата: три заглавные буквы, за которыми следует три цифры
    if number[:3].isalpha() and  number [3:].isdigit():
        print("номероной знак соответствует старому формату.")
    else:
        print("номероной знак  не соответствует ни одному из формату.")
     elif len(number) ==    7
# Проверка нового формата: четыре цифры за которыми следует три загалованые буквы
if number [:4]. isdigit() and number [4:].  isalpha():
    print ("Новый знак соответсьвует новому формату .")
else:
    print("Номерной знак не соответствует н одному из форматов .")
else:
print("Номерной знак не соответствует ри одному из форматов.")