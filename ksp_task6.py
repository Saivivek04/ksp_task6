# Print Statement.
print("Hello World")

# Comments in Python Denoted by "#".

# Variables should not be Keywords.
# Variable name must start with a letter.
# Variable name cannot start with a number.
# Variable contain only Alpha-Numeric and Underscore.
# Variables are Case-Sensitive.
s1 = "Here s1 is a variable"
var_1 = "var1 is also a Variable"
_val = "_val is also variable"
print(s1)
print(var_1)
print(_val)

# DataTypes in Python: Integer,String,Boolean.
number = 10 # Integer Datatype Example.
st1 = "Hello" # String Datatype Example.String are declared inside the Double Quotes.
# boolean Datatype gives output as either "True" or "False"
print(number)
print(st1)

#Conditional Statements: if, if-elif-else , if-else.
#Example Program of Conditional Statements.
val_1 = 10
val_2 = 20
if val_1 > val_2:
    print("Val_1 is Greater than Val_2")
elif val_1 == val_2:
    print("Both are Equal")
else:
    print("Val_2 is Greater than Val_1")

# Operators:Arthimetic Operators, Assignment Operators, Logical Operators, Comparison Operators.
# Example Program for Arthimetic Operators.
num1 = 20
num2 = 7
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 ** num2)
print(num1 // num2)

# Example Program for Assignment Operators.
a = 2
b = 3
a+=b
print(a)
a-=b
print(a)
a/=b
print(a)
a%=b
print(a)
a//=b
print(a)
a**=b
print(a)

# Example Program for Logical Operators.
var1 = True
var2 = False
print(var1 and var2)
print(var1 or var2)
print(not var1)
print(not var2)

# Example Program for Comparison Operators.
var1 = 10
var2 = 13
print(var1 > var2)
print(var1 < var2)
print(var1 == var2)
print(var1 != var2)
print(var1 >= var2)
print(var1 <= var2)

# While Loop.
i = 10
while i >= 0:
    print(i)
    i = i-2

# For Loop.
for i in range(10,20,2):
    print(i)

# Functions.
def add(n1,n2): # Parameters.
    print(n1 + n2)
add(4,19) # Arguments.

def sub(n_1,n_2): # Parametrs.
    print(n_1 - n_2)
sub(19,4) # Arguments.

n1 = 4
n2 = 19
def add(): 
    print(n1 + n2)
add() 