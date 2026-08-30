class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_at_index = {}
        compliment = 0

        # Find compliment and verify if we have seen it before
        for i in range(len(nums)):
            compliment = target - nums[i]

            # If not, save it for the next run
            if (seen_at_index.get(compliment) is None):
                seen_at_index[nums[i]] = i
                continue
            else:
                return [seen_at_index[compliment], i]

        return []
