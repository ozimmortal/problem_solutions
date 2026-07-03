class Trie:
    def __init__(self):
        self.trie = {}
        self.end_string = "*"

    def insert(self, word: str) -> None:
        curr = self.trie
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr[self.end_string] = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def valid(x , y):
            return 0 <= x < m and  0 <= y < n
        
        def dfs(x , y , node):

            if "*" in node:
                res.append(node["*"])
                del node["*"]
            
            
            directions = [(0 , 1) , (1 ,0) , (0 , -1) , (-1 , 0)]
            for dx , dy in directions:
                nx , ny = x + dx , y + dy
                if valid(nx , ny) and (nx, ny) not in seen and board[nx][ny]  in node:
                    seen.add((nx , ny))
                    dfs(nx , ny , node[board[nx][ny]])
                    seen.remove((nx, ny))
                    
        store = Trie()
        for word in words:
            store.insert(word)
        print(store.trie)
        res = []
        m , n = len(board) , len(board[0])
        for x in range(m):
            for y in range(n):
                curr = store.trie
                ch = board[x][y]
                if ch in curr:
                    seen = {(x , y)}
                    dfs(x , y , curr[ch])

        return res
