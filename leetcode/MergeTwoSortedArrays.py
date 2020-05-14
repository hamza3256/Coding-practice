class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == len(nums2):
            if nums2[0] >= nums1[-1]:
                return (nums2[0]+nums1[-1])/2
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        lN = len(nums1)
        if lN % 2 == 0:
            return(nums1[lN//2]+nums1[(lN//2)-1])/2
        else:
            return nums1[lN//2]