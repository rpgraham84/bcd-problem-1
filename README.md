Nearest Common Ancestor problem for BCD Travel
==============================================


Problem Description
-------------------
Big companies sometimes have a complex hierarchical structure. It is essential to represent
this structure as a tree. Sometimes, we need to know information about a company, for example
the nearest common ancestor of two companies.
Given a tree we need to find the nearest common ancestor for any 2 nodes.
Input: The program should take a file with tree as an input and ids of 2 nodes to find their
closest common ancestor. The file structure is pretty straightforward - each node and its parent
are written on a separate line. Obviously, root nodes has no parents. E.g.:

input.txt

NodeA

NodeB NodeA

NodeC NodeB

NodeD NodeA

NodeF

Nodes to find ancestor - NodeD NodeC

Output: NodeA is the closest common ancestor for NodeD and NodeC.


Design and Rationale
--------------------
The solution to the problem builds a forest (dict) to represent the data in memory. A class, Tree
is implemented to maintain the value and parent relation of each node and a recursive function,
get_parents is used to build a path of values back to it's root node. This path is compared node by 
node to the path of another node to determine the nearest common ancestor.

This solution took me about six hours.


Usage
-----

````bash
python solution.py input.txt NodeC NodeD
````

Should print NodeA.



Testing
-------

````bash
python -m unittest -v tests.solution_tests
````

