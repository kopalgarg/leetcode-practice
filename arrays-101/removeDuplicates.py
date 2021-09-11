class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = 1
        i = 1
        while i > 0 and i < len(nums):
            print(nums[:i])
            if nums[i] in nums[:i]:
                nums.pop(i)
                nums.append('_')
                i+=1
            else:
                unique+=1
                i+=1
