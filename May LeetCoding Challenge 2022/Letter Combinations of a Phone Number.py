
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}
        
        def combine(a, b: List[str]) -> List[str]:
            res = []
            for i in a:
                for j in b:
                    res.append(i + j)
            return res

        res = [x for x in letters[digits[0]]]
        for i in range(1, len(digits)):
            res = combine(res, [x for x in letters[digits[i]]])
        
        return res
      
