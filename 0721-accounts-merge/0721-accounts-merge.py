class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
                email_to_name[email] = name 
        
        res = []
        visited = set()

        def dfs(email):
            stack = [email]
            component = []
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in visited:
                            stack.append(nei)
            return component
        
        for email in graph:
            if email not in visited:
                component = dfs(email)
                res.append([email_to_name[email]] + sorted(component))
        return res
        

        
        