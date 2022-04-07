Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Variables in python?
a = 10
a
10
name = "Badra"
a + B
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a + B
NameError: name 'B' is not defined
a + b
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a + b
NameError: name 'b' is not defined
b = 20
a
10
b
20
a + b
30
c = a + b
c
30
d a- b
SyntaxError: invalid syntax
d = a - b
d
-10
abc-sss = 30
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
age
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    age
NameError: name 'age' is not defined
age = 30
age
30
salary
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    salary
NameError: name 'salary' is not defined
salary = 300000
salary
300000




salary1 = 30000
salary2 = 3000000
total = salary1 + salary2
total
3030000
names = ['badra', 'ravi']
names
['badra', 'ravi']
Names
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    Names
NameError: name 'Names' is not defined. Did you mean: 'names'?
Names = ['a', 'b;-']
Names
['a', 'b;-']
# When will we get name error?
# generally name will get when try to access undedined variables
# undefined variables



# single variable defination
a = 10
b = 10
c = 10

# multiple assignment
a = b = c = 10
a
10
b
10
c
10



a = 10
# stack  a = xyz            heap memory : 10 --> xyz

a
10
b = 20
# stack : b = abc ,            heap memory: 20 -> abc
b
20
# 1) python will store objects in heap memory and reference in stack memory
# python will look for variable names in stack memory and with help of reference , value will be fetched from heap memory



a = 10
a = 20
a
20
a = 10    # xyz -> 10
a = 20
a = 20  # abc > 20
a
20
# how memory clean up happend in python?
# python uses reference count alogorithm
# when ever if any object reference count is zero, python GC collected objects and remove from memeory
