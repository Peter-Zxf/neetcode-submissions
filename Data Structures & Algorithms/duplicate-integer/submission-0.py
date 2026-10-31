class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n1 = len(nums)
        n2 = len(set(nums))
        return n1 != n2
