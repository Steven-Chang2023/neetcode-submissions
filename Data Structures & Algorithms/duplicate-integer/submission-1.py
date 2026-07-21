class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = set()
        for el in nums:
            if el in hm:
                return True
            hm.add(el)
        return False