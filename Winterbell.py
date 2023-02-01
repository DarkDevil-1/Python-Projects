# 1 - Eligibility to Vote
def vote():
    age = int(input('Enter your age: '))
    if age >= 18:
        print('You are eligible to vote')
    if age < 18:
        print('You are not eligible to vote')


# 2 - Largest Number of the 3
def largest():
    n1 = float(input('Enter n1: '))
    n2 = float(input('Enter n2: '))
    n3 = float(input('Enter n3: '))
    if n1 > n2 and n1 > n3:
        print(n1, 'Is the largest of the pack')
    if n2 > n1 and n2 > n3:
        print(n2, 'Is the largest of the pack')
    if n3 > n1 and n3 > n2:
        print(n3, 'Is the largest of the pack')


# 3- Odd or Even
def odev():
    number = int(input('Enter a number: '))
    if number % 2 == 0:
        print('A even number')
    else:
        print('Odd number')


# 4 - Types of Triangles
def triangles():
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    if a == b == c:
        print('Equilateral Triangle')
    elif a == b or b == c or a == c:
        print('Isosceles Triangle')
    else:
        print('Scalene Triangle')


# 5 - Quadratic Equation
def quad():
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    d = (b ** 2) - (4 * a * c)
    if d > 0:
        print('Two Real Roots')
    elif d == 0:
        print('One Real Root')
    else:
        print('No Real Roots')
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('The roots are: ', x1, x2)


# 6 - Calculator
def calculator():
    print('OPERATORS: +, -, *, /')

    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = input('Enter the operation: ')
    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '*':
        print(a * b)
    elif c == '/':
        print(a / b)
    else:
        print('Invalid Operation')


# 7 - Ascending Order
def ascending():
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    if a > b and a > c:
        if b > c:
            print(c, b, a)
        else:
            print(b, c, a)
    elif b > a and b > c:
        if a > c:
            print(c, a, b)
        else:
            print(a, c, b)
    elif c > a and c > b:
        if a > b:
            print(b, a, c)
        else:
            print(a, b, c)


# 8 - Factorial
def factorial():
    n = int(input('Enter a number: '))
    f = 1
    for i in range(1, n + 1):
        f = f * i
    print(f)


# 9 - Fibonacci Series
def fibonacci():
    n = int(input('Enter a number: '))
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)


# 10 - Number pattern
def pattern():
    n = int(input('Enter a number: '))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()


# 11 - Sum of Digits
def sumofdigits():
    n = int(input('Enter a number: '))
    s = 0
    while n > 0:
        r = n % 10
        s = s + r
        n = n // 10
    print(s)


# 12 - Palindrome
def palindrome():
    n = int(input('Enter a number: '))
    temp = n
    rev = 0
    while n > 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    if temp == rev:
        print('Palindrome')
    else:
        print('Not a Palindrome')


# 13 - Area of Shapes (Circle, Rectangle, Triangle)
def area():
    try:
        print('1. Circle')
        print('2. Rectangle')
        print('3. Triangle')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            r = int(input('Enter the radius: '))
            print('Area of the circle is: ', 3.14 * r * r)
        elif choice == 2:
            l = int(input('Enter the length: '))
            b = int(input('Enter the breadth: '))
            print('Area of the rectangle is: ', l * b)
        elif choice == 3:
            b = int(input('Enter the base: '))
            h = int(input('Enter the height: '))
            print('Area of the triangle is: ', 0.5 * b * h)
        else:
            print('Invalid Choice')
    except ValueError:
        print('Invalid Input')


# 14 - number speciality (Armstrong, Palindrome, Prime)
def quality():
    print('1. Armstrong')
    print('2. Palindrome')
    print('3. Prime')
    n = int(input('Enter a number: '))
    choice = int(input('Enter your choice: '))
    if choice == 1:
        temp = n
        s = 0
        while n > 0:
            r = n % 10
            s = s + r ** 3
            n = n // 10
        if temp == s:
            print('Armstrong')
        else:
            print('Not Armstrong')
    elif choice == 2:
        temp = n
        rev = 0
        while n > 0:
            r = n % 10
            rev = rev * 10 + r
            n = n // 10
        if temp == rev:
            print('Palindrome')
        else:
            print('Not a Palindrome')
    elif choice == 3:
        c = 0
        for i in range(1, n + 1):
            if n % i == 0:
                c = c + 1
        if c == 2:
            print('Prime')
        else:
            print('Not Prime')


# 15 - Short from of string
def short():
    s = input('Enter a string: ')
    l = s.split()
    for i in l:
        print(i[0], end='')


# 16 - UC and LC
def uc_lc():
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


# 17 - Vowel and Consonant
def vowel_consonant():
    string = input('Enter a word: ')
    vctr = 0
    cctr = 0
    for i in string:
        if i in 'aeiouAEIOU':
            vctr += 1
        else:
            cctr += 1
    print('You Entered', vctr, 'Vowels and', cctr, 'Consonants')


# 18 - Even and Odd list
def even_odd():
    L = []
    inp = input('Enter list values seperated by a comma(,): ')
    val = ''
    for i in inp:
        if i != ',':
            val += i
            if val == ' ':
                val = ''
        else:
            L.append(int(val))
            val = ''
            continue
    L.append(int(val))
    print(L)
    E = []
    O = []
    G = []
    for i in L:
        if i % 2 == 0:
            E.append(i)
            G.append(int(i / 2))
        else:
            O.append(i)
            G.append(int(i * 3))
    print('Even List:', E, '\nOdd List:', O)
    print(G)


# 19 - Sum of list
def list_sum():
    L = []
    inp = input('Enter list values seperated by a comma(,): ')
    val = ''
    for i in inp:
        if i != ',':
            val += i
            if val == ' ':
                val = ''
        else:
            L.append(int(val))
            val = ''
            continue
    L.append(int(val))
    print(L)
    sum = 0
    for i in L:
        sum += i
    print('Sum of list:', sum)


# 20 - Mean of list
def mean_of_list():
    L = []
    inp = eval(input('Enter list: '))
    for i in inp:
        L.append(i)
    sum = 0
    for i in L:
        sum += i
    avg = sum / len(L)
    print(avg)


# 21 -Sum of elements in tuple
def sum():
    T = ()
    inp = input('Enter tuple values seperated by a comma(,): ')
    val = ''
    for i in inp:
        if i != ',':
            val += i
            if val == ' ':
                val = ''
        else:
            T = T + (int(val),)
            val = ''
            continue
    T = T + (int(val),)
    print(T)
    sum = 0
    for i in T:
        sum += i
    print('Sum of tuple:', sum)


# 22 - Convertion of list to tuple
def list_to_tuple():
    L = []
    inp = input('Enter list values seperated by a comma(,): ')
    val = ''
    for i in inp:
        if i != ',':
            val += i
            if val == ' ':
                val = ''
        else:
            L.append(int(val))
            val = ''
            continue
    L.append(int(val))
    print(L)
    T = tuple(L)
    print(T)


# 23 - Student marks in dictionary
def student_marks():
    D = {}
    n = int(input('Enter number of students: '))
    for i in range(n):
        name = input('Enter name of student: ')
        marks = int(input('Enter marks of student: '))
        D[name] = marks
    print(D)
    for i in D:
        if D[i] >= 90:
            print(i, 'has got A+')
        elif D[i] >= 80:
            print(i, 'has got A')
        elif D[i] >= 70:
            print(i, 'has got B+')
        elif D[i] >= 60:
            print(i, 'has got B')
        elif D[i] >= 50:
            print(i, 'has got C+')
        elif D[i] >= 40:
            print(i, 'has got C')
        else:
            print(i, 'has got F')


# 24 - Employee details in dictionary
def employee_details():
    D = {}
    n = int(input('Enter number of employees: '))
    for i in range(n):
        name = input('Enter name of employee: ')
        salary = int(input('Enter salary of employee: '))
        D[name] = salary
    print(D)
    for i in D:
        if D[i] >= 100000:
            print(i, 'has got bonus of 10%')
        elif D[i] >= 50000:
            print(i, 'has got bonus of 5%')
        else:
            print(i, 'has got bonus of 2%')


# 25 - Keys and values in dictionary
def keys_values():
    D = {}
    n = int(input('Enter number of elements: '))
    for i in range(n):
        key = input('Enter key: ')
        value = input('Enter value: ')
        D[key] = value
    print(D)
    print('Keys:', D.keys())
    print('Values:', D.values())


# 26 - Phonebook
def phonebook():
    D = {}
    n = int(input('Enter number of entries: '))
    for i in range(n):
        name = input('Enter name: ')
        number = input('Enter number: ')
        D[name] = number
    print(D)
    name = input('Enter name to search: ')
    if name in D:
        print('Number:', D[name])
    else:
        print('Not found')


# 27 - String functions
def string_functions():
    string = input('Enter a string: ')
    print('Length:', len(string))
    print('Uppercase:', string.upper())
    print('Lowercase:', string.lower())
    print('Capitalized:', string.capitalize())
    print('Title:', string.title())
    print('Reversed:', string[::-1])


# 28 - List functions
def list_functions():
    L = []
    inp = input('Enter list values seperated by a comma(,): ')
    val = ''
    for i in inp:
        if i != ',':
            val += i
            if val == ' ':
                val = ''
        else:
            L.append(int(val))
            val = ''
            continue
    L.append(int(val))
    print(L)
    print('Length:', len(L))
    print('Maximum:', max(L))
    print('Minimum:', min(L))
    print('Sorted:', sorted(L))
    print('Reversed:', L[::-1])
    print('Reversed sorted:', sorted(L)[::-1])
    print('Reversed sorted:', sorted(L, reverse=True))
    print('Reversed sorted:', sorted(L, reverse=False))
