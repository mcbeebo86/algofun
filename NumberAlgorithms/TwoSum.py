# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target,
# where index1 must be less than index2.

class TwoSum:

    def __init__(self, array, target):
        self.array = array
        self.target = target

    def solve(self):
        if not self.array or len(self.array) < 2: return

        remainders = {}
        for i in range(len(self.array)):
            diff = self.target - self.array[i]
            if diff in remainders:
                print ("Index1 = " + str(remainders[diff]))
                print ("Index2 = " + str(i))
                return
            else:
                remainders[self.array[i]] = i