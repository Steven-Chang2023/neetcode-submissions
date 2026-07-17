class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        no_way = 0
        for val in nums:
            no_way = no_way ^ val
        
        return no_way