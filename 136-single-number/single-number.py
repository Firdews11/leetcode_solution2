class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0 
        for i in nums:
            n^=i 
        return n
        # the sign ^ is bitt=wise XOR perform bits of 2 integer
