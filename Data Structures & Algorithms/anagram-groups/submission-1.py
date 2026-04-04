
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         #n x max(length of strings) x26
#         sortedAnagrams = [''.join(sorted(x)) for x in strs]
        
#         grouped_map = {}
#         for i in range(len(sortedAnagrams)):
#             if(not grouped_map.get(sortedAnagrams[i])):
#                 grouped_map[sortedAnagrams[i]] = [strs[i]]
#             else:
#                 grouped_map[sortedAnagrams[i]].append(strs[i]);
        
#         return list(grouped_map.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_map = defaultdict(list)

        for s in strs:
            chars_count = [0] * 26
            for c in s:
                chars_count[ord(c) - ord('a')] += 1
            grouped_map[tuple(chars_count)].append(s)
        return list(grouped_map.values());




