try:
    a=int(input("Enter 1st number:"))
    b=int(input("enter 2nd number:"))
    print(a/b)
except ZeroDivisionError as ze:
    print("DIVISION BY ZERO ERROR:",ze)
except ValueError as e:
    print("non integer value entered:",e)
