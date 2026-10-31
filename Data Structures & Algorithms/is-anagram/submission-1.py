class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def return_map(s: str):
            mapp = {}
            for v in s:
                if v not in mapp:
                    mapp[v] = 1
                else:
                    mapp[v] += 1
            return mapp
        
        return  return_map(s) == return_map(t)

        

        

            
            

        


        