
__author__: str = "730241536"
str_x: str = input("Input left-hand side number variable ")
str_y: str = input("Input right-hand side number variable ")
x: int = int(str_x)
y: int = int(str_y)
exp: int = (x**y)
div: float = (x/y)
floor_div: int = (x//y)
mod: int = (x%y)
result_y: str = str(y)
result_x: str = str(x)
exponent: str = str(x**y)
divi: str = str(x/y)
modu: str = str(x%y)
floor_divi: str = str(x//y)
print("Left-hand side: " + str_x)
print("Right-hand side: " + str_y)
print(str_x + " ** " + str_y + " is " + exponent)
print(str_x + " / " + str_y + " is " + divi)
print(str_x + " // " + str_y + " is " + floor_divi)
print(str_x + " % " + str_y + " is " + modu)