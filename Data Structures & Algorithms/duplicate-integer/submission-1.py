class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Provide answer in bool
        # Solving for if a duplicate is found within a LIST
        # True if value shows up more than once in LIST
        # False if value doesn't show up again
        
        # Brute Force:
        #for i in range(len(nums)):
        #    for j in range(i + 1, len(nums)):
        #        if nums[i] == nums[j]:
        #           return True
        #return False

        # Complex Solution
        # Create a set[]
        # Itterate through the set to find duplicates

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False