
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        hmap = defaultdict(list)
        for s in map(str.split, paths):
            for v, k in map(lambda x: x.split('('), s[1:]):
                hmap[k].append(f'{s[0]}/{v}')
        return filter(lambda x: len(x) > 1, hmap.values())
      
