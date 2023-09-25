
class Solution:
    def minCostConnectPoints(self, points):
        graph, unionSet, result, ans = [], [], [], 0

        def findRoot(des):
            if unionSet[des][0] != des:
                unionSet[des][0] = findRoot(unionSet[des][0])
            return unionSet[des][0]

        def toUnion(x, y):
            xRoot, yRoot = findRoot(x), findRoot(y)
            if unionSet[xRoot][1] >= unionSet[yRoot][1]:
                unionSet[yRoot][0] = xRoot
                unionSet[xRoot][1] += unionSet[yRoot][1] + 1
            else:
                unionSet[xRoot][0] = yRoot
                unionSet[yRoot][1] += unionSet[xRoot][1] + 1

        def f():
            pointAmount, edgeAmount, resultIndex, nextEdge = len(points), len(graph), 0, 0
            while resultIndex < pointAmount - 1 and nextEdge < edgeAmount:
                currentEdge = graph[nextEdge]
                nextEdge += 1
                xRoot, yRoot = findRoot(currentEdge[0]), findRoot(currentEdge[1]) 
                if xRoot != yRoot:
                    result.append(currentEdge)
                    resultIndex += 1
                    toUnion(xRoot, yRoot)

        for i in range(len(points)):
            unionSet.append([i, 0]) # root, weight
            for j in range(i + 1, len(points)):
                graph.append([i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])])
        graph = sorted(graph, key = lambda e : e[2])
        f()

        for i in range(len(result)): ans += result[i][2]
        return ans
      
