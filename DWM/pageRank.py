import networkx as nx
import pylab as plt

D=nx.DiGraph()

D.add_weighted_edges_from([('A','B',1),('A','C',1),('C','A',1),('B','C',1)])

print (nx.pagerank(D))

nx.draw(D, with_labels=True)
plt.show()