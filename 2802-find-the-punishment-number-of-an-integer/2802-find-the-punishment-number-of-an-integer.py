class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(sq_str: str, target: int) -> bool:
            def dfs(index: int, current_sum: int) -> bool:
                if index == len(sq_str):
                    return current_sum == target
                for j in range(index + 1, len(sq_str) + 1):
                    num = int(sq_str[index:j])
                    if dfs(j, current_sum + num):
                        return True
                return False

            return dfs(0, 0)

        total = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if can_partition(square_str, i):
                total += i * i
        return total