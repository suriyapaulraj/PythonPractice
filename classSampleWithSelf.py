class Sample: 
    a=10
    b=5

    def add (self, a, b):
        return self.a+b
    def sub (self, a, b):
        return self.a-b
        
  


s= Sample()

d=s.add(5,100)
c=s.sub(10,100)

print(d)
print(c)
print(s.a)
print(s.b)