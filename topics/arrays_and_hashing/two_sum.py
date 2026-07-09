"""
    
    Problem Link: https://neetcode.io/problems/two-integer-sum/question
    Difficulty: Easy
    Category: Arrays and Hashing
    
    Approach: Track the already seen elements using a hash map. For every element in the list, find the complement wrt the target and check if 
    it is in the hash map. If yes, return both indices. If not, store the number and its index in the hashmap
    
    Time Complexity: O(N) - Single pass through the list.
    Space Complexity: O(N) - Storing up to N elements in the hash table.  
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        already_seen = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in already_seen:
                return [already_seen[diff], i]
            already_seen[num] = i