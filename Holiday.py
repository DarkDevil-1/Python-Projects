# Holiday Homework 2022
import math
import sys


# An error function to be used for different programs below in a loop
def error():
    print('You have entered an Invalid value. Please try the program again. Thank You')
    print('=' * 80, 'RESTART', '=' * 80)


# Eligibility to Vote
def vote():
    while True:
        try:
            age = int(input('Enter current age in whole number: '))
            if age >= 18:
                print('You are eligible to vote in the elections :)')
            else:
                x = 18 - age
                print('You are not eligible to vote in the elections, You would be able to in a matter of', x,
                      'year(s)')
        except ValueError:
            error()
        else:
            break


# Greatest of 3 integers
def integers():
    while True:
        try:

            n1 = int(input('Enter Integer 1: '))
            n2 = int(input('Enter Integer 2: '))
            n3 = int(input('Enter Integer 3: '))
            if n1 > n2 and n1 > n3:
                print(n1, 'Is the largest of the pack')
            elif n2 > n1 and n2 > n3:
                print(n2, 'Is the largest of the pack')
            elif n3 > n1 and n3 > n2:
                print(n3, 'Is the largest of the pack')
        except ValueError:
            error()
        else:
            break


# Type Of Triangle
def triangle():
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
            error()
        else:
            break


# Quadratic Roots Calculator
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


# Arithmetic Calculator
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


# Grade of Student
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


# Factorial of a number
def factorial():
    while True:
        try:
            num = int(input('Enter Number:'))
            if num == 0:
                print('Factorial of 0 is 1')
            elif num < 0:
                print('Factorial does not exist for -ve numbers')
            else:
                fact = 1
                index = 1
                while index <= num:
                    fact *= index
                    index += 1
                print('The Factorial of', num, 'is', fact)
        except ValueError:
            error()
        else:
            break


# Ascending Order of 3 numbers
def ascend():
    while True:
        try:
            n1 = float(input("Enter No.1: "))
            n2 = float(input("Enter No.2: "))
            n3 = float(input("Enter No.3: "))
            if n1 < n2:
                if n2 < n3:
                    print(n1, "<", n2, "<", n3)
                else:
                    if n1 < n3:
                        print(n1, "<", n3, "<", n2)
                    else:
                        print(n3, "<", n1, "<", n2)
            else:
                if n3 < n2:
                    print(n3, "<", n2, "<", n1)
                else:
                    if n3 < n1:
                        print(n2, "<", n3, "<", n1)
                    else:
                        print(n2, "<", n1, "<", n3)
        except ValueError:
            error()
        else:
            break


# Even or Odd
def evenorodd():
    while True:
        try:
            n1 = float(input('Enter number: '))
            if n1 % 2 == 0:
                print('Given number is an even number')
            else:
                print('Given number is an odd number')
        except ValueError:
            error()
        else:
            break


# Fibnoccii Series
def fib():
    while True:
        try:
            n1 = int(input("Please Enter the Fibonacci Number Range = "))
            First = 0
            Second = 1
            Sum = 0
            for i in range(0, n1):
                Sum = Sum + First
                Third = First + Second
                First = Second
                Second = Third
            print(f'The Sum of Fibonacci Series Numbers = {Sum}')
        except ValueError:
            error()
        else:
            break


# Number Pattern
def number():
    while True:
        try:
            num = int(input('Enter Number: '))
            x = 1
            for i in range(num):
                for j in range(i + 1):
                    print(x, end=" ")
                    x = x + 1
                x = 1
                print()
        except ValueError:
            error()
        else:
            break


# Sum of Digits of a Number
def digits():
    while True:
        try:
            num = int(input("Input a number (Max of 4 digits): "))
            x = num // 1000
            p = (num - x * 1000) // 100
            q = (num - x * 1000 - p * 100) // 10
            r = num - x * 1000 - p * 100 - q * 10
            print("The sum of digits in the number is", x + p + q + r)
        except ValueError:
            error()
        else:
            break


# Palindrome
def palindrome():
    while True:
        try:
            n = int(input("Enter number:"))
            temporary = n
            reverse = 0
            while n > 0:
                digit = n % 10
                reverse = reverse * 10 + digit
                n = n // 10
            if temporary == reverse:
                print("Given number is a Palindrome")
            else:
                print('Given number is not a Palindrome')
        except ValueError:
            error()
        else:
            break


# String Pattern Right Triangle
def string():
    value = input('Enter String: ')
    x = len(value)
    for i in range(x):
        for j in range(i + 1):
            print(value[j], end='')
        print()


# END OF HOLIDAY HOMEWORK


