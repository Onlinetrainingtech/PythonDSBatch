#Local and Global variables
a=10#Global variable
def func():
    a=12#Local variable
    print("Inside the function the value of:",a)
    
func()
print("Outside function the value of a is acting as global",a)
