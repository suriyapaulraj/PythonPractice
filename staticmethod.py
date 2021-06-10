class sample:
    a = 10
    b = 15
  
    @staticmethod
    def add(a, b):
        return sample.a + b
  
    @staticmethod
    def sub(b, c):
        return sample.b -c
    
s= sample.add(14, 15)
p= sample.sub(16, 12)

print(s)
print(p)
