class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combine = list(zip(position, speed))
        combine.sort(key=lambda x: x[0])

        stack = []

        for pos, sped in combine:

            time_end = (target - pos)/sped
            while stack:
                top = stack[-1]
                if time_end >= top:
                    stack.pop()
                else:
                    break
            stack.append(time_end)

        return len(stack)
           
            
