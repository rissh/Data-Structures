
class Solution:
    def numOfSubsequences(self, s: str) -> int:
        
        n = len(s)
        prefix_L = [0] * (n + 1)
        for i in range(n):
            prefix_L[i + 1] = prefix_L[i] + (1 if s[i] == 'L' else 0)

        suffix_T = [0] * (n + 1)
        for i in reversed(range(n)):
            suffix_T[i] = suffix_T[i + 1] + (1 if s[i] == 'T' else 0)

        original_subseqs = 0
        for j in range(n):
            if s[j] == 'C':
                original_subseqs += prefix_L[j] * suffix_T[j + 1]

        suffix_C_contrib = [0] * (n + 1)
        for i in reversed(range(n)):
            suffix_C_contrib[i] = suffix_C_contrib[i + 1]
            if s[i] == 'C':
                suffix_C_contrib[i] += suffix_T[i + 1]
        max_L_gain = max(suffix_C_contrib)

        prefix_C_contrib = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_C_contrib[i] = prefix_C_contrib[i - 1]
            if s[i - 1] == 'C':
                prefix_C_contrib[i] += prefix_L[i - 1]
        max_T_gain = max(prefix_C_contrib)

        max_C_gain = 0
        for i in range(n + 1):
            gain = prefix_L[i] * suffix_T[i]
            if gain > max_C_gain:
                max_C_gain = gain

        best_insertion_gain = max(0, max_L_gain, max_T_gain, max_C_gain)
        return original_subseqs + best_insertion_gain
        
