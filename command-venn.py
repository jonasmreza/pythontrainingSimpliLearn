Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
set={11,12,13,14,14,14,14}
set1
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    set1
NameError: name 'set1' is not defined. Did you mean: 'set'?
set
{11, 12, 13, 14}
a={5,6,7,8}
b={7,8,9,10}
a&b
{8, 7}
a|b
{5, 6, 7, 8, 9, 10}
a-b
{5, 6}
a+b
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
b-a
{9, 10}
a={4,5,6,4,4,4,4}
len(a)
3
data1{"aaafadf":75,"aasdfasd":80}
SyntaxError: invalid syntax
data1={"asdasdas"}