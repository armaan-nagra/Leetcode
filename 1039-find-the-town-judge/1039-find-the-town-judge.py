class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inboundNodes = defaultdict(list)
        outboundNodes = defaultdict(list)
        for a, b in trust:
            inboundNodes[b].append(a)
            outboundNodes[a].append(b)        

        for person in range(1, n+1):
            if len(inboundNodes[person]) == n - 1 and len(outboundNodes[person]) == 0:
                return person
        
        return -1
        
        
        #go over each item in the hash map and find any nodes which have length of n - 1?

        
        
                

