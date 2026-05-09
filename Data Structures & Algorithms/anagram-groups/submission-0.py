class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # Group all anagrams together 
    # Return the output in any order
    # Compare between inputs

    # Brute Force
    # for every word:
    #   compare against every other word
    #       using anagram logic
        
        # Store final grouped result
        results = []

        # Track words that have already been grouped
        used = set()

        # Itterate through each word
        for word in strs:
            
            # Skip words already grouped
            if word in used:
                continue

            # Create a new group for current word    
            group = []
            
            # Compare current word against every other word
            for other_word in strs:
                if sorted(word) == sorted(other_word):
                    group.append(other_word)
                    used.add(other_word)
            
            # Add completed group to result
            results.append(group)

        return results