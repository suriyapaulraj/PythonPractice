class sample:
    a= 90
    b= 86

    @classmethod
    def add(cls, a, b):
        return a+ cls.b

    @classmethod
    def sub(cls, b, c):
        return cls.b- c


k= sample.add(34, 54)

j= sample.sub(45, 30)

print(k)
print(j)





               