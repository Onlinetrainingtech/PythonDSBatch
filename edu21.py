class B():
    def fun1(self):
        self.name=input("Enter the value is")
class D(B):
    def viewdetails(self):
        print("Your name is",self.name)
d1=D()
d1.fun1()
d1.viewdetails()
