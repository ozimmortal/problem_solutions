class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

def build_trie(words):
    root = TrieNode()
    for word in words:
        curr = root
        for i , c in enumerate(word):
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
    return root

def search(st , node  , path):
    res = []
    if node.end:
        res.append(st + "".join(path))

    for ch in node.children.keys():
        path.append(ch)
        res.extend(search(st ,node.children[ch] , path))
        path.pop()
    
    return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        trie = build_trie(products)
        res =[]
        curr = trie
        for i , ch in enumerate(searchWord):
            if ch not in curr.children:
                while len(res) < len(searchWord):
                    res.append([])
                break
            suggestion = search(searchWord[:i + 1] ,curr.children[ch] , [])
            res.append(sorted(suggestion)[:3])
            curr = curr.children[ch]
        
        return res
            

        