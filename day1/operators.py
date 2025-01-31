#operators
#1. Arithmatic operators
print("1. Arthematic operators..")
num1 = 12
num2 = 5
print("num1 :", num1,"num2 :", num2)
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("FllorDivision:", num1 // num2)
print("Modulus:", num1 % num2)

#2. Comparison(relational) operators
print("relational operators...")
val1 = 10
val2 = 20.5
print("val1 :", num1,"val2 :", num2)
print(val1 > val2) #false
print(val1 < val2)#true
print(val1 >= val2)#false
print(val1 <= val2)#true
print(val1 == val2)#false
print(val1 != val2)#true

#3. Assignment operators
print("Assignment operators...")
num1 = 10
num2 = 15
print("num1 :", num1,"num2 :", num2) #10 15
num1 = num2
print("num1 :", num1,"num2 :", num2)#15 15
num1 += num2
print("num1 :", num1,"num2 :", num2)#30 15
num1 -= num2
print("num1 :", num1,"num2 :", num2)#15 15
num1 *= num2
print("num1 :", num1,"num2 :", num2)#225 15
num1 /= num2
print("num1 :", num1,"num2 :", num2)#15 15

#Bitwise operators
print("Bitwise operators...")
num1 = 5
num2 = 3
print("num1 :", num1,"num2 :", num2)
print(num1 & num2)#1
print(num1 | num2)#7
print(num1 ^ num2)#6
print(~num1)#-6

#ternary operator is not there in python
(5 > 3)if "5 greater than 3" else "5 is not greater than 3"

#identity operators
list1 = [10,20,30,40]
x = 50
print(x in list1) #false
print(x not in list1) #true
    
#membersip operators
num1 = 10
num2 = 10.0

#logical operators
print("Logical operators")
print((10 > 0) and (15 % 2 == 1)) #true
print((10 < 0) and (15 % 2 == 1)) #false

print(False or True) #True

print(not(1))

print(num1 is num2)#false
print(num1 is not num2)#false


#presidence and Assosiativity
expr = 2 + 3 * 2 - 5
print(expr)#3

#assosiativity
expr2 = (2 + 3 * 4 -8 / 4) #left to right-12.0
print(expr2)



















