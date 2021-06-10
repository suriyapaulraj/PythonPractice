import sys

class sample:
    def add(self, a, b):
        return a+b

obj = sample()

a= int(sys.argv[1])
b= int(sys.argv[2])

z=obj.add(a, b)

print(z)