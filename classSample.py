class Sample: 
    a=10
    b=5

    def add (self, a, b):
        return a+b
    def sub (self, a, b):
        return a-b
    def mul (self, a, b):
        return a*b
    def div (self, a, b):
        return a/b        


S= Sample()

addition= S.add(10,5)
subtraction= S.sub(10,5)
multiplication= S.mul(10,5)
division= S.div(10,5)


print(addition)
print(subtraction)
print(multiplication)
print(division)