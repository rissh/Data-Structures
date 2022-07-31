
class Solution:
    def check_elements(self, arr, n, A, B):
        unique_nums = set()
        for num in arr:
            if(num >= A and num <=B):
                unique_nums.add(num)
        return len(unique_nums) == B-A+1
      
