ans = int(input('Enter a Value: '))
root = 0
pwr = 0
while root < 10000:
   pwr = 0
   root = root + 1
   while pwr < 7:
       pwr = pwr + 1
       
       if ans == root**pwr:
           print ('the root is ',root,'and the power is ',pwr)

