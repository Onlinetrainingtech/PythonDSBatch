try:
    num=int(input("Enter the number"))
    re=100/num
except  ZeroDivisionError as e:#exception argument
    print("Something is wrong",type(e))
else:
    print("Result is:",re)
finally:
    print("Finally programs ends")
