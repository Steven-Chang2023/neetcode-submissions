class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        qu = [1] * len(edges)
        for i in range(1, len(edges)):
            qu[i] = i + 1
        
        def find(q):
            
            if qu[q - 1] == q:
                return q
            
            output = q

            while qu[output - 1] != output:
                output = qu[output - 1]
            
            return output
            

        def qunion(q, p):
            idq = find(q)
            idp = find(p)
            qu[idp - 1] = idq 


        for edge in edges:
            if find(edge[0]) == find(edge[1]):
                return edge
            else:
                qunion(edge[0], edge[1])
                print(qu)