Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# it is a user defined name to the python objects
# variable, function, class, module
age = 20
# age is an identifier
# = is operator
# 20 is the value/object
age
20
salary =30000
# salary is identifier
# -
# 30000 is object
salary
30000
age
20
hdhdhhdd = 4
# rules to define variable name
for = 30
SyntaxError: invalid syntax
for1
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    for1
NameError: name 'for1' is not defined
for1 = 3
and = 20
SyntaxError: invalid syntax
class = 30
SyntaxError: invalid syntax
Class = 30
Class
30
# case sensitive
# rule #1 : we shouldn't use reserved keywords as indetifier name
help()

Welcome to Python 3.10's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.10/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> exit
Help on Quitter in module _sitebuiltins object:

exit = class Quitter(builtins.object)
 |  exit(name, eof)
 |  
 |  Methods defined here:
 |  
 |  __call__(self, code=None)
 |      Call self as a function.
 |  
 |  __init__(self, name, eof)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

help> \1
No Python documentation found for '\\1'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> \q
No Python documentation found for '\\q'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> exit()
No Python documentation found for 'exit()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> q

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.







# rule # 2 we can use upper, lower case amd 0-9, _
name = "Badra"
Name ="Badra"
NAME = "JSJJSJ"
firstName = "HH"
lastName = "JJJ"
name1 = "HHH"
name2 = "JJJJJJ"
n23b = 33
first_name = "Akhila"
last_name = "B"
33 = "A"
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
2name = "A"
SyntaxError: invalid decimal literal
name2 = "SSS"
_33 = 44
_33
44
name1 = "A"
n23abc = "A"

2abc = 10 # invalid
SyntaxError: invalid decimal literal
abc1 = 20
a_2_3_r = "B"
a - b - c = "C" # Invalid
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
class = "Python"
SyntaxError: invalid syntax
_class = "Python"
# we use _ to make it as private variables
jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj = 44
jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
44
age = 40
a = 30
# is there any limit on identifier name in python?
# there is no limit on length of the identifier in python
firsrName = "Mouni"
firstname = "Akila"
ab10c = 20
_ = 30
_
30
_abc = 30
for = 40
SyntaxError: invalid syntax
_for = 30
for1 = 40
f1or = 30
1for = 30
SyntaxError: invalid decimal literal
_anb = 30
_anc_ = 30
_anc_ = 30 # it is not best practice
__module__
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    __module__
NameError: name '__module__' is not defined
dir()
['Class', 'NAME', 'Name', '_', '_33', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '_abc', '_anb', '_anc_', '_class', '_for', 'a', 'a_2_3_r', 'ab10c', 'abc1', 'age', 'f1or', 'firsrName', 'firstName', 'first_name', 'firstname', 'for1', 'hdhdhhdd', 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj', 'lastName', 'last_name', 'n23abc', 'n23b', 'name', 'name1', 'name2', 'salary']
__package__ = 'dd'
__package__
'dd'
and_ = 30
_and = 3
_and_
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    _and_
NameError: name '_and_' is not defined. Did you mean: '_anc_'?
anc = "Honda amaze"
anc
'Honda amaze'
car_name = "Honda amaze"
salary = 3333
s -ddd
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    s -ddd
NameError: name 's' is not defined
s = 444
