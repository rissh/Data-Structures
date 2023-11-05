class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        n = len(arr)
        nums = arr * 2
        count = 0
        current = 0

        for i in range(n):
            
            if arr[i] == arr[current]:
                continue
            if arr[i] < arr[current]:
                count += 1
            if arr[i] > arr[current]:
                count = 1
                current = i

            if count >= k:
                return arr[current]

        return max(arr)
