'''
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121 (negative number is never a palindrome)
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
'''
import unittest

# both time and space complexity are O(n)
def is_palindrome_linear(input):
    # convert number to string
    # then process both ends inward
    if input < 0:
        return False
    
    num_str=str(input)
    if len(num_str)==1:
        return True
    mid=len(num_str)//2
    if input%2 == 1:
        mid += 1
    left=0 
    rit=len(num_str)-1
    for left in range(0,mid):
        if left >= rit:
            return True
        
        if num_str[left] != num_str[rit]:
            return False
        
        left += 1
        rit -=1
    return True

'''
n=1234
reverse_half: rh=0

if n > rh
n=1234/10 = 123
mod=1234%10=4
rh=rh*10+mod=0*10+4=4

if n>rh
n=123/10=12
mod=123%10=3
rh=rh*10+mod=4*10+3=43
if n>rh which is not (12 < 43)

n=12, rh43, they are not the same, return false

-------
n=123
rh=0
if n > rh
n=123/10=12
m=123%10=3
rh=0*10+3=3

if n>rh
n=12/10 = 1
m=12%10=2
rh=3*10+2=32

n=1, rh=32, not the same

----
n=121
rh=0
if n>rh
n=121/10 = 12
m=121%10=1
rh=0*10+1=1

if n>rh
n=12/10=1
m=12%10=2
rh=1*10+2=12
n=1, rh=12, because rh/10=12/10=1, its the same as n. 
This is because if a number has odd number of digits, then (if n>rh) expression will bring 
rh 10X greater than input variable n, that's why we compare both n == rh and r == rh/10

This algo is log10K because n is reduced by 1 digit at a time, but that digit represent a shrunk by 10
'''
def is_palindrome_lg_10_base_k(input):
    if input <0 or (input %10==0 and input !=0):
        return False
    
    reverse_half=0
    while input > reverse_half:
        mod_val=input%10
        input //= 10
        reverse_half=reverse_half*10+mod_val
        
    if input == reverse_half or input == reverse_half//10:
        return True
    return False

class TestPalindromeNumbers(unittest.TestCase):
    def test_log_algo(self):
        test_nums={0:True,121:True, -121:False, 100:False, 20:False, 10:False, 1:True, 123321:True, 1234321:True, 1234:False}
        for key,val in test_nums.items():
            self.assertEqual(is_palindrome_lg_10_base_k(key), val)

# coverage run -m unittest unittest_divide.py
# coverage report or coverage html followed by htmlcov/index.html
#unittest.main() 

# if __name__ == "__main__":
#     test_nums=[0,121, -121, 100, 20, 10, 1, 123321, 1234321, 1234]
#     for v in test_nums:
#         print (f"Test Linear Input: {v}, the result is {is_palindrome_linear(v)}")
        
#     for v in test_nums:
#         print (f"Test log10k Input: {v}, the result is {is_palindrome_lg_10_base_k(v)}")
        
#     # print(f"{is_palindrome_lg_10_base_k(101)}")
        
