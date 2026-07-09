"""
    
    Problem Link: https://neetcode.io/problems/is-anagram/question
    Difficulty: Easy
    Category: Arrays and Hashing
    
    Approach: 
    1) Sort both words in the alphabetical order. In case both of them are equal, the word is an anagram.
    Time Complexity: O(NlogN) - Sorting the words
    Space Complexity: O(N) - Storing the sorted words
    
    2) Maintain a helper list of length 26 representing the English alphabet, where each index represents a letter. Loop through the first
    word and increment the corresponding index. The index is calculated for any letter by subtracting the ASCII value of 'a' from the ASCII
    value of the letter itself. Loop through the second word and decrement the corresponding indices. If the helper list contains all zeros, 
    return True.
    Time Complexity: O(N + M) - Looping through both the words (N and M are equal)
    Space Complexity: O(1) - Storing the fixed helper list
"""


class Solution:
    def isAnagram_solution1(self, s: str, t: str) -> bool:
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        return True if sorted_s == sorted_t else False
    
    def isAnagram_solution2(self, s: str, t: str) -> bool:
        alphabet = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            alphabet[ord(s[i]) - ord("a")] += 1
        for i in range(len(t)):
            alphabet[ord(t[i]) - ord("a")] -= 1
        return all(x == 0 for x in alphabet)