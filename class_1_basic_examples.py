Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# this is python interpreter
# define a variable
age = 30
age
30
a = 30
b = 40
# add
a + b
70
a - b
-10
a * b
1200
a/b
0.75
a//b
0
# create a variable to store float
price = 158.50
price
158.5
# find a type of price value
type(price)
<class 'float'>
age = 33
type(age)
<class 'int'>
# define a chars data
location = "Hyderabad"
type(location)
<class 'str'>
# define boolean value
# bool
# True or False
is_manager = True
if is_manager:
    print("Eligible for salary hike")

Eligible for salary hike
is_manager = False
if is_manager:
    print("Eligible for salary hike")

23 < 30
True
30 > 20
True
30 < 10
False
type(True)
<class 'bool'>
type(False)
<class 'bool'>
# every thing in python is an object
# int object
# float object
# bool object(True or False)
# string ("sjjsjsjs")
# do we need to specify data while creating variables in python?
# ans: python is dynamic type language, we no need to specify the data, because variable data type will decide at runtime
a = 20
2 = "Badra"
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a = "Badra"
a
'Badra'
# int, float, string bool
# how do we handle collection of values
friends = ['ram', 'mounika', 'akhila', 'jagan']
friends
['ram', 'mounika', 'akhila', 'jagan']
type(friends)
<class 'list'>
# get first name
friends[0]
'ram'
friends[1]
'mounika'
friends[2]
'akhila'
friends[3]
'jagan'
friends[4]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    friends[4]
IndexError: list index out of range
friends[5]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    friends[5]
IndexError: list index out of range
friends[3]
'jagan'
# list
# tuple
gender = ('Male', "Female")
gender = ('Male', "Female")
type(gender)
<class 'tuple'>
# tuple stores data in index position
gender[0]
'Male'
gender[1]
'Female'
gender[2]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    gender[2]
IndexError: tuple index out of range
# how do we display two values at once
gender
('Male', 'Female')
gender[0:1]
('Male',)
gender[0:2]
('Male', 'Female')
gender[0:3000]
('Male', 'Female')
# dict sir
# key value pair
college_details = {"college_name": "CBIT", "address": "Hyderabsd,djddjd"}
type(college_details)
<class 'dict'>
college_details
{'college_name': 'CBIT', 'address': 'Hyderabsd,djddjd'}
# print only college_name
college_details['college_name']
'CBIT'
college_details['address']
'Hyderabsd,djddjd'
# set
# set to remove duplicate elements
data = {1,2,3,4,4}
type(data)
<class 'set'>
data[0]
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    data[0]
TypeError: 'set' object is not subscriptable
data1 = {2, 3}
data
{1, 2, 3, 4}
data2
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    data2
NameError: name 'data2' is not defined. Did you mean: 'data'?
data1
{2, 3}
data & data1
{2, 3}
data | data1
{1, 2, 3, 4}
data.intersection(data1)
{2, 3}
out = list(data)
out
[1, 2, 3, 4]
out[1]
2
