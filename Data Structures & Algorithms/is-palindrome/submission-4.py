class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        #The question asks for confirming if palindrome or not
        #If palindrome return true, else return false
        #This sounds like a two pointer problem where 
        #One pointer will be on the left and the other on the right
        #iterating through each side until they meet the middle

        #Brute Force
        #I can clean the string and reverse it 

        #cleaned = s.lower().replace(" ","").replace("?","")
        #if cleaned == cleaned[::-1]:
        #    return True
        #return False

        # Complex solution uses two pointers 
        s = s.lower().replace(" ","").replace("?","").replace(",","").replace("'","").replace(".","").replace(":","")
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True