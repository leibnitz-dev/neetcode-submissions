class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pes = []
        count_zeros = 0
        for v in nums:
            if v == 0:
                count_zeros += 1
        
        if count_zeros == 0:
            product = 1
            for v in nums:
                product *= v
            for v in nums:
                pes.append(int(product/v))
        elif count_zeros == 1:
            for i, v in enumerate(nums):
                if v != 0:
                    pes.append(0)
                else:
                    arr = nums[:i] + nums[i+1:]
                    prod = 1
                    for v in arr:
                        prod *= v
                    pes.append(prod)
        else:
            pes = [ 0 for _ in nums]
        
        return pes 

        
        

        