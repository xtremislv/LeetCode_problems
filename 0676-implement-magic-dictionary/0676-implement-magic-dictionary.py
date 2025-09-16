class MagicDictionary:

    def __init__(self):
        self.dictionary = []
        

    def buildDict(self, dictionary: List[str]) -> None:
        self.dictionary = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.dictionary:
            if len(searchWord) == len(word) and searchWord != word:
                i = count = 0
                while i < len(word):
                    if searchWord[i] != word[i]:
                        count += 1
                    if count > 1:
                        break
                    i += 1
                if count == 1:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)