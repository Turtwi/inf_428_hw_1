class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        LCIS = 0
        current_LCIS = 0
        current_number = 0

        for num in nums:
            if current_number < num:
                current_LCIS+=1
            else:
                LCIS = max(LCIS, current_LCIS)
                current_LCIS = 1
            current_number = num

        LCIS = max(LCIS, current_LCIS)
        return LCIS