x = input("enter the term til which  you want to find finnonacci series: ")
y = int(x)



def fibbonacci(y):
    a=0
    b=1

    print(a)
    print(b)

    for i in range(2, y):
        c= a+b
        a=b
        b=c    
        print(c)




fibbonacci(y)
