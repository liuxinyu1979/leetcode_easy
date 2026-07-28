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




if __name__ == "__main__":
    test_nums=[121, -121, 10, 1, 123321, 1234321, 1234]
    for v in test_nums:
        print (f"Input: {v}, the result is {is_palindrome_linear(v)}")
