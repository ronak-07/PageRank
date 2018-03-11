"""  
  Project : To build PageRank                  
  Course No : CS F469 Information Retrieval

  Time (in seconds) for finding the result(Avg. of 3 runs):
                                                  nx.from_numpy_matrix(A)         : 0.3327369689941406
                                                  Calculating vote_value          : 66.64699625968933
                                                  Teleportation                   : 46.422672271728516
                                                  Markov chains                   : 107.17060327529907
Data Description

# Directed graph (each unordered pair of nodes is saved once): p2p_Gnutella.txt
# Directed Gnutella P2P network from August 4 2002
# Nodes: 10876 Edges: 39994
# FromNodeId	ToNodeId

"""

'''
        NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
'''
import networkx as nx

'''
        NumPy is the fundamental package for scientific computing with Python. It contains among other things: a powerful N-dimensional array object
'''
import numpy as np

'''
        Pickle package is used to save and load already saved data structures. It saves the pre processing time.
'''
import pickle

import time

# n is the total no of nodes
n=10878

#Probability of choosing the original_link
beta = 0.85                                 

#For markov chains, how much should be the difference
steady_state = 0.01                         

#Matrix to hold the original_votes
original_votes = np.zeros ( (n,n) )

#Matrix to store the final votes
final = np.zeros ( (n,n) )

#Array to store the final page rank
page_rank = np.zeros( (1,n) )

#Matrix to store the teleported votes
teleported = np.zeros( (n,n) )

#Used to fill the teleported Matrix
k=1/n

#To fill the teleported matrix
teleported.fill(k)

def markov_chain():
        """
            By using power matrix method we calculate the final page ranks
        """
        start = time.time()

        #Temporary array to store the value of previous iteration 
        r_temp = np.zeros( (1,n) )
        global page_rank

        #Assigning the first page a rank of 1. 
        page_rank[0][0] = 1

        #Power matrix method till the difference in consecutive page ranks > steady_state. (Steady state is declared globally)
        while np.sum(np.abs(page_rank - r_temp)) > steady_state:
                r_temp= page_rank.copy()
                page_rank = page_rank.dot(final)
                print(page_rank)
        print(time.time()-start)

def teleportation():
        """
                To solve the spider trap & Dead end problem.
                final = beta*original_votes + (1-beta)*teleported
                        where beta    =  probabilty of opting for the link it originally pointed to
                              1- beta =  proababilty to opt for all opting any node
        """
        start = time.time()
        global final
        final = beta*original_votes + (1-beta)*teleported
        print(time.time()-start)
    
def vote_value():
        """
                The Matrix is Row Stochastic.
                Find the value of vote:
                        1. Sum of no. of elements for each row where original_votes[row][j]>0.
                        2. Divide by this sum to get the value of each vote
                        3. Update the value in original_votes Matrix
        """
        start =time.time()
        for row in original_votes:
                if sum(row)>0:
                    vote = 1/sum(row)
                    row[row==1] = vote
        print(time.time()-start)
        
def pickled():
        """
            This function uses the Pickle Library to permanently store the following:
            Matrix: Original_Votes, Final_votes
            Array:  PageRank
        """
        with open("original_votes.pickle","wb")as f:
                pickle.dump(original_votes,f)
        with open("final.pickle","wb")as f:
                pickle.dump(final,f)
        with open("page_rank.pickle","wb")as f:
                pickle.dump(page_rank,f)

def main():
        start = time.time()
        
        with open("p2p_Gnutella.txt") as f:
                global original_votes
                for x in range(39994):
                    node = f.readline()
                    node = node.split("\t")

                    #From Node
                    a= int(node[0])

                    #To Node
                    b= int(node[1])     

                    #Matrix is ROW stochastic.
                    original_votes[a-1][b-1] = 1
                    
                end = time.time()
                print(end-start)
                
                print("Calculating vote_value")
                vote_value()
                
                print("Combating Spider Trap & Dead Ends: Teleportation")
                teleportation()
                
                print("Markov Chains to Calculate Page Rank")
                markov_chain()

                #Storing for future reference
                #Uncomment Only if you make any change in any formula or something else
                #pickled()

if __name__ == "__main__":
    main()          
