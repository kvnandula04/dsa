import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot = random.randint(l, r)  # choose a random pivot
            partition_index = l  # the index to divide the numbers < pivot and > pivot

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[partition_index], nums[i] = (
                        nums[i],
                        nums[partition_index],
                    )  # swap the current element with the element at partition_index - update the partition_index
                    partition_index += 1

            nums[partition_index], nums[r] = (
                nums[r],
                nums[partition_index],
            )  # swap the current pivot with the element at partition_index (which is the first element > pivot value)

            if partition_index < k:
                return quickSelect(partition_index + 1, r)  # search the right side
            elif partition_index > k:
                return quickSelect(l, partition_index - 1)  # search the left side
            else:
                return nums[partition_index]

        return quickSelect(0, len(nums) - 1)


sol = Solution()
print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
