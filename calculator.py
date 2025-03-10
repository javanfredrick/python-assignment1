import sys
def main():
  

    x= int(input("What is the value of x ?"))
    y= int(input("What is the value of y  ?"))
    sign=input("Enter the sign of the operation to be performed  ")
    if sign == "add":
        def add(x,y):
            z=x +y
        
            print("The sum of x and y is",add(x,y))
            add(x,y)
            return z
            sys.exit()
    elif sign == "subtract":
        def subtract(x,y):
         z=x-y
        
        print("The difference of x and y is",subtract(x,y))
        return z




    def subtract(x,y):
        z=x-y
        return z
    print("The difference of x and y is",subtract(x,y))



    def multiply(x,y):
        z=x*y
        return z
    print("The product of x and y is",multiply(x,y))

    def divide(x,y):
        z=x/y
        return z
    print("The division of x and y is",divide(x,y))










if __name__=="__main__":
    main()

