class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for v in strs:
            res += str(len(v)) + "#" + v
        print(res)
        return res 


    def decode(self, s: str) -> List[str]:
        words = []
        l = 0; r = 0
        while r <= len(s) - 1:
            if s[r] != '#':
                r += 1
            else:
                mv = int(s[l:r])
                word = s[r+1: r+mv+1]
                print(word)
                words.append(word)
                l = r =r+mv+1
        


        return words




    
    
    



