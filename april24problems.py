class sample:
    a= 90
    b= 86

    def add(self, a, b):
        return a+ self.b

    def sub(self, b, c):
        return self.b- c

obj= sample()
k= obj.add(34, 54)
obj.a=90
obj.b=86
j= obj.sub(45, 30)

print(k)
print(j)