class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        
        right = 0
        
        while right < len(nums):
            if target - nums[right] in hash_map:
                return [hash_map[target - nums[right]], right]
            else:
                hash_map[nums[right]] = right
                right += 1