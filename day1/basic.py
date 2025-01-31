#python basics
print("Hello world");
#variables
age = 24
name = "sruthi"
salary = 15000.50
'''print(age)
print(name)
print(salary)'''
#print(name, age, salary)
#print("name:{} age:{} salary:{}".format(name, age, salary))
print("su","sruthi",sep="-",end="\n")
print("hi", sep='-')
#datatypes
# 1.Numeric datatypes
x = 1000000
print(type(x)) #int
y = 10.0
print(type(y))
z = 3 + 4j
print(type(z))

w = 1000000
print(x is w)

a = 100
b = 100
print(a is b)  # Output: True (they share the same memory reference)

a = 1000
b = 1000
print(a == b)
print(a is b)  # Output: False (they are different objects)

#count of keywords
import keyword
print(len(keyword.kwlist))












