def divide1():
    try:
         num=int(input("Enter the number"))
         c=45/num
         print(c)
    except ValueError:
        print("This is value error")
    except ZeroDivisionError:
        print("Do not use zeros")
    finally:
        print("This is finally block")
divide1()
