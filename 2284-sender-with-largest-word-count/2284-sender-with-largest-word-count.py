class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        
        wordCounts = defaultdict(int)
        for i in range(len(senders)):
            wordCounts[senders[i]] += len(messages[i].split())
        
        return max(wordCounts , key = lambda x : (wordCounts[x] , x))