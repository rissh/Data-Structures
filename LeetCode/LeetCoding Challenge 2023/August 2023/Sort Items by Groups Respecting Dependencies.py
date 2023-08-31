
from collections import defaultdict

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        g_ind = defaultdict(int)
        g_out = defaultdict(list)
        g_contain = defaultdict(list)
        ind = defaultdict(int)
        out = defaultdict(list)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
            g_contain[group[i]].append(i)
        for i in range(m):
            g_ind[i] = 0
        for i in range(n):
            if beforeItems[i]:
                for j in beforeItems[i]:
                    if group[i] != group[j]:
                        g_ind[group[i]] += 1
                        g_out[group[j]].append(group[i])
                    else:
                        ind[i] += 1
                        out[j].append(i)
       
        g_with_0_ind = []
        for i in range(m):
            if g_ind[i] == 0:
                g_with_0_ind.append(i)
        g_order = []
        while g_with_0_ind:
            curr = g_with_0_ind.pop()
            g_order.append(curr)
            for nxt in g_out[curr]:
                g_ind[nxt] -= 1
                if g_ind[nxt] == 0:
                    g_with_0_ind.append(nxt)
        if len(g_order) != m:
            return []
        
        ans = []
        
        for g in g_order:
            members = g_contain[g]
            node_with_0_ind = []
            for i in members:
                if ind[i] == 0:
                    node_with_0_ind.append(i)
            order = []
            while node_with_0_ind:
                curr = node_with_0_ind.pop()
                order.append(curr)
                for nxt in out[curr]:
                    ind[nxt] -= 1
                    if ind[nxt] == 0:
                        node_with_0_ind.append(nxt)
            if len(order) != len(members):
                return []
            ans += order

        return ans
      
