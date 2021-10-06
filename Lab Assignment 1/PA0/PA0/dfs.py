#
# dfs.py
#
# This file provides a function implementing depth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
# 
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
# 


from route import Node
from route import Frontier


def DFS(problem, repeat_check=False):
    """Perform depth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    # PLACE YOUR CODE HERE
    #TreeNode = Node within the tree
    #TreeQueue = Queue of nodes of the tree (contains treeNodes)
    #problem is a function of the route_problem class - is_goal is a function of the same class

    #Starting position of the Map
    treeNode = Node(problem.start) # the start of the problem on road map

        #checking if Node contains a state of the solution 
    if problem.is_goal(treeNode.loc): #.loc will give the location
        return treeNode # we have found our soultion

    #For DFS make sure to write true for the stack parameter
    treeQueue = Frontier(treeNode, True)
    
    #we want to check if we need to check the Node or not... True means we do 
    if(repeat_check == True):
        #we are initializing a list to carry "Visited" Nodes 
        visited = [treeNode.loc] #creating a list in Python containg the location of the visited nodes

    #as long as the TreeQueue list isnt empty 
    while (treeQueue.is_empty() == False):
        #we are pulling one Node of the list TreeQueue to account as a Checked node 
        checked = treeQueue.pop()
        #if the goal of the problem is the checked location of the checked node then we have the soultion
        if problem.is_goal(checked.loc): #.loc will give the location
            return  checked # we have found our soultion
            #we are expanding the node checked of the problem... expand returns a list so now we have a list of children of the checked Nodes
        children = checked.expand(problem)
    
    #exclusively checking the nodes within the list of checked nodes we have
        for child in children:
            #If we need to check 
            if(repeat_check == True):
                #and the loaction of the child is within the visited list of node locations
                if(child.loc in visited):
                    pass # we will pass 
                else: #if the location of the child is not in the list of visited nodes 
                    #we will add the child to the list TreeQueue
                    treeQueue.add(child)
                    #and we will also add the location of the child node to the list of visited node locations
                    visited.append(child.loc) # adding location of the node to the visited since its a regular list we just use append
            else: #not true -- we dont need to perform a check... but add the child node to the list TreeQueue of nodes
                treeQueue.add(child)
    return None  # Similar to void in C...

