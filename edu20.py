class Product():
    def addProduct(self):
        self.productid=int(input("Enter the Productid"))
        self.pname=input("Enter the value is")
    def viewDetails(self):
        print("Your ProductId is",self.productid)
        print("Your Pname is",self.pname)
s1=Product()
s1.addProduct()
s1.viewDetails()
