class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(' ')
        b = []
        for i in a:
            if i != "":
                b.append(i)
                # return a

        return ' '.join(b[::-1])
