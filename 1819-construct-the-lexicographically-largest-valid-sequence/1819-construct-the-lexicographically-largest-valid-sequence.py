class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def backtrack(index: int) -> bool:
            while index < len(res) and res[index] != 0:
                index += 1
            if index == len(res):
                return True  

            for num in range(n, 0, -1):  
                if used[num]:
                    continue
                if num == 1:
                    res[index] = 1
                    used[1] = True
                    if backtrack(index + 1):
                        return True
                    res[index] = 0
                    used[1] = False
                else:
                    j = index + num
                    if j < len(res) and res[index] == 0 and res[j] == 0:
                        res[index] = res[j] = num
                        used[num] = True
                        if backtrack(index + 1):
                            return True
                        res[index] = res[j] = 0
                        used[num] = False
            return False

        backtrack(0)
        return res