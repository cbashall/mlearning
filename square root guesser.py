x = 25
epsilon =0.01
step = epsilon**2
numguess = 0
ans = 0
while abs(ans**2 - x) >= epsilon and ans*ans <= x:
    ans += step
    numguess += 1
print ('numguess =', numguess)
if abs(ans**2 - x) >= epsilon:
    print ('failed on square root of ', x , ans)
else:
    print (ans, 'is close to square root of ', x)
