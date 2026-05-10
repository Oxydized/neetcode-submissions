class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # im given an array of integers and a Target integer
        # i must return the indices of two numbers that = Target 
        # i can assume that every input has one correct pair
        # return the answer with the smaller index first

        # Brute force:  I can check each number against another
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # Because the previous answer used nested loops it's time complexity is O(n^2)
        # We can reduce this time down to O(n) by using a hashmap to store seen numbers

        # intialize hashmap
        seen_num = {}

        for i, num in enumerate(nums):
            # we have two given values target and the value in index
            # we will create a value to find the missing one
            needed_num = target - num
            if needed_num in seen_num:
                return [seen_num[needed_num], i]
            seen_num[num] = i
