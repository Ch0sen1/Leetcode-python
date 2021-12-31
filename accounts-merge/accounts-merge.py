class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited_account = set()
        emails_linked_account = defaultdict(list)
        res = []
        for i , account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                emails_linked_account[email].append(i)
                
        def dfs(i, emails):
            if i in visited_account:
                return
            visited_account.add(i)
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in emails_linked_account[email]:
                    dfs(neighbor, emails)
        
        
        for i , account in enumerate(accounts):
            if i in visited_account:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        
        return res
        
        