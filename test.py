L = []
inp = input('Enter list values seperated by a comma(,): ')
val = ''
for i in inp:
    if i != ',':
        val += i
        if val == ' ':
            val = ''
    else:
        L.append((val))
        val = ''
        continue
L.append((val))
print(L)
# Using del L deletes the list and is not possible to print it again it will be subjected to error
del_index = int(input('Enter index to delete: '))
del L[del_index]
print(L)
upd_index = int(input('Enter index to update: '))
upd_val = input('Enter value to update: ')
L[upd_index] = upd_val
print(L)
