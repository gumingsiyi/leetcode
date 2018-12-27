class Solution:
    ans=[]
    def dfs(self, s, r, l, n):
        if l > n:
            return
        if l < r:
            return
        if r == l and l == n:
            self.ans.append(s)
            # print(s)
            return
        self.dfs(s+'(', r, l+1, n)
        self.dfs(s+')', r+1, l, n)
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans.clear()
        self.dfs('',0,0,n)
        return self.ans

s = Solution()
res = s.generateParenthesis(3)
print(res)