from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        common_pairs = count.most_common(k)
        
        return [item[0] for item in common_pairs]
