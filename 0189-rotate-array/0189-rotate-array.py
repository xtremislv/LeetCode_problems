class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            s = nums[-1]
            nums.pop()
            nums.insert(0,s)
            k -= 1

        