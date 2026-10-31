class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt_mp = {}
        for v in nums:
            if str(v) not in cnt_mp:
                cnt_mp[str(v)] = 1
            else:
                cnt_mp[str(v)] += 1

        sorted_cnt_mp = dict(sorted(cnt_mp.items(), key=lambda item: item[1], reverse= True))
        return [int(v) for v in sorted_cnt_mp.keys()][:k]


        

        

        
        

        




        