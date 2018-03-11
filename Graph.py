"""  
  Project : To build PageRank                  
  Course No : CS F469 Information Retrieval

  This is for Graph Visualisation.
  The graphs we want to visualise are as follows:

  1. Initial Graph when only original links are considered
  2. Updated Graph when teleportation is allowed
  3. Graph where bubble size is relative to their pageRank
  
"""
'''
    Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats.
'''
import matplotlib.pyplot as plt

'''
        NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
'''
import networkx as nx

'''
        Pickle package is used to save and load already saved data structures. It saves the pre processing time.
'''
import pickle

'''
        NumPy is the fundamental package for scientific computing with Python. It contains among other things: a powerful N-dimensional array object
'''
import numpy as np

# n is the total no of nodes
n=10878

#Matrix storing the final votes
with open("final.pickle","rb") as f:
    final_votes=pickle.load(f)

#Array storing the final page rank
with open("page_rank.pickle","rb") as f:
    pg_rank=pickle.load(f)

#Matrix to hold the original_votes
with open("original_votes.pickle","rb") as f:
    original_votes=pickle.load(f)

def submatrix( matrix, startRow, startCol, size):
    """
        To return the submatrix from the n*n matrix.
        We will draw the graph on the returned nodes
    """
    return matrix[startRow:startRow+size,startCol:startCol+size]

#To form Graph 1 (Graph with original links)

#Finding the submatrix
ori_submatrix = submatrix(original_votes,269,1043,10)

#Converting the submatrix to a Multi Di Graph using Networkx package
ori_MDGraph = nx.MultiDiGraph(ori_submatrix)

#Form a dot file in the current directory using Networkx package
nx.drawing.nx_pydot.write_dot(ori_MDGraph,'Initial.dot')




#To form Graph 2 (Graph after Teleportation)
fin_submatrix = submatrix(final_votes,269,1043,10)

#Converting the submatrix to a Multi Di Graph using Networkx package
fin_MDGraph = nx.MultiDiGraph(fin_submatrix)

#Form a dot file in the current directory
nx.drawing.nx_pydot.write_dot(fin_MDGraph,'Final.dot')

#Edit the dot file: Required Editing in terms of node label, color and other parameters


#To form Graph 3 (Varying Bubble Size)

#To get the page rank of required nodes, we reshape it from 1 X N to N X 1
pg_rank.shape = n,1

#Slicing the required nodes
nodes_pg_rank = pg_rank[1044:1054]

#converting to row major from column major
nodes_pg_rank.shape=1,10

#Since the page rank values are in the order of 10^-7 multiply with 10^8
nodes_pg_rank=10e8*nodes_pg_rank

#Giving the new labels to nodes. Format- Old_node_name: str(Node No.) : str([10^5 * Score[Node No]])
lab =({0:str(1044)+ " : " + str(10e5*pg_rank[1044]),
	1:str(1045)+ " : " + str(10e5*pg_rank[1045]),
	2:str(1046)+ " : " + str(10e5*pg_rank[1046]),
        3:str(1047)+ " : " + str(10e5*pg_rank[1047]),
        4:str(1048)+ " : " + str(10e5*pg_rank[1048]),
        5:str(1049)+ " : " + str(10e5*pg_rank[1049]),
        6:str(1050)+ " : " + str(10e5*pg_rank[1050]),
        7:str(1051)+ " : " + str(10e5*pg_rank[1051]),
        8:str(1052)+ " : " + str(10e5*pg_rank[1052]),
        9:str(1053)+ " : " + str(10e5*pg_rank[1053])})

#Attributes to Graph
nx.draw(fin_MDGraph,labels=lab,
        arrows=True, with_labels=True,
        node_size=nodes_pg_rank,
        style="dotted",
        node_color=range(10),
        edge_color=range(100),
        cmap=plt.cm.Spectral,
        width=0.8,
        edge_cmap=plt.cm.GnBu)

#Using matplotlib drawing the graph.
plt.show()
