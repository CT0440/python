var1 = 100
var2 = 65.9
var3 = "codetantra pvt ltd"
_var4 = 123
var5 = 123.6 
print(var1, var2, var3, _var4, var5, sep="    ", end="\n")

#local, Global, NoLocal variables
Global_var = "this is global variable"
def my_function():
    global Global_var 
    Global_var = "Global modified"
    local_var = "this is local variable"
    print("Inside my_function:",local_var)
    print("Inside my_function:",Global_var)
print("Outside my_function:",Global_var)
# print("Outside my_function:",local_variable)

def outerfunction():
    nonlocal_var = "This is nonlocal variable"
    print("Inside outer function: ",nonlocal_var)
    def innerfunction():
        nonlocal nonlocal_var
        nonlocal_var = "nonlocal variable modified inside innerfunction"
        local_var2 = "this local variable2"
        print("Inside inner function: ",local_var2)
        print("Inside inner function: ",nonlocal_var)
    innerfunction()
outerfunction()
my_function() 

print("Out side of the program : ", Global_var)


#class variable and Instance variable
class Myclass:
    class_varaible = "this is class varaible"
    print(class_varaible)
    def __init__(self, value):
        self.Instancevar = value #instance variable

obj1 = Myclass("This is Instance varaible")
print(obj1.Instancevar)

#special variables
print("Special variables are: Magic(dunder):__init__,__name__,__str__ & contsant variables: PI")
#Environamental variables
print("Environmental variables are system specific: os")


    