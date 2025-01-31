#I/0 & formatting strings
#taking input from the user
num1 = int(input("Enter number1: "))
num2 = float(input("Enter number2: "))
res = (int)(num1 + num2)
#printing output
print(res)

#string formatting
print("String formating...")
print("1. concatenation")
name = input("name:")
age = input("age:")
print("hello my name is: " + name + " and my age is: " + age)

print("2.formating")
print("name : {} and age : {}".format(name, age))

print("3.fstrings")
print(f"my name is : {name} and my age is {age}")

name = "ramya"
age = 25
print("4. % - formatting(old version)")
print("name: %s and age is %d" %(name, age))

#controlling decimal places
PI = 3.1412
print("PI value : {:.2f}".format(PI))
#padding & Alignment
print("{:<10}".format("left"))
print("{:>10}".format("right"))




























