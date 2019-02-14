class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        jewel = set(J)
        cnt = 0
        for s in S:
            if s in jewel:
                cnt += 1
        return cnt