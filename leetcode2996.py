class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Find the sum of the longest sequential prefix
        firstnum = nums[0]
        total = nums[0]

        for i in nums[1:]:
            if i != firstnum + 1:
                break
            total += i
            firstnum = i

        # Step 2: Find the smallest missing integer >= total
        nums_set = set(nums)           # O(n) lookup
        x = total
        while x in nums_set:           # keep increasing until we find a missing one
            x += 1
        return x
