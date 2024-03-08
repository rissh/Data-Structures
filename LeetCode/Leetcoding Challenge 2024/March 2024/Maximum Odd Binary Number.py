
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        n = len(s)
        count = 0 # Ones
        for bit in s:
            if bit == '1':
                count += 1

        res = (count - 1) * "1" + (n - count) * "0" + "1"
        return res

        '''
        hashMap = {}
        n = len(s)
        
        for char in s:
            if char in hashMap:
                hashMap[char] += 1
            else:
                hashMap[char] = 1

        res = ""
        for i in range(n - 1):
            if hashMap.get('1', 0) > 1:
                res += '1'
                hashMap['1'] -= 1
            elif hashMap.get('0', 0) >= 1:
                res += '0'
                hashMap['0'] -= 1

        res += '1'
        return res
        '''
      
