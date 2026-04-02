from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        maxfreq=max(freq.values())
        maxCount=sum(1 for c in freq.values() if c == maxfreq)
        return max(len(tasks),(maxfreq-1)*(n+1)+maxCount)
        