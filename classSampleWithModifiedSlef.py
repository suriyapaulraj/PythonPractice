class Sample:
    a=10
    b=20

    def add (self, a, b):
        return a+self.a

    def sub (self, a, b):
        return self.add(a,b)-b
    
s= Sample()

s.a= 1
s.b= 2

k=s.add(3,6)
l=s.sub(10,20)

print(k)
print(l)


