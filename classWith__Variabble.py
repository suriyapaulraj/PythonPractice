class Sample:
    __a= 1
    __b= 2

    def add (a,b):
        return self.__a+self.__b
    
    def sub (a,b):
        return self.__a-a

s= Sample()

s.__a=10
s.__b=20

p=s.add(5,6)
q=s.sub(7,8)

print(p)
print(q)