class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # create a graph that show [email] : id
        email_id_graph = defaultdict(list)
        visited_account = set()
        res = []
        
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                email_id_graph[email].append(i)
        
        
        def dfs(i, emails):
            if i in visited_account:
                return
            visited_account.add(i)
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neigh in email_id_graph[email]:
                    dfs(neigh, emails)
        
        
        
        for i, account in enumerate(accounts):
            if i in visited_account:
                continue
            name = account[0]
            emails = set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
            
        return res
            
        
        