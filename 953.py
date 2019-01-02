class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        dp = [1] * len(A[0])
        for i in range(1, len(A[0])):
            for j in range(i):
                flag = True
                for k in range(len(A)):
                    if A[k][j] > A[k][i]:
                        flag = False
                        break
                if flag:
                    dp[i] = max(dp[i], dp[j]+1)
        res = max(dp)
        return len(A[0])-res

s = Solution().minDeletionSize(['fedcba'])
print(s)

