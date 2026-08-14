class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '-', '*', '/'])
        for guy in tokens:
            if guy in ops:
                right = int(stack.pop())
                left = int(stack.pop())
                if guy == '+':
                    stack.append(left + right)
                elif guy == '-':
                    stack.append(left - right)
                elif guy == '*':
                    stack.append(left * right)
                else:
                    stack.append(left / right)
            else:
                stack.append(guy)
        
        return int(stack[0])
            