import math
import sys
import random
import time


def error():
    print('You have entered an Invalid value. Please try the program again. Thank You')
    print('=' * 80, 'RESTART', '=' * 80)


def calc():
    while True:
        print(
            '***** FOR LOGARITHM, ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION, SQUARE-ROOT, POWER, RADIAN, DEGREE, '
            'REMAINDER *****')
        print('OPERATORS = log , + , - , * , /, %, sqrt , ^, rad, deg')

        try:
            num1 = float(input('Number 1 here:'))
            op = input('Enter Operator:')
            operator = 'log', '+', '-', '^', '*', '/', 'sqrt', 'rad', 'deg'
            if op not in operator:
                print('Invalid Operator')
                sys.exit()
            if op == 'log':
                log = math.log10(num1)
                print('Answer:', log)
            elif op == 'rad':
                rad = math.radians(num1)
                print(rad)
            elif op == 'deg':
                deg = math.degrees(num1)
                print(deg)
            elif op == 'sqrt':
                sqrt = math.sqrt(num1)
                print('Answer:', sqrt)
            else:
                num2 = float(input('Number 2 here:'))
                if op == '+':
                    print('Answer:', num1 + num2)
                elif op == '-':
                    print('Answer:', num1 - num2)
                elif op == '/':
                    print('Answer:', num1 / num2)
                elif op == '*':
                    print('Answer:', num1 * num2)
                elif op == '^':
                    power = math.pow(num1, num2)
                    print('Answer:', power)
                elif op == '%':
                    val = num1 % num2
                    print('Answer:', val)
        except ValueError:
            error()
        else:
            what()
            break


def masc():
    print('ree')


def age():
    while True:
        try:
            a = int(input('Enter Year Born: '))
            c = int(input('Enter Month born in number (1,2,3...12): '))
            b = int(input('Enter Current Year: '))
            d = int(input('Enter Current month in number (1,2,3...12): '))

            if a > b or d > 12:
                print('HMM-MMMM WHAT, i think you just broke my sys-')
            else:
                b -= a
                if d == c:
                    print('You are', b, 'years old')
                elif d > c:

                    c = d - c
                    print('You are', b, 'years and', c, 'months Old')
                    if b < 18:
                        print('\n ( ͡° ͜ʖ ͡°)')
                else:
                    b = b - 1
                    c = 12 - (c - d)
                    print('You are', b, 'years and', c, 'months Old')
                    if b < 18:
                        print('\n ( ͡° ͜ʖ ͡°)')
        except ValueError:
            print('\n')
        else:
            time.sleep(3)
            jas()
            what()
            break


def jas():
    print('\nA - Arithmetic Calculator', '\nB - Age Calculator', '\nC - Squares And Cubes',
          '\nD - Quadratic Roots',
          '\nE - Guess The Number Game', '\nF - Area Of Rectangle,Triangle,Circle', '\nEX - EXIT', end='\n')

    print('\nENTER OPTION IN CAPITAL (A, B, C, D, E, F, EX)\n')


def what():
    while True:
        try:

            print('If EX does not work after doing a program please try again :)\n')
            opinion = input('Enter Option: ')
            if opinion == 'A':
                print('\n')
                calc()
            elif opinion == 'B':
                age()
            elif opinion == 'C':
                square()
            elif opinion == 'D':
                quad()
            elif opinion == 'E':
                guess()
            elif opinion == 'F':
                area()
            elif opinion == 'EX':
                break
            else:
                error()

        except ValueError:
            error()
        else:
            what()
            break


def leap():
    while True:
        try:
            print('************* PRINTS IF GIVEN YEAR IS A LEAP YEAR OR NOT **************')
            inp = int(input('Enter Any Year:'))
            x = inp % 4
            if inp < 1000:
                print('Enter a year over 1000')
            elif x == 0:
                print(inp, 'is a leap year')
            elif x != 0:
                print(inp, 'Is not a leap year')
            else:
                error()
        except ValueError:
            error()
        else:
            time.sleep(3)
            jas()
            what()
            break


def guess():
    while True:
        try:
            print('*' * 7, 'Guess The Number', '*' * 7, '\n')
            number = random.randrange(1, 20, 1)
            ctr = 0
            while ctr < 10:
                brass = int(input('Guess a Number between 0-20:'))
                print('********* You have', 9 - ctr, 'tr(ies/y) ************')
                if brass == number:
                    print('You got it right :)')
                    break
                else:
                    ctr += 1
            if not ctr < 10:
                print('\nYou Failed :( \nThe number was', number, )
        except ValueError:
            error()
        else:
            jas()
            what()
            break


# SUM OF ALL NUMBERS FROM ENTERED NUMBER - if enter 5 then 1+2+3+4+5

def first():
    print("****** FIND HOW THE SUMS OF THE EVEN AND ODD NUMBERS IN THE FIRST 'n' NUMBERS ******  ")
    n = int(input('Enter number:'))
    ctr = 1
    e_count = 0
    o_count = 0
    sum_odd = sum_even = 0
    while ctr <= n:
        if ctr % 2 == 0:
            sum_even += ctr
            e_count += 1
        else:
            sum_odd += ctr
            o_count += 1

        ctr += 1

    print('The sum of even numbers is', sum_even, '\nNo. of Even numbers =', e_count, end='\n')
    print('--------------------------\n')
    print('The sum of odd numbers is', sum_odd, '\nNo. of Odd numbers =', o_count, end='\n')
    print('----------PROGRAM FINISHED------------\n')


def quad():
    while True:
        try:
            print("************** QUADRATIC EQUATION ROOTS CALCULATOR **************")
            print('Of the form ax^2 + bx + c = 0')
            a = int(input('Enter value of A: '))
            b = int(input('Enter value of B: '))
            c = int(input('Enter value of C: '))

            if a == 0:
                print('THE VALUE OF A CANNOT BE 0, PLEASE TRY AGAIN')
            else:
                delta = b ** 2 - (4 * a * c)

                if delta == 0:
                    ex1 = (-b + math.sqrt(delta)) / 2 * a
                    ex2 = (-b - math.sqrt(delta)) / 2 * a
                    print('\nThe roots of the equation')
                    print(a, 'x^2 + ', b, 'x + ', c, ' = 0', sep='')
                    print('\nIS =', [ex1, ex2])
                    print('The roots of this equation are real and equal')
                elif delta > 0:
                    ex1 = (-b + math.sqrt(delta)) / 2 * a
                    ex2 = (-b - math.sqrt(delta)) / 2 * a
                    print('\nThe roots of the equation')
                    print(a, 'x^2 + ', b, 'x + ', c, ' = 0', sep='')
                    print('\nIS =', [ex1, ex2])
                    print('The roots of this equation are real and distinct')
                elif delta < 0:
                    ex1 = (-b + (delta ** 0.5)) / 2 * a
                    ex2 = (-b - (delta ** 0.5)) / 2 * a
                    print('\nThe roots of the equation')
                    print(a, 'x^2 + ', b, 'x + ', c, ' = 0', sep='')
                    print('IS =', [ex1, ex2])

                    print('\nThe roots are complex and imaginary')
            print('\nProgram Over')
        except ValueError:
            error()
        else:
            time.sleep(3)
            jas()
            what()
            break


def square():
    while True:
        try:
            print('*' * 9, 'THAHIR FILLING STATION , PAKISTAN', '*' * 9)
            print('\n Calculates Cubes or squares from 1 till number entered\n')
            num = int(input('Enter number: '))
            opinion = input('Do you want cubes or squares (C,S): ')
            ctr = num + 1
            if opinion == 'C':
                for i in range(1, ctr):
                    print(i, 'x', i, 'x', i, '=', i * i * i)
                print('\nThank You For using Thahir filling station')
            elif opinion == 'S':
                for i in range(1, ctr):
                    print(i, 'x', i, '=', i * i)
                print('\nThank You For using Thahir filling station')
            else:
                error()
        except ValueError:
            error()
        else:
            time.sleep(3)
            jas()
            what()
            break


def area():
    while True:
        try:
            print('***** AREA OF RECTANGLE *****')
            print('Get Access to triangle and circle by skipping over deez')
            loo = input('Do you want to skip (yes/no):')
            yes = 'Yes', 'yes', 'YES'
            no = 'No', 'NO', 'no'
            if loo in yes:
                var = input('Do you want circle or triangle:')
                circle = 'circle', 'Circle', 'CIRCLE'
                train = 'triangle', 'TRIANGLE', 'Triangle'
                if var in circle:
                    print('**** YOU HAVE UNLOCKED AREA OF CIRCLE ****')
                    r = int(input('Enter the radius:'))
                    g = input('Enter unit:')
                    pi = 22 / 7
                    a = pi * r ** 2
                    print('\n', a, g)
                elif var in train:
                    print('**** YOU HAVE UNLOCKED AREA OF TRIANGLE ****')
                    b = int(input('Enter Base Of triangle:'))
                    h = int(input('Enter Height of triangle:'))
                    g = input('Enter unit:')
                    half = 1 / 2
                    a = half * b * h
                    print('\nArea of the Triangle :', a, g)
                else:
                    print('NAH YOUR BLACK')
            elif loo in no:
                a = int(input('Enter length of Rectangle:'))
                b = int(input('Enter breadth of Rectangle:'))
                g = input('Enter unit:')
                x = a * b
                print('\nAREA OF RECTANGLE =', x, g)
            else:
                print('Batman is dark so is your skin(if your white then its your heart)')
        except ValueError:
            error()
        else:
            time.sleep(3)
            jas()
            what()
            break
def xox():
    L = []
    inp = input('Enter list values seperated by a comma(,): ')
    val = ''
    for i in inp:
        if i != ',':
            val += i
            if val == ' ':
                val = ''
        else:
            if val.isdigit():
                L.append(int(val))
                val = ''
            else:
                L.append(val)
                val = ''
            continue
    if val.isdigit():
        L.append(int(val))
    else:
        L.append(val)
    print(L)
    # Using del L deletes the list and is not possible to print it again it will be subjected to error
    del_index = int(input('Enter index to delete: '))
    del L[del_index]
    print(L)
    upd_index = int(input('Enter index to update: '))
    upd_val = input('Enter value to update: ')
    L[upd_index] = upd_val
    print(L)


xox()