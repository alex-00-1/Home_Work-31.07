# ДЗ 3.1. Найпростіший калькулятор

num1, num2 = int(input("Ведіть перше число: ")), int(input("Введіть друге число: "))
sign = input("Введіть арефметичний знак: ")

if sign == "+":
    print(f'{num1} + {num2} = {num1 + num2}')

if sign == "-":
    print(f'{num1} - {num2} = {num1 - num2}')

if sign == "*":
    print(f'{num1} * {num2} = {num1 * num2}')

if sign == "/":
    if num2 == 0:
        print("На нуль ділити не можна !!!")
        num2 = int(input("Змініть значення для другого числа: "))
        if num2 == 0:
            print('Почни з початку')
        else:
            print(f'{num1} / {num2} = {num1 / num2}')
        
    else:
        print(f'{num1} / {num2} = {num1 / num2}')