age=int(input("Enter the value is"))
if age>=60:
    salary=int(input("Enter the salary is"))
    if salary>=20000:
          bns=salary+500
          print("Your salary is",bns)
    else:
          bns=salary+1000
          print("Your salary is",bns)
else:
    print("Your age is less than 60")
    
