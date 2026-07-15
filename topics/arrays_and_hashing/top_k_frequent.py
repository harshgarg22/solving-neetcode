"""
    Problem Link: https://neetcode.io/problems/top-k-elements-in-list/question
    Difficulty: Medium
    Category: Arrays and Hashing
    
    Approach: 
    First create a hashmap that keeps track of the frequencies in the list. Once we have that, we take an array of size equal to the length
    of the input array. The index in this case represents the count/frequency. The maximum frequency that a number can have is equal to the
    length of the list, i.e., when the same number occurs throughout. Now you put the numbers at the corresponding indices using the frequency. 
    Start from the end of this array and return the first 'k' elements. 

    Time Complexity: O(N) - Iterating over the input list of length 'N' and then iterating over the count array of length 'N' that we created
    Space Complexity: O(N) - Storing the newly created list
"""

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        #Calculate and store the frequency of each element
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            elif num in frequency:
                frequency[num] += 1

        count = [[] for i in range(len(nums) + 1)]

        #Add everything into the count array
        for num, freq in frequency.items():
            count[freq].append(num)
        
        #Start from the end of the array and add to the result array
        result = []
        for i in range(len(nums), 0, -1):
            for res_num in count[i]:
                result.append(res_num)
                if len(result) == k:
                    return result 