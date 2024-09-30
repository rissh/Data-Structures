
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, num):
        node = self.root
        for char in str(num):
            node = node.setdefault(char, {})
        node['#'] = True

    def f(self, num):
        node, res = self.root, 0
        
        for char in str(num):
            if char not in node:
                return res
            node, res = node[char], res + 1
            
        return res
    
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        trie, maxLen = Trie(), 0
        
        for num in arr1:
            trie.insert(num)
        for num in arr2:
            maxLen = max(maxLen, trie.f(num))
            
        return maxLen

