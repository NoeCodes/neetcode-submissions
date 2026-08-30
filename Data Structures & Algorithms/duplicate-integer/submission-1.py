class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_counter = {}
        total_dupes = 0

        for i in range(len(nums)):
            freq = freq_counter.get(nums[i])

            if (freq is None):
                freq_counter[nums[i]] = 1
                continue
            else:
                freq_counter[nums[i]] += 1

        for i in freq_counter:
            if (freq_counter[i] > 1):
                return True
        
        return False