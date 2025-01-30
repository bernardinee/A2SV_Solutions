class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        original = str(x)
        reversed_string = original[::-1]
        
        return original == reversed_string