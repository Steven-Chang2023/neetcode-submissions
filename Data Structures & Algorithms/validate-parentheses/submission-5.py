class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        left = set(['{', '[' , '('])

        for c in s:
            if c in left:
                stack.append(c)
            else:
                if c == '}' and (not stack or stack.pop() != '{'):
                    return False
                elif c == ')' and (not stack or stack.pop() != '('):
                    return False
                elif c == ']' and (not stack or stack.pop() != '['):
                    return False


                
        if stack:
            return False


        return True
