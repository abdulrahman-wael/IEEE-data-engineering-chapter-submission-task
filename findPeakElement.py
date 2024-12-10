class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if mid < len(nums) -1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                right = mid - 1
            else:
                return mid
