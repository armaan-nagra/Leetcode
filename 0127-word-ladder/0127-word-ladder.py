class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        n = len(beginWord)

        buckets = defaultdict(list)
        for w in wordList:
            for i in range(n):
                buckets[w[:i] + "-" + w[i+1:]].append(w)
        
        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps
            
            for i in range(n):
                patWord = word[:i] + "-" + word[i+1:]
                for nei in buckets.get(patWord,[]):
                    if nei not in visited:
                        q.append((nei, steps + 1))
                        visited.add(nei)
            buckets[patWord] = []
        return 0