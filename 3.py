class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        wmap={}
        window_size=0
        res=0
        for i in range(len(s)):
            if s[i] not in wmap:
                wmap[s[i]] = i
                window_size += 1
                print(s[i]+"+1")
                res = max(res, window_size)
            else:
                window_size = i-wmap[s[i]]
                d = []
                for c in wmap:
                    if wmap[c] < wmap[s[i]]:
                        d.append(c)
                for c in d:
                    wmap.pop(c)
                wmap[s[i]]=i
        return res
    
s = Solution().lengthOfLongestSubstring("tmmzuxt")
print(s)
            