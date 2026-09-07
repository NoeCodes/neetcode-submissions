class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        1. Sort the array and make a set out of it
        2. For each number:
            a. Find what the next number should be
            b. Check the set if it contains the next number
                - If True: Increment the current streak
                - If False: Update the highest streak and restart the current streak
                - Handle Edge cases: One unique number and duplicates
        3. Return the highest streak
        """
        nums.sort()
        numSet = set(nums)
        highestSequenceStreak = 0
        currentSequenceStreak = 0
        print(nums)

        # Edge case: If nums only contains one unique integer
        if (len(numSet) == 1):
            highestSequenceStreak = 1
            return highestSequenceStreak

        previousNumberInArray = None   # Edge case: Disregard duplicates
        for i in range(len(nums)):
            if (i > 0):
                previousNumberInArray = nums[i - 1]

            if (previousNumberInArray == nums[i]):
                continue

            currentSequenceStreak += 1
            nextNumber = nums[i] + 1

            if (nextNumber in numSet):
                continue
            else:
                if (currentSequenceStreak > highestSequenceStreak):
                    highestSequenceStreak = currentSequenceStreak
                currentSequenceStreak = 0

        return highestSequenceStreak