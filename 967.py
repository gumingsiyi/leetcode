class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        ans=set()
        stack=['0','1','2','3','4','5','6','7','8','9']
        while len(stack)!=0:
            cur = stack.pop()
            print(cur)
            if len(cur) == N:
                if cur[0] != '0' or N == 1:
                    ans.add(int(cur))
                continue
            
            num = int(cur[-1])
            if 0<=num-K<=9:
                stack.append(cur+str(num-K))
            if 0<=num+K<=9:
                stack.append(cur+str(num+K))
        return list(ans)

s = Solution().numsSameConsecDiff(2,0)
print(s)