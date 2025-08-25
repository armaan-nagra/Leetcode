class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)

        g = []
        for _ in range(n):
            g.append([])
        
        for a, b in pairs:
            g[a].append(b)
            g[b].append(a)
        
        res = list(s)
        visited = [False] * n

        for i in range(n):
            if visited[i]:
                continue
            
            stack = [i]
            visited[i] = True
            comp = []

            while stack:
                u = stack.pop()
                comp.append(u)
                for v in g[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            
            comp.sort()
            chars = []
            for idx in comp:
                ch = res[idx]
                chars.append(ch)
            chars.sort()

            for k, idx in enumerate(comp):
                res[idx] = chars[k]
        
        return "".join(res)


            