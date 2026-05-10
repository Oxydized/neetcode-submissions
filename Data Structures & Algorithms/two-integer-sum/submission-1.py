class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # im given an array of integers and a Target integer
        # i must return the indices of two numbers that = Target 
        # i can assume that every input has one correct pair
        # return the answer with the smaller index first

        # Brute force:  I can check each number against another
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]