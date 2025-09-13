class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower():
            return True
        elif word.isupper():
            return True
        else:
            for i in word:
                if i.isupper():
                    return word[1:].islower()

        # shortcut
        # return word.isupper() or word.islower() or word.istitle()