class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = j = 0
        size = len(nums)
        while j < size:
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return i

test = [1, 2, 2, 2, 3, 4, 4, 5]
print(Solution().removeElement(test, 2))
print(test)