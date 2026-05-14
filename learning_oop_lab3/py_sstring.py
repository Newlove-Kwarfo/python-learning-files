filename = 'umat_lab3/pi_million_digits.txt'

with open(filename) as file:
    lines = file.readlines()

py_string = ''
for line in lines:
    py_string += line.strip()

# print(py_string[:52])
# print(len(py_string))

birthday = input('Enter you birthday in the form ddmmyy: ')
if birthday in py_string:
    print('Your birhtday is found in the first million digits of pi!')
else:
    print('Your bithday is not found in the first million digits of pi')