'''
Implementation of Watershed Cuts Algorithm from  

Jean Cousty, Gilles Bertrand, Laurent Najman, and Michel Couprie. 
Watershed Cuts: Minimum Spanning Forests and the Drop of Water Principle.
PAMI. 2009. (31:8), p. 1362-1374, http://dx.doi.org/10.1109/TPAMI.2008.173
'''

import networkx
import collections

def watershedCuts(G) :

    labels = collections.defaultdict(lambda : None)
    num_labels = 0

    def stream(head) :
        L = set([head])
        unexplored = set([head])
        while unexplored :
            y = unexplored.pop()
            F_y = min([nabe['weight'] for nabe in G[y].values()])
            potential_nabes = set([nabe for nabe, attributes in G[node].items() 
                                   if attributes['weight'] == F_y])

            for z in potential_nabes.difference(L) :
                if labels[z] is not None :
                    return L, labels[z]
                else :
                    L.add(z)
                    F_z = min([nabe['weight'] for nabe in G[z].values()])
                    if F_z < F_y :
                        unexplored = set([node])
                        break
                    else :
                        unexplored.add(node)
        return L, None
                
    for node in G.nodes() :
        if labels[node] is None :
            L, label = stream(node) 
        
            if label is None :
                num_labels += 1
                for node in L :
                    labels[node] = num_labels
            else :
                for node in L :
                    labels[node] = num_labels

    return labels

if __name__ == '__main__' :
 
    lines = ["1 2 3",
             "2 3 27",
             "3 4 3.0",
             "3 5 2.0"]
    G = networkx.parse_edgelist(lines, nodetype = int, data=(('weight',float),))

    print watershedCuts(G)
