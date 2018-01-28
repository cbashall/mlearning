x = int(input('Value of X:'))
y = int(input ('Value of Y:'))
z = int(input ('value of Z:')) 

if x%2 != 0 and y%2 != 0 and z%2 != 0:
    if x > y and x  > z:
        print (x, 'is the largest odd number')
    elif y > z:
        print (y, 'is the largest odd number')
    elif z > y:
        print (z, ' is the largest odd number')
    elif x == y and y == z:
        print (x, ' all values are equal and odd')
        
elif x%2 != 0 and y%2 != 0 and z%2 == 0:
    if x > y:
        print (x,' is the largest odd number')
    else:
        print (y, ' is the largest odd value')
elif x%2 != 0 and y%2 == 0 and z%2 != 0:
    if x > z:
        print (x, ' is the larget odd number')
    else:
        print (z, ' is the largedst odd number')
elif x%2 == 0 and y%2 != 0 and z%2 != 0:
    if y > z:
        print (y, ' is the larget odd number')
    else:
        print (z, ' is the largest odd number')
elif x%2 == 0 and y%2 != 0 and z%2 == 0:
        print (y, ' is the only Negative number')
elif  x%2 == 0 and y%2 == 0 and z%2 == 0:
        print ('all numbers are even')
elif x == y and y == z:
        print (x, 'is the largest value and they are the same')
else:
        print ('error')
    

