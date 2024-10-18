import os
import time


WHITE = '\u001b[47m'
BLUE = '\u001b[46m'
RED = '\u001b[41m'
END = '\u001b[0m'
PURPLE = '\u001b[45m'
CLEAR = '\033[2H'

def var():
    os.system("cls")
    print("вариант №4")
    time.sleep(3)
    os.system("cls")


def flag():
    for i in range(4):
        print(line(WHITE, 30))
    for i in range(4):
        print(line(RED, 30))
    time.sleep(3)
    os.system("cls")

def line(color, lenght):
    return color + ' '*lenght + END

def patt(color):
    step = ' '
    lenght = 30
    half_lenght = lenght//2 - 1
    quarter_lenght = lenght//4 - 1

    for i in range (lenght):
        print(CLEAR)
        print(line(color, i))
        time.sleep(0.02)
    
    print(step*half_lenght + line(color, 2) + step*half_lenght)

    for i in range (lenght):
        print(CLEAR+'\n'*2)
        print(line(color, i))
        time.sleep(0.02)

    print(step*quarter_lenght + line(color, 2) + step*quarter_lenght*2 +  line(color, 2))

    for i in range (lenght):
        print(CLEAR+'\n'*4)
        print(line(color, i))
        time.sleep(0.02)
    time.sleep(1)
    os.system("cls")

def chart():
    print('y=x^0.5')
    m = [[1 if round(j**0.5) == i else 0 for j in range(1, 145)] for i in range(1, 12)]
    for i in range(10, -1, -1):
        for j in m[i]:
            print(' ', end='') if j==0 else print(line(PURPLE,1), end='')
        print()
    time.sleep(3)
    os.system("cls")

def sequence():
    s = [abs(float(x)) for x in open('sequence.txt').readlines()]
    s1 = s[:125]
    s2 = s[125:]
    average_s1 = sum(s1)/len(s1)
    average_s2 = sum(s2)/len(s2)
    print(f'Среднее значение по модулю первых 125 чисел равно {average_s1}\nСреднее значение по модулю вторых 125 чисел равно {average_s2}')
    
var()
flag()
[patt(color) for color in [PURPLE, WHITE, BLUE]]
chart()
sequence()