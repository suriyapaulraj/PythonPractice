class GFather:

    asset=10
    b=15

    def add(self, a, b):
        return a+b
    
class Father(GFather):

    def sub(self, a, b):
        return self.asset- b

class Child(Father):

    def mul(self, a, b):
        return self.b-b


suriya= Child()

x= suriya.add(30, 30)
y= suriya.sub(50,50)
z= suriya.mul(2, 2)

print (x)
print (y)
print (z)