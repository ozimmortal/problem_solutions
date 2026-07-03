class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr["*"] = True
        
    def search(self, word: str) -> bool:
        
        curr = self.trie
        def s(i, curr : dict):
            if i == len(word):
                return True  if curr.get("*") else False

            if word[i] == ".":
                for k in curr.keys():
                    if k != "*" and s(i + 1 , curr[k]):
                        return True
                return False
            elif word[i] not in curr:
                return False
        
            return s(i + 1 , curr[word[i]])

        return s(0, curr)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)