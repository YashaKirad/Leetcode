class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map=defaultdict(list)
        for word in strs:
            sorteds=''.join(sorted(word))
            ana_map[sorteds].append(word)
        return list(ana_map.values())
        