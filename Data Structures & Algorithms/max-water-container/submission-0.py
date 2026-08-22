class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        store = 0
        while l < r:
            cur_store = min(heights[l], heights[r]) * (r-l)
            store = max(cur_store, store)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return store