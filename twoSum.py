""" 
Given an array of integers 'nums' and an integer 'target'.

You may assuma that each input would have *exactly one solution*,
and you may not use the same element twice.

You can return the answer in any order.
"""
"""
 Gelistirme icin targetin hangi degerler araliginda olduguna bakip len(nums)'i
ona gore degistirebiliriz(bu sadece sirali dizilerde mi gecerli?). veya
   

"""

def findFibonacci(number):
    fibonacciNumbers = [0, 1]
    for i in range(2, number):
        x = fibonacciNumbers[i - 1] + fibonacciNumbers[i - 2]
        fibonacciNumbers.insert(i, x)
    return fibonacciNumbers


# print(findFibonacci(12))

# let 'nums' to be fibonacci numbers without first 2 elements


def twoSum(self, nums, target):
    # First 12 numbers of fibonacci
    x = findFibonacci(12)

    #  Removed first 2 element bcz of that 'exactly one solution' part,
    # otherwise there would be '0' and two '1', this would lead to unwanted
    # results.

    for i in range(0, 2):
        x.remove(i)
    nums = x  # [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    self = []

    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                self.append(i)
                self.append(j)
                break
    self.sort(reverse=True)
    print(self)


twoSum([], [], 36)
