"""Relational operators practice using booleans and strings."""
__author__: str = "730241536"
str_x: str = input("Input left-hand side number variable ")
str_y: str = input("Input right-hand side number variable ")
x: int = int(str_x)
y: int = int(str_y)
less_bool: bool = (x<y)
greater_than_or_equal: bool = (x>=y)
equals: bool = (x==y)
not_equals: bool = (x!=y)
result_y: str = str(y)
result_x: str = str(x)
lbool: str = str(x<y)
gbool: str = str(x>=y)
eq: str = str(x==y)
neq: str = str(x!=y)
print("Left-hand side: " + str_x)
print("Right-hand side: " + str_y)
print(str_x + " < " + str_y + " is " + lbool)
print(str_x + " >= " + str_y + " is " + gbool)
print(str_x + " == " + str_y + " is " + eq)
print(str_x + " != " + str_y + " is " + neq)