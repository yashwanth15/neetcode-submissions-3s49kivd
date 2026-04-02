class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap=defaultdict(list)
        for word in strs:
            hashWord="".join(sorted(word))
            anagramMap[hashWord].append(word)
        return list(anagramMap.values())
        