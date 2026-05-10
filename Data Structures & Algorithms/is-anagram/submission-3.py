class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Im given 2 strings (s) and (t)
        # I have to compare the two strings 
        # to determine if they are anagrams (contain the same letter counts)
        # Output should be True if they are anagrams and False if not

        # The easiest solution to this problem would be to use the sort function in python
        # There could be edge cases where capitals and punctuation would interfere with the sort

        # in this case there are no capitals or punctuation, however it's still good to prepare

        # .isalnum() can clean the punctuation and spaces and .lower() can address case sensitivity
        # .isalnum() can't modify the string so I will need to create a variable to hold the new string 

        # absolute bare bones sort if there are no edge cases
        # return sorted(s) == sorted(t)

        # if there are edge cases, how would I handle the sort
        
        # # initialize empty strings
        # cleaned_s = "" 
        # cleaned_t = ""

        # # for character in sorted string s
        # for char in s.lower():
        #     if char.isalnum():
        #         cleaned_s += char
        # for char in t.lower():
        #     if char.isalnum():
        #         cleaned_t += char
        # return sorted(cleaned_s) == sorted(cleaned_t)

        # The previous solution would be at O(n log n) due to the sorting
        # A better solution would be to keep a dictionary via hashmap

        # initialize dictionary as count
        count = {}

        # for loop
        if len(s) != len(t):
            return False

        for letter in s:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
        for letter in t: 
            if letter not in count or count[letter] == 0:
                return False
            else:
                count[letter] -= 1                        
        return True
