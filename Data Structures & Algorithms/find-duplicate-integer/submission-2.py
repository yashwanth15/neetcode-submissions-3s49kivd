class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1) Find meeting point inside the cycle
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # 2) Find the entrance to the cycle (duplicate)
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow     