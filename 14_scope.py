class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        max_a=max(self.__elements)
        min_a=min(self.__elements)
        self.maximumDifference=abs(min_a-max_a)
       

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
