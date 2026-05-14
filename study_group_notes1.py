"""
house_price = 1000000
good_credit = True
if good_credit:
    down_payment = .1 * house_price
    print(down_payment)
else:
    down_payment = .2 * house_price
    print(down_payment)
"""

"""
a = 15
b =10
c =3

if a>b and a>c:
    print('a is the greatest')
elif b>a and b>c:
    print('b is the greatest')
elif c>a and c>b:
    print('c is the greatest')
"""

"""
x=False
if not x:
    print('True')
else:
    print('False')
"""

numbers = [1,9,6,4,5]

"""
#add to list
numbers.append('eye')
print(numbers)

#put new value at index ans shift values down
numbers.insert(2, 'fish')
print(numbers)


#removing item
numbers.remove('fish')
print(numbers)

#pop rmeoves last value in the list
x = numbers.pop()
print(numbers)
print(x)

#sorting temprorily
x = sorted(numbers)
print(x)
print(numbers)

#sort permanently
x = numbers.sort()
print(numbers)

#reverse permanently
numbers.reverse()
print(numbers)


y = numbers[::-1]
print(y)

del(numbers[2])
print(numbers)
"""
newNumbers = [1,2,3,4,5]

#Iterates through and prints new num
for num in newNumbers:
    print(num)
    
#does the sme as above
for num in range(0,len(newNumbers)):
    print(newNumbers[num])
    
for num in newNumbers:
    if num %2 == 0:
        print('Even')
    elif num % 2 ==1:
        print('Odd')
        
for num in range(1,21):
    if (num % 5 == 0) and (num % 3 == 0):
        print(num)
        print('fizzbuzz')
    elif num % 3 == 0:
        print(num)
        print('fizz')
    elif num % 5 == 0:
        print(num)
        print('buzz')

        