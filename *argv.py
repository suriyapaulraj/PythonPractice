class sample:
    def add(self, *suriya):
        sum=0
        for i in suriya:
            sum= sum+ i
        return sum    

obj = sample()

z=obj.add(2, 2, 2, 2, 2)

print(z)