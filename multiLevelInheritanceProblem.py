class factorial():

    n = 5
    fact = 1
    
    for i in range(1,n+1):
        fact = fact * i
        
    print (fact)

class fibonacci(factorial):

    nterms = n
   
    n1, n2 = 0, 1
    count = 0   

    if:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2        
            n1 = n2
            n2 = nth
            count += 1


class primeNumber(fibonacci):
        
    num = n   

    flag = False

    if num > 1:       
        for i in range(2, num):
            if (num % i) == 0:
               
                flag = True
                
                break

  
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")