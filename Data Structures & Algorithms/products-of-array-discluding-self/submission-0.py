class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)

        n = len(nums) - 1
        for i in range(len(nums)):
            if i != 0:
                left[i] = nums[i] * left[i-1]
                right[n-i] = nums[n-i] * right[n - i + 1]
            else:
                left[i] = nums[i]
                right[n-i] = nums[n-i]

        output = [0] * len(nums)

        for i in range(len(nums)):
            if i != 0 and i != n:
                output[i] = left[i-1] * right[i + 1]
            elif i == 0:
                output[i] = right[i + 1]
            else:
                output[i] = left[i-1]

        return output
            
        

