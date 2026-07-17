class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1 = nums.copy()

        nums1.sort()

        l = 0
        r = len(nums) -1

        n1 = -1

        n2 = -2
        while(l < r):
            if nums1[l] + nums1[r] < target:
                l += 1
            elif nums1[l] + nums1[r] > target:
                r -= 1
            else:
                n1 = nums1[l]
                n2 = nums1[r]
                break
        
        i1 = -1
        i2 = -1
        
        for i in range(len(nums)):
            if nums[i] == n1 and i1 < 0:
                i1 = i
            elif nums[i] == n2:
                i2 = i
        
        return [min(i1, i2), max(i1,i2)]