class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def neighbour(node):
            ans = []
            for a in "abcdefghijklmnopqrstuvwxyz":
                for i in range(len(node)):
                    new_word = node[:i] + a + node[i+1:]
                    ans.append(new_word)
            return ans

        seen = set(beginWord)
        queue = deque([(beginWord , 0)])
        wordList = set(wordList)
        while queue:
            node , s = queue.popleft()
            if node == endWord: return s + 1
            for n in neighbour(node):
                if n not in seen and n in wordList:
                    seen.add(n)
                    queue.append((n , s + 1))
        return 0
