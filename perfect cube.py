#find the cube root of the perfect cube
x = int(input('Enter and int: '))
answ = 0
while answ**3 < abs(x):
            answ = answ + 1
if answ**3 != abs(x):
        print (x, 'is not a perfect cube')
else:
        if x < 0:
            answ = -answ
        print ('cube root of' , x, 'is' , answ)
