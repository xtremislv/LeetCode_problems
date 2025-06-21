class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        freq_values = list(freq.values())
        max_freq = max(freq_values)
        min_deletions = float('inf')

        for target in range(1, max_freq + 1):
            deletions = 0
            for f in freq_values:
                if f < target:
                    deletions += f  # delete all
                elif f > target + k:
                    deletions += f - (target + k)  # reduce to (target + k)
            min_deletions = min(min_deletions, deletions)

        return min_deletions