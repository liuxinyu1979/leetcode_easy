""""
This is the two sum problem
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. 

eg: input [2, 7, 11, 15], target=9, return [0,1]
input [3, 2, 4], target=6, return [1,2]
input [3, 3], target=6, return [0,1]
if doesnt exist, return [-1,-1]
"""

"""
time complexity: O(n^2) quadratic time
space complexity: o(1), no extra space required
nested loop
"""
def twosum_quadratic(input_ary, target):
    ans=[-1,-1]
    ary_len=len(input_ary)
    for x in range(0,ary_len):
        for y in range(x+1,ary_len):
            if input_ary[x]+input_ary[y] == target:
                print("found")
                ans=[x,y]
                return ans
    print("not found")
    return ans

"""
time complexity: O(n) linear time
space complexity: O(n) linear space
"""
def twosum_linear(input_ary, target):
    # for [2, 7, 11, 7, 15]
    # lookup should look like {2: set(0), 7:set(1, 3), 11:set(2), 15: set(4) }
    ans=[-1,-1]
    lookup={}
    pos=0
    for v in input_ary:
        if v in lookup:
            lookup[v].add(pos)
        else:
            lookup[v]={pos}
        pos += 1
    pos=0
    for v in input_ary:
        remain=target-v
        if remain in lookup:
            if remain==v:
                lookup[remain].remove(pos)
                # because remain+v=target, and remain==v, then we need to remove the v's pos in set and look up again
                if remain in lookup and len(lookup[remain])>0:
                    ans = [pos,list(lookup[remain])[0]]
                    return ans
            else: 
                ans = [pos,list(lookup[remain])[0]]
                return ans
        pos+=1
    return ans
    


def tests_quad():
    print(f"test_1_quad result is: {twosum_quadratic([2, 7, 11, 15], 9)}")    
    print(f"test_2_quad result is: {twosum_quadratic([3,2,4], 6)}")
    print(f"test_3_quad result is: {twosum_quadratic([3,3], 6)}")
    print(f"test_4_quad result is: {twosum_quadratic([3,3], 5)}")

def tests_linear():
    print(f"test_1_linear result is: {twosum_linear([2, 7, 11, 15], 9)}")    
    print(f"test_2_linear result is: {twosum_linear([3,2,4], 6)}")
    print(f"test_3_linear result is: {twosum_linear([3,3], 6)}")
    print(f"test_4_linear result is: {twosum_linear([3,3], 5)}")


if __name__ == "__main__":
    tests_quad()
    tests_linear()
    