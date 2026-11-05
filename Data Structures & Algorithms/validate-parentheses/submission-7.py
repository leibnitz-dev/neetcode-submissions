class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        matching_brackets = {')':'(', '}':'{', ']':'['}

        for ch in s:
            if ch in '{[(':
                stack.append(ch)
            elif ch in '}])':
                if not stack or matching_brackets[ch] != stack[-1]:
                    return False 
                stack.pop()
        
        return len(stack) == 0

        
        
        

        