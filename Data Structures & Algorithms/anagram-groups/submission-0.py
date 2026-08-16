from collections import defaultdict 

class Solution:
    def groupAnagrams(self,strs):
        l1 = defaultdict(list)
        for S in strs:
            S1 = ''.join(sorted(S))
            l1[S1].append(S)
        return list(l1.values())
l = Solution()
print(l.groupAnagrams(["act","pots","tops","cat","stop","hat"]))