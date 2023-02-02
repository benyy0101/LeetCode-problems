class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        target = collections.defaultdict(list)
        
        for item in strs:
            target[''.join(sorted(item))].append(item)
        
        return target.values()