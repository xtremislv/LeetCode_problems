class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        latest_subsequences = [""]
        count_subsequences = {"":1}
        temp_list = [""]
        for c in t:
            temp_list.append(c)
            count_subsequences["".join(temp_list)]=0
        for c in s:
            for i in range(len(latest_subsequences)-1,-1,-1):
                cur_subsequence = latest_subsequences[i]+c
                if cur_subsequence in count_subsequences:
                    count_subsequences[cur_subsequence]+=count_subsequences[latest_subsequences[i]]
            if latest_subsequences[-1]+c in count_subsequences:
                latest_subsequences.append(latest_subsequences[-1]+c)
        return count_subsequences[t]