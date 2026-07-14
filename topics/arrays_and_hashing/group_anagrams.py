"""
    
    Problem Link: https://neetcode.io/problems/anagram-groups/question
    Difficulty: Medium
    Category: Arrays and Hashing
    
    Approach: 
    1) Iterate through the list and sort each word in the list. The sorted word serves as the key for the hashmap. Anagrams will have the
    same hash key, hence they are appended to the list of that particular key in the hashmap. 
    Time Complexity: O(M*NlogN) - Sorting all the the 'M' words in the list with a time complexity of O(NlogN) for the sorting algorithm 
    Space Complexity: O(M) - Storing the hash map
    
    2) Maintain a helper list of length 26 representing the English alphabet, where each index represents a letter. This list will track
    the frequency of the characters. Iterate through the given input list. For each word, update the character frequency in the helper list.
    This helper list will not be the same for two words unless they are anagrams. Hence, this list serves as the key to the hash map. 
    Using this logic we will group all the anagrams together in the hash map. 

    Time Complexity: O(M*N) - Iterating over the input list of length 'M' where the average length each word in the list is 'N' characters.
    Space Complexity: O(M) - Storing the hash map
"""
from typing import List

class Solution:
    def groupAnagrams_solution1(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        if len(strs) == 1:
            return [strs]
        anagram_map = {}
        for word in strs:
            normalized_word = "".join(sorted(word))
            if normalized_word not in anagram_map:
                anagram_map[normalized_word] = [word]
            elif normalized_word in anagram_map:
                anagram_map[normalized_word].append(word)

        return [anagram_map[x] for x in anagram_map]
    
    def groupAnagrams_solution2(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        if len(strs) == 1:
            return [strs]

        anagram_map = {}
        for word in strs:
            character_array = [0]*26

            for character in word:
                character_array[ord(character) - ord('a')] += 1

            unique_id = tuple(character_array)
            if unique_id not in anagram_map:
                anagram_map[unique_id] = [word]
            elif unique_id in anagram_map:
                anagram_map[unique_id].append(word)
        
        return [anagram_map[x] for x in anagram_map]