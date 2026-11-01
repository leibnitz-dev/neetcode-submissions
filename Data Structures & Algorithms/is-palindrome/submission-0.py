class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_considered = ""

        for ch in s:
            if ch.isalnum():
                s_considered += ch
        
        s_considered = s_considered.lower()
        print(s_considered)
        
        i = 0 
        j = len(s_considered) - 1

        while i <= j:
            if s_considered[i] != s_considered[j]:
                return False
            i += 1; j -= 1
        
        return True

        