
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #n x max(length of strings)
        sortedAnagrams = [''.join(sorted(x)) for x in strs]
        grouped_map = {}
        for i in range(len(sortedAnagrams)):
            if(not grouped_map.get(sortedAnagrams[i])):
                grouped_map[sortedAnagrams[i]] = [strs[i]]
            else:
                grouped_map[sortedAnagrams[i]].append(strs[i]);
        
        return list(grouped_map.values())