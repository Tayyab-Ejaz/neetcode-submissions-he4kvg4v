class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_1 = defaultdict(int)
        for c in s:
            hash_1[c] = hash_1.get(c, 0) + 1
        
        hash_2 = defaultdict(int)
        for c in t:
            hash_2[c] = hash_2.get(c, 0) + 1
        return hash_1 == hash_2