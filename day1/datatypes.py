#datatypes
print("Numeric datatypes...")
print("1.int", end="\n")
print("2.float", end="\n")
print("3.complex", end="\n")
numeric1 = 12
numeric2 = 60.5
numeric3 = 9 + 3j
print(numeric1, numeric2, numeric3)

print("Boolean datatyes..")
boolean1 = True
boolean2 = False
print(type(boolean1))

print("sequence datatypes...")
print("1.list", end="\n")
print("2.String", end="\n")
print("3.Tuple", end="\n")
list1 = ["codetantra", 150.89, 3 + 6j, True]
string1 = "SVPCET College"
tuple1 = (1, 2, 3.5, "CT")
print(list1, string1, tuple1, end = "\n")

print("dictionary datatype..")
dict1 = {101: "susruthi", 102: "swapna", 103: "keerthi"}
keys = dict1.keys()
values = dict1.values()
print(keys)
print(values)

print("set datatype..")
set1 = {1, "hi", 3, "1", 3} #duplicants are not allowed
print(set1)

print("remaining datatypes: None, frozen set, bytes, bytearray, range etc")


print("Type conversion")
print("Implicit type conversion")
num1 = 2
num2 = 2.5
num3 = num1 + num2
print("Integer + float = float, num = ",num3)

print("Explicit type conversion")
num1 = 3
num2 = 4.5
num3 = (int)(num2)
print("int + converting to int = int, num3 = ",num3)

string1 = "123"
num1 = (int)(string1)
print(num1)
print(type(num1))






