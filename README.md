
Page Rank Implementation
===========
Google's page rank implementation on p2p file sharing database. 

To combat the problem of spider trap and dead ends we used another matrix. Via Teleportation these problems were resolved. Also since operating on rows seemed convenient, we made it row stochastic instead of column stochastic. Using Markov chain process, page ranks were calculated.
To draw the graphs, we used dot (basic graph language) and matplotlib. Matplotlib doesn’t give arrowheads. To visualize with arrowheads as well, we used dot.

Usage
------
        First run Gnutella_page_rank.py
        Then run Graph.py

General Description
-------------------

### Graph.py

This is for visualizing the graph structures developed in the Gnutella_page_rank.py.

    To form Graph 1 (Graph with original links)

![alt text](https://github.com/ronak-07/PageRank/blob/master/Initial.png)

- Finding the submatrix: Since the number of nodes were quite high, we located 10 nodes that helped us to visualize the graph structure after calculating the original_votes.

- Converting the submatrix to a Multi Di Graph using Networkx package
Multi Di Graph allow self and parallel loops between two nodes. Thus among other options, it described the graph is most accurate manner 

- Form a dot file in the current directory using Networkx package
Via this we prepare a dot file having a graph representation. This ensures that we don’t have to write the dot file from the scratch.

        To form Graph 2 (Graph with final links)
        
![alt text](https://github.com/ronak-07/PageRank/blob/master/Final.png)

- Instead of passing the original_votes as matrix we passed final matrix in the subarray function. Other things were similar.

- Changes in the attributes of the generated dot files. This ensured that graphs generated have the labels as their node ids. Also other attributes like edge color, node color etc were changed.

        To form Graph 3 (Varying Bubble Size)

![alt text](https://github.com/ronak-07/PageRank/blob/master/Bubble_Spectrum.png)

- To visualize the page ranks along with nodes, we used matplotlib. Size of the nodes is 10^8 of their respective page_ranks. The displayed page_rank is 10^5 of their respective page_ranks. This manipulation was done as the default size is 300 units and the page_ranks were of the order of 10^-6.  

- Other attributes were also experimented for better visualizations.

###  Gnutella_page_rank.py
-	Each row is read from the p2p_Gnutella.txt and original_votes matrix is being populated.

-	Since we are trying to make the matrix as Row Stochastic.
    Find the value of vote:

        1. Sum of no. of elements for each row where original_votes[row][j]>0.
        2. Divide by this sum to get the value of each vote
        3. Update the value in original_votes Matrix

-	To solve the spider trap & Dead end problem.
	
        final= beta*original_votes + (1-beta)*teleported
        where beta= probability of opting for the link it originally pointed to
        1- beta= probability to opt for all opting any node

-	By using power matrix method we calculated the final page ranks

-	Since the data corpus is static, we decided to tradeoff space with time. This uses the Pickle package to permanently store the following:
        original_votes 			Matrix to hold the original_votes
        final				Matrix to store the final votes
        page_rank			To store the page rank of nodes


Contributors
-------------
[Ronak Sisodia](https://github.com/ronak-07)
