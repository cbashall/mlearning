Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
x, y = 2 ,3
>>> print "x"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("x")?
>>> print ("x")
x
>>> x= 4
>>> print ("x")
x
>>> adad
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    adad
NameError: name 'adad' is not defined
>>> if x < y and x < z:
	print 'x is least'
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('x is least')?
>>> if x < y and x < z:
	print ('X is the smallest value')

	
>>> if x < y and x < z:
		print ('X is the smallest value')
	elif y < Z :
		
SyntaxError: unindent does not match any outer indentation level
>>> if x < y and x < z:
		print ('X is the smallest value')
	elif y < Z:
		
SyntaxError: unindent does not match any outer indentation level
>>> sample
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    sample
NameError: name 'sample' is not defined
>>> run sample
SyntaxError: invalid syntax
>>> run test
SyntaxError: invalid syntax
>>> test
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    test
NameError: name 'test' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> test.py
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    test.py
NameError: name 'test' is not defined
>>> python test.py
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> test.py
