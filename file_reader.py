# filename = 'C:/Users/NYK/Desktop/Learning Python/umat_lab3/pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line)
          
filename = 'C:/Users/NYK/Desktop/Learning Python/umat_lab3/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string)-2)
