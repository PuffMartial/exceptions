try:
    numerator = int(input("enter a number to divide: "))
    denominator = int(input("enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("you cant divide by zero! you Morron!!")
except ValueError as e:
    print(e)
    print("enter only numbers not words and symbols")
except Exception as e:
    print(e)
    print("somethings wrong :/")
else:
    print(result)