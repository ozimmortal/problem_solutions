class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def neighbour(node):
            neighbours = []
            for gene in "ACGT":
                for i in range(8):
                    mutated = node[:i] + gene + node[i + 1:]
                    neighbours.append(mutated)
            return neighbours
        
        queue = deque([(startGene , 0)])
        seen = {startGene}

        while queue:
            node ,s = queue.popleft()

            if node == endGene: return s
            for n in neighbour(node):
                if n not in seen and n in bank:
                    queue.append((n , s + 1))
                    seen.add(n)
        return -1