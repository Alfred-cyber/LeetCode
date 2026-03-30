'''
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums = [0,0,1,1,1,2,2,3,3,4]
        if not nums:
            return 0

        k = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k 
        
sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
