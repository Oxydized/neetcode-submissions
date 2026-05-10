class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # im given 2 strings "s" and "t" 
        # i have to determine if they are anagrams or each other
        # if they anagrams return True

        # cleaned_s = ""
        # cleaned_t = ""

        # # for char in string s if a part of the string is a number or letter 
        # # create a new string to house it
        # for char in s.lower():
        #     if char.isalnum():
        #         cleaned_s += char
        # for char in t.lower():
        #     if char.isalnum():
        #         cleaned_t += char

        # return sorted(cleaned_s) == sorted(cleaned_t)

        # previous solution was O(n log n) better solution would be to hash map in order to reach 
        # O(n) by checking the letters from both strings against values seen in hashmap

        count = {}

        # Cleaning string for edge cases
        cleaned_s = []
        cleaned_t = []

        for char in s.lower():
            if char.isalnum():
                cleaned_s.append(char)
        cleaned_s = "".join(cleaned_s)

        for char in t.lower():
            if char.isalnum():
                cleaned_t.append(char)
        cleaned_t = "".join(cleaned_t)

        # return False for cases where cleaned strings do not equal length 

        if len(cleaned_s) != len(cleaned_t):
            return False

        for char in cleaned_s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for char in cleaned_t:
            if char not in count or count[char] == 0:
                return False
            else: 
                count[char] -= 1

        return True


