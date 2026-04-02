from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        need=Counter(s1)
        window=Counter()
        matches=0
        for i in range(len(s2)):
            char=s2[i]
            window[char]+=1

            if char in need and window[char] == need[char]:
                matches+=1
            
            if i>=len(s1):
                leftchar=s2[i-len(s1)]
                if leftchar in need and window[leftchar] == need[leftchar]:
                    matches-=1
                window[leftchar]-=1
                if window[leftchar]==0:
                    del window[leftchar]
            
            if matches==len(need):
                return True
        return False
        