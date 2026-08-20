class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack:
                i, top = stack[-1]
                if temp <= top:
                    break
                stack.pop()
                result[i] = index - i
            stack.append((index, temp))

        return result