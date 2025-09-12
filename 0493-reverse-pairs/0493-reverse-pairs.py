class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums) 
        self.count = 0
        def mergesort(l, r):
            mid = (l + r) // 2
            if l == r:
                return [nums[l]]
            if l > r:
                return []
            
            left_arr = mergesort(l, mid)
            right_arr = mergesort(mid + 1, r)
            return merge(left_arr, right_arr)

        def merge(left_arr, right_arr):
            arr = []
            nleft = len(left_arr)
            nright = len(right_arr)
            left = 0
            right = 0
            while left < nleft and right < nright:
                if left_arr[left] > right_arr[right]:
                    arr.append(right_arr[right])
                    right += 1
                else:
                    arr.append(left_arr[left])
                    left += 1
            
            while left < nleft:
                arr.append(left_arr[left])
                left += 1
            
            while right < nright:
                arr.append(right_arr[right])
                right += 1

            left = right = 0
            
            while left < nleft and right < nright:
                if left_arr[left] > 2 * right_arr[right]:
                    self.count += nleft - left
                    right += 1
                else:
                    left += 1

            return arr
        
        mergesort(0, n - 1)

        return self.count