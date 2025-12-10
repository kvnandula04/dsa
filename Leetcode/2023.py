from collections import Counter

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        combinations = 0
        map_count = Counter(nums)
            
        for num in nums:
            if target.startswith(num):
                # Remaining is complement
                complement = target[len(num):]

                combinations += map_count[complement]

                if num == complement:
                    combinations -= 1                

        return combinations