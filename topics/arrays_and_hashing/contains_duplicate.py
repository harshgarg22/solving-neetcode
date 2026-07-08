"""
    
    Problem Link: https://neetcode.io/problems/duplicate-integer/question
    Difficulty: Easy
    Category: Arrays and Hashing
    
    Approach: Use a hash table (or a dict) to store the numbers of the list as keys. In case a key exists, i.e., a number is repeated, return True.
    
    Time Complexity: O(N) - Single pass through the array.
    Space Complexity: O(N) - Storing up to N elements in the hash table.  
"""

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_seen = {}
        for num in nums:
            if num in already_seen:
                already_seen[num] += 1
                return True
            else:
                already_seen[num] = 1
        return False
                    

if __name__ == "__main__":
    sol = Solution()
    
    try:
        assert sol.hasDuplicate([1,2,3,4]) == False
        assert sol.hasDuplicate([1,2,3,4,1]) == True
        print("All tests passed!")
    except AssertionError:
        print(f"Test case failed")