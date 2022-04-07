Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# how to define identifiers?
# rules to follow while defining identifiers
# user defined name to the python object
# lets define variable to store int values
# int --> 10, 30, 40
# float --> 10.5, 44.5
# complex -> 1 +4j

qty = 30
price = 15.5
# lets find the total price
total_price = qty * price
total_price
465.0
# python provining a function to find data type of given value
type(10)
<class 'int'>
type(11.3)
<class 'float'>
type(2 + 4j)
<class 'complex'>
# note: python is dynamic type lanaguage, that means type will decide at runtime
# we no need to specify the data type at the time creating variables


# c, c++ int age = 20
\
age = 30
# int
type(age)
<class 'int'>
age = "30"
type(age)
<class 'str'>
age
'30'
age = 22.4
age
22.4
type(age)
<class 'float'>
age = "sldaklsmdlamldmlsd"
type(age)
<class 'str'>
# what do you mean by dynamic programming language?
# python is a dynamic p lanaaguge, because we no need to difine data type while creating/defining a variables. Type will decide at runtime based value assigennt

# lets do some calculations
a = 10
b = 20
# sum operations on int datatype
a + b
30
a - b
-10
b - 1
19
b - a
10
# 20 - 10
# 10
# multi
a * b
200
a ** b
100000000000000000000
2 ** 2
4
2 ** 3
8
10 ** 2
100
10  * 2
20
# int + int
10 + 20
30
10 + 22.3
32.3
10 + 2 + 4j
(12+4j)
# int + str
name = "hhshsh"
age = 30
name + age
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    name + age
TypeError: can only concatenate str (not "int") to str
# int + str
# lets deal with string data
# alpahabets
# how do we define string in python?
# we can create stringe in python 3 ways
#1) by using single quote ('hello')
#2) by using double quites ("Hello")
#3) by using thriple quites  ("""Hello""")
company_name = "Sumna IT"
type(company_name)
<class 'str'>
location = "nilgiri block, near ameerpet metro"
location
'nilgiri block, near ameerpet metro'
print(location)
nilgiri block, near ameerpet metro
fee = 2000.40
class_time = "9:30"
company_name
'Sumna IT'
location
'nilgiri block, near ameerpet metro'
fee
2000.4
class_time
'9:30'
type(fee)
<class 'float'>
type(companay_name)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    type(companay_name)
NameError: name 'companay_name' is not defined. Did you mean: 'company_name'?
type(company_name)
<class 'str'>
type(class_time)
<class 'str'>
# lets deal +
"Suman" + "IT"
'SumanIT'
"Suman" + "" + "IT"
'SumanIT'
"Suman" + "--->" + "IT"
'Suman--->IT'
"Suman" + "Mounica" + "IT"
'SumanMounicaIT'
"Suman" + "--> "+ "Mounica" + ""+ "IT"
'Suman--> MounicaIT'
"Suman" + "--> "+ "Mounica" + "-->"+ "IT"
'Suman--> Mounica-->IT'
'sumanit' + 20  # str + int (Inavlid)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    'sumanit' + 20  # str + int (Inavlid)
TypeError: can only concatenate str (not "int") to str
'Sumanit' + 33.30 # str + float (Invalid)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    'Sumanit' + 33.30 # str + float (Invalid)
TypeError: can only concatenate str (not "float") to str
# deal with *
'sumanIT' * 2 # str * int (valid)
'sumanITsumanIT'
'sumanIT' * 10 # str * int (valid)
'sumanITsumanITsumanITsumanITsumanITsumanITsumanITsumanITsumanITsumanIT'
# lets deal with -
"Suman" - "IT"
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    "Suman" - "IT"
TypeError: unsupported operand type(s) for -: 'str' and 'str'
# str - ingt
"SumanIT" - 20
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    "SumanIT" - 20
TypeError: unsupported operand type(s) for -: 'str' and 'int'
"ananan" + 22.22
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    "ananan" + 22.22
TypeError: can only concatenate str (not "float") to str
"ananan" + "22.22"
'ananan22.22'
# lets deal with bool values
True
True
False
False
isManager = True
if isManager:
    print("He is a manager")

He is a manager
isManager = False
if isManager:
    print("He is a manager")

10 > 30
False
if 10 > 30:
    print("HHSHSH")

if 10 < 30:
    print("HHSHSH")

HHSHSH
# int
# str
# float
# True or False
# lets deal with list
fruit_name = 20
fruit_name = "banana"
fruits = ['banana', 'orange', 'graphs']
fruits
['banana', 'orange', 'graphs']
type(fruits)
<class 'list'>
# list stores data in index postion
fruits[0]
'banana'
fruits[1]
'orange'
fruits[2]
'graphs'
fruits[0:2]
['banana', 'orange']


