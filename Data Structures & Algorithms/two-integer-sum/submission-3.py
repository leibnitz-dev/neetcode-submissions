class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, v in enumerate(nums):
            complement = target - v
            if complement in seen and seen[complement] != i:
                return [seen[complement], i]
            seen[v] = i

        
        