class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(list(set(nums)))

        longest_seq_length = 1
        cnt = 1

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i+1] == sorted_nums[i] +1:
                cnt += 1
            else:
                cnt = 1
            

            if cnt > longest_seq_length:
                longest_seq_length = cnt
        return longest_seq_length




        


