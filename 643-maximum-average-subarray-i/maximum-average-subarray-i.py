class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ava = sum(nums[:k])
        max_ava = sum_ava / k 
        for i in range(k,len(nums)):
            sum_ava += nums[i] - nums[i-k]
            ava = sum_ava/k
            max_ava = max(max_ava,ava)
            
        return max_ava