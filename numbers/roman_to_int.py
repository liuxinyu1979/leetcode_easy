'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, 
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

'''

def roman_to_int(input_str):
    # if we encounter a letter, we can lookup the value and do add or subtract
    # add and subtract is based on whether or not the previous value is smaller
    # than current
    val_lookup= {'I':   1,'V':   5,'X':  10,'L':  50,'C': 100,'D': 500,'M':1000}
    
    # algo:
    # loop all letters:
    # if cur is the first letter, than look up the value and add to total
    # elif cur is > prev, then minus prev (because it was added to total, it's like pop from stack), 
    # and than add (cur-prev) eg: if prev is I and cur is V, prev was added to total, so we need to might I
    # and then V- I = 5-1 = 4
    idx=0
    total=0
    # we assume chars are in the above char set, so not validating
    for idx in range(0, len(input_str)):
        cur_val=val_lookup[input_str[idx]]
        if idx ==0:
            total += cur_val
        else:
            prev_val=val_lookup[input_str[idx-1]]
            if cur_val > prev_val:
                total= total-prev_val+cur_val-prev_val
            else:
                total += cur_val
    return total


if __name__ == "__main__":
    print(f"{roman_to_int('II')}")
    print(f"{roman_to_int('IV')}")
    print(f"{roman_to_int('VI')}")
    print(f"{roman_to_int('M')}") # 1000
    print(f"{roman_to_int('LVIII')}") #58
    print(f"{roman_to_int('MCMXCIV')}") # 1994