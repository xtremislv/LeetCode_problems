class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        # Count white blocks in the first window of size k
        white_count = sum(1 for i in range(k) if blocks[i] == 'W')
        min_recolors = white_count

        # Slide the window from start to end
        for i in range(k, n):
            # Remove the leftmost block of the previous window
            if blocks[i - k] == 'W':
                white_count -= 1
            # Add the new block at the right end of the current window
            if blocks[i] == 'W':
                white_count += 1
        
            min_recolors = min(min_recolors, white_count)

        return min_recolors