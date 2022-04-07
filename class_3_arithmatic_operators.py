Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 30
b = 20
# Addition
a + b
50
# Substraction
a - b
10
b - a
-10
# Mul
a * b
600
a * a
900
b * a
600
# Devision
a/b
1.5
b/a
0.6666666666666666
# / always return the float
10/2
5.0
# what is the output datatype of below example
20/5
4.0
# it is float

# floor division
20//5
4
0/5
0.0
5/0
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    5/0
ZeroDivisionError: division by zero
333/0
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    333/0
ZeroDivisionError: division by zero
0/3444
0.0
444/000
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    444/000
ZeroDivisionError: division by zero
# exp
2 ** 2
4
2 **3
8
2 * 3
6


# int operands
# trail and error with int and str
"ABC" + 2  # it is invalid
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    "ABC" + 2  # it is invalid
TypeError: can only concatenate str (not "int") to str
"ABC" + "d"
'ABCd'

# str + float
"your's"
"your's"
"you 'dddd' k"
"you 'dddd' k"
' "ddd", dddd'
' "ddd", dddd'


"B" + 33.5
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    "B" + 33.5
TypeError: can only concatenate str (not "float") to str
# *
"C" * 2
'CC'
"c" * 10
'cccccccccc'
"Badra" * 3
'BadraBadraBadra'
"3" * 2
'33'
d = 30
c = 30
c = "30"
c
'30'
# i want to convert it to int
# int()
int(c)
30
c
'30'
int('30') * 2 # 30 * 2 = 60
60
int("A123") + 3 # erro
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    int("A123") + 3 # erro
ValueError: invalid literal for int() with base 10: 'A123'
int("SDD")
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    int("SDD")
ValueError: invalid literal for int() with base 10: 'SDD'
int("4444")
4444
int("4444.55")
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    int("4444.55")
ValueError: invalid literal for int() with base 10: '4444.55'
float("4444.50")
4444.5



int("44") # out? data type int - 44
44
int("44.6") # error
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    int("44.6") # error
ValueError: invalid literal for int() with base 10: '44.6'
float("444.55")
444.55
float("44")
44.0




# lets deal str + str
"Abc" + "--->" + "xyz"
'Abc--->xyz'
"Abc" + " " + "--->" + " "+ "xyz"
'Abc ---> xyz'
"Abc" + "$" + "--->" + "$"+ "xyz"
'Abc$--->$xyz'


# list
data = [1,2,3]
data1 = [4, 5, 6]
# list + list
data + data1
[1, 2, 3, 4, 5, 6]
data - data1
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    data - data1
TypeError: unsupported operand type(s) for -: 'list' and 'list'

# mu
data * 2
[1, 2, 3, 1, 2, 3]
data 8 10
SyntaxError: invalid syntax
data * 10
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
"E" * 3
'EEE'


# deal with tuple
data = (1,2,3)
data2 = (3,5,6)
data + data2
(1, 2, 3, 3, 5, 6)
data
(1, 2, 3)
data2
(3, 5, 6)



(1,2,3) + [3,5,6]
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    (1,2,3) + [3,5,6]
TypeError: can only concatenate tuple (not "list") to tuple
{'a': 10} + {'b': 30}
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    {'a': 10} + {'b': 30}
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'



# dict + dict > invalid
# list + list > valid --> list
# tuple + tuple > valid --> tuple
# tuple + list > invalid
# str + int > invalid
# int + float > valid --> float
# str * int > valid --< str
