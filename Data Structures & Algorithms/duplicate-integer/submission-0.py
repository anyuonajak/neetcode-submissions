from collections import Counter 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for key in count.keys():
            if count[key] >= 2:
                return True 

        return False 
        