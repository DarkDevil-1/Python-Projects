import math
import sys


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
            break


def wap():
    while True:
        try:
            print('*' * 20, 'Enter Any Number', '*' * 20)
            n1 = int(input('Enter Number'))
            if n1 == 0:
                print('\nYour number is 0, which carries no value')
            elif n1 > 0:
                print('\nYour number is positive')
            elif n1 < 0:
                print('\nYour number is negative')
        except ValueError:
            print('ERROR')
        else:
            break


def train():
    while True:
        try:
            n1 = float(input('Enter side 1:'))
            n2 = float(input('Enter side 2:'))
            n3 = float(input('Enter side 3:'))
            EX = n1 == n2
            y = n2 == n3
            z = n1 == n3
            if EX and y and z:
                print('Given triangle is Equilateral')
            elif EX or y or z:
                print('Given Triangle is Isosceles Triangle')
            elif not EX and not y and not z:
                print('Given Triangle is Scalene Triangle')
            else:
                print('Please enter a number')
                print('=' * 60, 'RESTART', '=' * 60)
        except ValueError:
            print('Error')
            print('Please enter a number')
            print('=' * 60, 'RESTART', '=' * 60)
        else:
            break


def x():
    while True:
        try:

            n1 = float(input('Enter n1: '))
            n2 = float(input('Enter n2: '))
            n3 = float(input('Enter n3: '))
            if n1 > n2 and n1 > n3:
                print(n1, 'Is the largest of the pack')
            if n2 > n1 and n2 > n3:
                print(n2, 'Is the largest of the pack')
            if n3 > n1 and n3 > n2:
                print(n3, 'Is the largest of the pack')
        except ValueError:
            print('ERROR!, ENTER A FLOAT VALUE')
        else:
            break


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
                root1 = (-b + math.sqrt(delta)) / 2 * a
                root2 = (-b - math.sqrt(delta)) / 2 * a
                if delta == 0:
                    print('\nThe roots of the equation')
                    print(a, 'x^2 + ', b, 'x + ', c, ' = 0', sep='')
                    print('\nIS =', [root1, root2])
                    print('The roots of this equation are real and equal')
                elif delta > 0:
                    print('\nThe roots of the equation')
                    print(a, 'x^2 + ', b, 'x + ', c, ' = 0', sep='')
                    print('\nIS =', [root1, root2])
                    print('The roots of this equation are real and distinct')
                elif delta < 0:
                    root1 = (-b + (delta ** 0.5)) / 2 * a
                    root2 = (-b - (delta ** 0.5)) / 2 * a
                    print('\nThe roots of the equation')
                    print(a, 'x^2 + ', b, 'x + ', c, ' = 0', sep='')
                    print('IS =', [root1, root2])

                    print('\nThe roots are complex and imaginary')
            print('\nProgram Over')
        except ValueError:
            error()
        else:
            break


def division():
    while True:
        try:
            print('Enter Your marks Out of 100')
            sub1 = float(input('Enter Marks in Science: '))
            sub2 = float(input('Enter Marks in Math: '))
            sub3 = float(input('Enter Marks in English: '))
            sub1 = sub1 / 100
            sub2 = sub2 / 100
            sub3 = sub3 / 100
            total_percentage = (sub1 + sub2 + sub3) / 3 * 100
            if total_percentage >= 85:
                print('You are in top 500 of candidates that passed the exam, First Division, A+')
            elif total_percentage >= 44:
                print('You are in the Mid Division, B+')
            elif total_percentage >= 31:
                print('You are in the Third Division, C+')
            elif total_percentage < 30:
                print('You have failed the exam, F-')

        except ValueError:
            error()
        else:
            break


def discount():
    while True:
        try:
            bill = float(input('Enter Your Bill amount: '))
            if bill >= 20000:
                dx = bill * 25 / 100
                print(bill - dx, 'Is the discounted amount you have to pay with the discount to be', dx)
            elif bill >= 15000:
                dx = bill * 15 / 100
                print(bill - dx, 'Is the discounted amount you have to pay with the discount to be', dx)
            elif bill >= 10000:
                dx = bill * 10 / 100
                print(bill - dx, 'Is the discounted amount you have to pay with the discount to be', dx)
            elif bill < 10000:
                print('We cant offer you any discount , peasant')
        except ValueError:
            print('Error, Enter a valid number. Try again')
        else:
            break


def descend():
    while True:
        try:
            n1 = int(input('Enter no1: '))
            n2 = int(input('Enter no2: '))
            n3 = int(input('Enter n3: '))
            one = n1
            two = n2
            three = n3

            if n1 > n2 > n3:
                print(one, '>', two, '>', three)
            elif n2 > n3 > n1:
                print(two, '>', three, '>', one)
            elif n2 > n1 > n3:
                print(two, '>', one, '>', three)
            elif n3 > n1 > n2:
                print(three, '>', one, '>', two)
            elif n3 > n2 > n1:
                print(three, '>', two, '>', one)
            elif n1 > n3 > n2:
                print(one, '>', three, '>', two)
            elif n1 > n3 and n1 == n2:
                print(one, '=', two, '>', three)
            elif n3 > n2 and n3 == n1:
                print(one, '=', three, '>', two)
            elif n3 > n1 and n3 == n2:
                print(three, '>', two, '>', one)
            else:
                print(one, '=', two, '=', three)
            print('Descending Order')
        except ValueError:
            error()
        else:
            break


def ascend():
    while True:
        try:
            n1 = int(input('Enter no1: '))
            n2 = int(input('Enter no2: '))
            n3 = int(input('Enter n3: '))

            ass = [n1, n2, n3]
            ass.sort()
            print(ass, 'Is the ascending order')

        except ValueError:
            error()
        else:
            break


def choices():
    while True:
        try:
            i = input('Do you want to Ascending Order or descending order (A/D) : ')
            if i == 'A':
                ascend()
                break
            if i == 'D':
                descend()
            elif i != 'A' or 'D':
                error()
                continue
        except ValueError:
            error()
        else:
            break


def fact():
    while True:
        try:
            num = int(input('Enter Number:'))
            if num == 0:
                print('Factorial of 0 is 1')
            elif num < 0:
                print('Factorial does not exist for -ve numbers')
            else:
                factorial = 1
                index = 1
                while index <= num:
                    factorial *= index
                    index += 1
                print('The Factorial of', num, 'is', factorial)
        except ValueError:
            error()
        else:
            break


def abc():
    while True:
        try:
            letter = input('Enter a Alphabet:')
            vowel = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
            if letter.isnumeric():
                error()
                print('\n')
                continue
            elif len(letter) > 1:
                print('Enter a single Alphabet\n')
                continue
            else:
                if letter in vowel:
                    print('Given Alphabet is a vowel')
                else:
                    print('Given Alphabet is a consonant')
        except ValueError:
            error()
        else:
            break


def number():
    num = input('Enter number: ')
    summation = 0
    for i in num:
        i = int(i)
        summation += i
    print(summation)


def count():
    while True:
        try:
            n1 = int(input('Enter number 1: '))
            n2 = int(input('Enter number 2: '))
            cunt = 0
            for i in range(n1):
                for y in range(n2):
                    cunt += 1
            print(cunt)
        except ValueError:
            error()
        else:
            break


def average():
    name = input('Enter You Name:')
    mark1 = float(input('Enter English Marks:'))
    mark2 = float(input('Enter Math Marks:'))
    mark3 = float(input('Enter Science Marks:'))

    conv1 = mark1 / 40 * 100
    conv2 = mark2 / 40 * 100
    conv3 = mark3 / 40 * 100

    total_perc = int((mark1 + mark2 + mark3) / 120 * 100)

    print('HI', name, 'YOU SCORED AN AVERAGE OF', total_perc, '%''\n'
                                                              'You Scored', conv1, '% in English''\n'
                                                                                   'You Scored', conv2, '% in Maths''\n'
                                                                                                        'You Scored',
          conv3, '% in Science')


def temperature():
    while True:
        try:
            temp = float(input('Enter temperature: '))
            choice_input = input('Enter unit of temperature (F/C): ')

            if choice_input == 'F':
                cel = (temp - 32) * 5 / 9
                print('Given temperature in Celsius(C) is:', cel)

            elif choice_input == 'C':
                far = (temp * 9 / 5) + 32
                print('Given temperature in Fahrenheit(F) is:', far)

            else:
                print('Please Enter a Valid Unit')
        except ValueError:
            error()
        else:
            break


def str_manipulation_1():
    name = input('Enter Your Name: ')
    for i in name:
        if i == name[-1]:
            print(i)
        else:
            print(i + '-', end='')


def revstr():
    name = input('Enter Your Name: ')
    for i in range(-1, -len(name) - 1, -1):
        print(name[i], end='')


def shorty():
    word = input('Enter a word: ')
    out = ''
    for i in range(0, len(word)):
        if word[i] == word[0]:
            out += word[0]
        elif word[i - 1] == ' ':
            out += word[i]
        else:
            continue

    out = out.upper()

    for i in out:
        print(i + '.', end='')


def vowel_count():
    inp = input('Enter a word: ')
    v_count = 0
    if inp.isnumeric():
        error()
    for i in inp:
        if i in 'aeiouAEIOU':
            v_count += 1
    print('Number of vowels:', v_count)


def pattern_1():
    string = input('Enter a symbol: ')
    lines = int(input('Enter Number of lines: '))
    out = ''
    for i in range(lines):
        out += string
        print(out)


def count_str():
    string = input('Enter a word: ')
    upctr = 0
    dnctr = 0
    dictr = 0
    wstr = 0
    for i in string:
        if i.isupper():
            upctr += 1
        if i.islower:
            dnctr += 1
        if i.isdigit():
            dictr += 1
        if i.isspace():
            wstr += 1
    print('You Entered', upctr, 'Uppercase Letters', dnctr, 'Lowercase Letters', dictr, 'Digits and', wstr, 'Spaces')


def count_str_2():
    line = input('Enter a line or sentence: ')
    word = input('Enter a word or letter to count: ')
    ctr = 0

    if len(word) > 1:
        line = line.split()
        for i in line:
            if i == word:
                ctr += 1
        print('The word "{}" appears {} times in the line.'.format(word, ctr))
    else:
        ctr = line.count(word)
        print('The letter "{}" appears {} times in the line.'.format(word, ctr))
