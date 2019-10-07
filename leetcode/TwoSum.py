class Solution(object):
    def twoSum(self, nums, target):
        found = {}
        for i, num in enumerate(nums):
            val = target - num
            if val not in found:
                found[num] = i
            else:
                return [found[val], i]
