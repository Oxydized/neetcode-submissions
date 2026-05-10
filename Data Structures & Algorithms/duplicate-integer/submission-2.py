class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # give an integer ARRAY 
        # check if any value appears more than once
        # if value appears more than once return True
        # else return False

        # Brute force solution would likely involve a nested for loop
        # checking all numbers against one another
        
        # For the index of the range of the list of numbers
        # for i in range(len(nums)):
        #     # For the index of one greater position than i in list of numbers
        #     for j in range(i + 1, len(nums)):
        #         # checks if numbers are = if they are then a duplicate was foound
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Since the previous solution provided gave O(n^2) I believe I can use set() to 
        # check if a number has been seen then check against the set 
        
        # initialize set
        seen_num = set()

        # 
        for num in nums:
            if num in seen_num:
                return True
            seen_num.add(num)
        return False

