class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        total_actual, min_initial = self.divide_and_conquer(tasks, 0, len(tasks) - 1)
        
        return min_initial

    def divide_and_conquer(self, tasks: list[list[int]], start: int, end: int) -> tuple[int, int]:
        if start == end:
            return tasks[start][0], tasks[start][1]
        
        mid = (start + end) // 2
        
        left_actual, left_min = self.divide_and_conquer(tasks, start, mid)
        right_actual, right_min = self.divide_and_conquer(tasks, mid + 1, end)
        
        merged_actual = left_actual + right_actual
        merged_min = max(left_min, right_min + left_actual)
        
        return merged_actual, merged_min