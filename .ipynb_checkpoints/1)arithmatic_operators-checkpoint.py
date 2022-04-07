Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Arithmetic operators
# +, - , *, /, // %, **
# to perform some calculations on numbers
num1 = 20
num2 = 30
# qddition
num1 + num2 # 20 + 30
50
# sub
num1 - num2
-10
# mul
num1 * num2
600
# division
num1/num2
0.6666666666666666
# float
num2/num1
1.5
num1
20
num2
30
# floor division
num1//num2
0
num2/num1
1.5
num2//num1
1
# note: division returns float value
# but floor division returns int value
# power
num1 ** 2
400
num1 ** 3
8000
num1 ** 1
20
num1
20
# num1 is int
20.4 ** 2
416.15999999999997
20 ** 1.5
89.44271909999159
10 % 2
0
20 % 4
0
# write a program to calculate total price after discount
shirt_price = 500
dicount =  200
# toatal price
total = shirt_price - dicount
total
300
# write a program to find the price after 5% dicount
price = 500
dicount = 5
# write a program to find the share value for each person to pay bill
bill_amount = 50000
head_count = 4
contribution_per_head = bill_amount / head_count
contribution_per_head
12500.0
# write a program to find the amount required to 1000 shares of tatapower
current_price = 250
position_size = 1000
capital_required = current_price * position_size
capital_required
250000




# lets deal with strings
"Mr." + "Mahesh"
'Mr.Mahesh'
# it is valid operation
"Mr." - "Mahesh"  # it is an invalid( we can't substract two strings)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    "Mr." - "Mahesh"  # it is an invalid( we can't substract two strings)
TypeError: unsupported operand type(s) for -: 'str' and 'str'
# mul
"MR." * 3  # it is valid statement
'MR.MR.MR.'
"Mr." * 5
'Mr.Mr.Mr.Mr.Mr.'
# list
[1,2,4] + [4, 5, 6]
[1, 2, 4, 4, 5, 6]
# it is a valid
[1,2,3] - [2,3,4]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    [1,2,3] - [2,3,4]
TypeError: unsupported operand type(s) for -: 'list' and 'list'
[1,2 ] * 2
[1, 2, 1, 2]
[1,2 ] * 3
[1, 2, 1, 2, 1, 2]
# tuple
(1,2,34) + (2,3,4,4)
(1, 2, 34, 2, 3, 4, 4)
(1,2) - (3, 5)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    (1,2) - (3, 5)
TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
# dict
{"name": "Suman"} + {'age': 20}
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    {"name": "Suman"} + {'age': 20}
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
