class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Take two integers in an array and return the two
        # Return indicies that equal the target integer
        # Assume every input has one pair of indicies
        # Return the lowest numbered indicies that equal target
        
        # nums[i] + nums [j] == target and i != j
    
        # Brute Force
        #for i in range(len(nums)):
         #   for j in range(i + 1, len(nums)):
          #      if nums[i] + nums[j] == target:
           #         return [i,j]

        # Complex
        # Create a dictionary to store values and compare

        val = {}
        for i, num in enumerate(nums):
            complement = target - num
                
            if complement in val:
                return [val[complement], i]

            val[num] = i
        
