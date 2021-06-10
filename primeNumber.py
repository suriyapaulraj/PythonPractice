x=input("enter the number that you want to check if prime or not: ")
y= (int(x))

def prime(y):
    
    for i in range (2, y):
        if y % i == 0:
            print("the given number is not prime")
            break

    else:
        print("the given number is prime")

prime(y)
