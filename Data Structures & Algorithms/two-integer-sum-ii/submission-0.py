class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        ini = 0
        fii = len(numbers) - 1
        while ini <fii:
            if numbers[ini] + numbers[fii] < target:
                ini += 1
            elif numbers[ini] + numbers[fii] > target:
                fii -= 1
            else:
                return [ini+1, fii+1]
        