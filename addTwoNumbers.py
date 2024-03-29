"""
 You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

 You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""


def addTwoNumbers(l1, l2):
    # Equalizing length of lists:

    length1 = len(l1)
    length2 = len(l2)

    if length1 != length2:
        diffDigit = abs(length1 - length2)
        if length1 > length2:
            for i in range(0, diffDigit):
                l2.insert(0, 0)
        else:
            for i in range(0, diffDigit):
                l1.insert(0, 0)

    index = length1 - 1
    print(l1)
    print(l2)
    self = []
    
    for i in range(0, index + 1):
        self.append(0)       
    
    while True:
        self[index] = l1[index] + l2[index]
        if self[index] > 9:
            self[index] = self[index] % 10
            l1[index - 1] += 1            
        index -= 1
        if index == 0 and self[index] > 9:
            self.insert(0,1)
            self[index] = self[index] % 10
#elde var 1 ilk satırda olunca, sonucun başına bir hane daha eklemesi gerekiyor.
#tersten yazma eklenecek(ya da ona göre düzenlenecek)
        if index == -1:
            break

    print(self)


addTwoNumbers([2, 3, 5, 1], [8 , 9, 9, 9])
