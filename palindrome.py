'''Given an integer x, return true if x is a palindrome, and false otherwise.'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        if y[0] == '-':
            return False
        else:
            return y == y[::-1]
        
sol = Solution()
print(sol.isPalindrome(-121))