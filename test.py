# MARKS AVERAGE
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
                                                                                                    'You Scored', conv3,
      '% in Science')

# TEMPERATURE

celsius = int(input('Insert Temperature in Celsius:'))
fahrenheit = int(input('Insert Temperature in Fahrenheit:'))
w = input('F OR C YOU WANT TO CONVERT:')
if w == 'C':
    far = (celsius * 9 / 5) + 32
    print('Your Fahrenheit IS:', far)
elif w == 'F':
    cel = (fahrenheit-32)*5/9
    print(cel)
