class Sample():
    def fun1(self,name):
        print("welcome",name)
    def fun2(self,age):
        print("function-1",age)
    def __init__(self):
        print("Welcome to default function")
s1=Sample()
s1.fun1("azar")
s1.fun2(23)
