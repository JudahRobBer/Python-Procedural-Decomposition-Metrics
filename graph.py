import copy
from dataclasses import dataclass
import graphviz

class DirectedGraph:
    """
    Attributes
    ----------
    nodes : set
        Set of vertices of the graph
    edges : set
        Set of edges of the graph (ordered)
    adjList : dict
        Dictionary mapping nodes to the set of neighbors (out)
        
    """
        

    def __init__(self,nodeSet:set = set(), edgeSet:set = set(), adjList:dict = None):
        """
        vertex set is a set of integers, edgeSet is a set of tuples
        every element of every tuple of edgeSet must be an element of vertex set

        Parameters:
        nodeSet (set): set of integers representing nodes
        edgeSet (set): set of tuples representing edges
        adjList (dict): dictionary representing and adjacency list

        Returns:
        None
        """
        if adjList is None and len(nodeSet) != 0:
            self.nodes:set = copy.deepcopy(nodeSet)
            self.edges:set = copy.deepcopy(edgeSet)
            self.genAdjList()
        elif adjList is not None and len(nodeSet) == 0:
            self.adjList = adjList
            self.genNodeSet()
            self.genEdgeSet()
        else:
            raise Exception("Invalid combination of parameters. Provide either a node and edge set, or an adjacency list")
    
    
    def genAdjList(self) -> None:
        """
        Map every vertex to set of neighbors, generating an adjacancy list

        Parameters:
        None

        Returns:
        adjList (dict): dictionary representing the adjacency list
        """
        
        adjList = {node : set() for node in self.nodes }
        
        edge: tuple
        for edge in self.edges:
            #graph is undirected, despite variable name denotation
            try:
                source, dest = edge[0], edge[1]
                if not (source in self.nodes and dest in self.nodes):
                    raise ValueError("at least one endpoint was not in vertex set", source, dest)
                adjList[source].add(dest)
            except ValueError as err:
                message, source, dest = err.args[0],err.args[1],err.args[2]
                print(message)
                print("source node:",source)
                print("destination node:",dest)
                continue
        
        self.adjList = copy.deepcopy(adjList)
    

    def genNodeSet(self) -> None:
        self.nodes = {node for node in self.adjList.keys()}

    
    def genEdgeSet(self) -> None:
        self.edges = set()
        for node, neighbors in self.adjList.items():
            for neighbor in neighbors:
                self.edges.add((node,neighbor))

    def addNode(self, node:any) -> None:
        """
        Add the input node to the graph

        Parameters:
        node (any): Node to be added to the graph

        Returns: 
        None
        """
        if node not in self.nodes:
            self.nodes.add(node)
            self.genAdjList()
    
    
    def addEdge(self, edge:tuple) -> None:
        """
        Add the input edge to the graph

        Parameters:
        edge (tuple): edge to be added to the graph

        Returns:
        None
        """
        if edge not in self.edges:
            self.edges.add(edge)
            self.genAdjList()

    
    def printAdjList(self) -> None:
        """
        Prints the adjacency list of the graph

        Parameters:
        None

        Returns:
        None
        """
       
        for node, neighbors in self.adjList.items():
            print(node, ": ", end="")
            print(neighbors)
        print()
    
    
    def printNodeSet(self) -> None:
        """
        Prints the vertex set of the graph
        
        Parameters:
        None

        Returns:
        None
        """
        print("Vertices: " + str(self.vertices))
    

    def printEdgeSet(self) -> None:
        """
        Prints the edge set of the graph

        Parameters:
        None

        Returns:
        None
        """
        print("Edges: " + str(self.edges))



class AugmentedCallGraph(DirectedGraph):
    
    @dataclass(eq=False,frozen=True) 
    class FunctionNode:
        name:str
        fan_in:int
        fan_out:int
        parameter_count:int
        
        def __repr__(self):
            return self.name


    def __init__(self,adjList:dict, fan_in:dict,fan_out:dict, parameter_counts:dict):
    
        #generate a graph object whose nodes are FunctionNodes from the data
        funcAdjList = {}
        for node, neighbors in adjList.items():
            funcNode = self.FunctionNode(node,fan_in[node],fan_out[node],parameter_counts[node])
            funcNeighbors = set()
            for neighbor in neighbors:
                funcNeighbor = self.FunctionNode(neighbor,fan_in[neighbor],fan_out[neighbor],parameter_counts[neighbor])
                funcNeighbors.add(funcNeighbor)
            funcAdjList[funcNode] = funcNeighbors
        
        super().__init__(adjList=funcAdjList)

    
    def visualize_graph(self): 
        dot = graphviz.Digraph()

        for node, neighbors in self.adjList.items():
            dot.node(str(node))
            for neighbor in neighbors:
                dot.edge(str(node),str(neighbor))
        
        dot.render('graph',format='png',view = True)
    

    def count_reused_leafs(self) -> int:
        """
        Any leaf node that is called by multiple intermediate or root nodes indicates that the code contains reusable modules.
        We specifically consider the reuse of low-abstraction functions, but the principle could potentially be expanded to include
        the reuse of higher-abstraction functions
        """
        return sum(1 for node in self.nodes if node.fan_out == 0 and node.fan_in > 1)


    def get_leaf_nonLeaf_ratio(self) -> float:
        """
        The leaf to non-leaf ratio provides a proxy for the overall structure of the graph
        """
        
        leaf_count = sum(1 for node in self.nodes if node.fan_out == 0)
        nonLeaf_count = sum(1 for node in self.nodes if node.fan_out != 0)

        return leaf_count / nonLeaf_count





            