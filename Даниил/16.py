class MathMethod:
    def __init__(self, n1, n2, n3, n4):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
    def max_nums(self):
        return max([self.n1,self.n2,self.n3,self.n4])
    def min_nums(self):
        return min([self.n1,self.n2,self.n3,self.n4])
    def average(self):
        return sum([self.n1,self.n2,self.n3,self.n4])

nums = MathMethod(1,2,3,4)
print(nums.max_nums())
print(nums.min_nums())
print(nums.average())