class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        node_map = collections.defaultdict(list)
        for i, j in edges:
            node_map[i].append(j)
            node_map[j].append(i)
        memo = set()
        def addComp(i):
            if i in memo: return 
            memo.add(i)
            for nei in node_map[i]:
                addComp(nei)
                
        count = 0
        for i in range(n):
            if i not in memo:
                addComp(i)
                count += 1
        return count
