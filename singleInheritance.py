class father:

    asset = 10
    b= 2

    def add(self, a, b):
        return a+b
    
class child(father):

    def sub (self, a, b):
        return self.asset-b
    
suriya = child()

s= suriya.add(100, 200)
p= suriya.sub(500, 1000)

print(s)
print(p)

    
    
