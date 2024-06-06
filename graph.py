import copy
import dataclasses
from dataclasses import dataclass
import graphviz
import networkx as nx

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
            self.__genAdjList()
        elif adjList is not None and len(nodeSet) == 0:
            self.adjList = adjList
            self.__genNodeSet()
            self.__genEdgeSet()
        else:
            raise Exception("Invalid combination of parameters. Provide either a node and edge set, or an adjacency list")
    
    
    def __genAdjList(self) -> None:
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
    

    def __genNodeSet(self) -> None:
        self.nodes = {node for node in self.adjList.keys()}

    
    def __genEdgeSet(self) -> None:
        self.edges = set()
        for node, neighbors in self.adjList.items():
            for neighbor in neighbors:
                self.edges.add((node,neighbor))

    def addNode(self, node:any) -> None:
        if node not in self.nodes:
            self.nodes.add(node)
            self.__genAdjList()
    
    
    def addEdge(self, edge:tuple) -> None:
        if edge not in self.edges:
            self.edges.add(edge)
            self.__genAdjList()

    
    def printAdjList(self) -> None:
        for node, neighbors in self.adjList.items():
            print(node, ": ", end="")
            print(neighbors)
        print()
    
    
    def printNodeSet(self) -> None:
        print("Nodes: " + str(self.nodes))
    

    def printEdgeSet(self) -> None:
        print("Edges: " + str(self.edges))



class AugmentedCallGraph(DirectedGraph):
    
    @dataclass(eq=False,frozen=True) 
    class FunctionNode:
        name:str
        fan_in:int
        fan_out:int
        parameter_count:int
        #if the function is builtin, it is not counted by fan_out
        #the function is built_in if it wasn't detected when parameter_counting
        built_in:bool = False

        
        """ def __repr__(self):
            return self.name """
        
        #higher information representation
        def __repr__(self):
            fields = dataclasses.fields(self)
            repr = ""
            for v in fields:
                repr += f'{v.name}: = {getattr(self, v.name)} '
            return repr
            
        


    def __init__(self,adjList:dict,parameter_counts:dict):
        """
        generate a graph object whose nodes are FunctionNodes from the data
        """
        
        funcAdjList = {}
        built_in_nodes = self.__get_built_in_nodes(adjList,parameter_counts)
        fan_out = self.__generate_fan_out_map(adjList,built_in_nodes)
        fan_in = self.__generate_fan_in_map(adjList)
        
        #reconstruct existing nodes as function nodes
        for node, neighbors in adjList.items():
            funcNode = self.__build_functionNode(node,fan_in[node],fan_out[node],parameter_counts)
            funcNeighbors = set()
            for neighbor in neighbors:
                funcNeighbor = self.__build_functionNode(neighbor,fan_in[neighbor],fan_out[neighbor],parameter_counts)
                funcNeighbors.add(funcNeighbor)
            funcAdjList[funcNode] = funcNeighbors
        
        super().__init__(adjList=funcAdjList)

    
    def __get_built_in_nodes(self,adjList:dict,parameter_counts:dict):
        """
        We have to know if a node is built-in before we can compute the fan in,
        which means we have to know if its built-in before we build the functionNode
        """
        return {node for node in adjList.keys() if node not in parameter_counts.keys()}

    
    #following constructions of dictionaries in advance are necessary for construction of frozen class FunctionNode
    def __generate_fan_out_map(self,adjList:dict,built_in_nodes:set) -> dict:
        """
        Asssociates Nodes with their out degree, built_in functions are not counted
        """
        fan_out = {key : sum(1 for i in lst if i not in built_in_nodes) for key,lst in adjList.items()}
        return fan_out

    
    def __generate_fan_in_map(self,adjList:dict) -> dict:
        """
        Associates nodes with their in-degree
        """
        fan_in = {key : 0 for key in adjList.keys()}

        for key in fan_in:
            for subroutines in adjList.values():
                if key in subroutines:
                    fan_in[key] += 1
                    
        return fan_in

    
    def __build_functionNode(self,name:str,fan_in:int,fan_out:int,parameter_counts:dict):
        if name not in parameter_counts.keys():
            return self.FunctionNode(name,fan_in,fan_out,-1,True)
        else:
            return self.FunctionNode(name,fan_in,fan_out,parameter_counts[name])

    
    def visualize_graph(self): 
        dot = graphviz.Digraph()

        for node, neighbors in self.adjList.items():
            dot.node(str(node))
            for neighbor in neighbors:
                dot.edge(str(node),str(neighbor))
        
        dot.render('graph',format='png',view = True)


    def printNodeSet(self) ->None:
        for node in self.nodes:
            print(node)
    

    def count_reused_leafs(self) -> int:
        """
        Any leaf node that is called by multiple intermediate or root nodes indicates that the code contains reusable modules.
        We specifically consider the reuse of low-abstraction functions, but the principle could potentially be expanded to include
        the reuse of higher-abstraction functions
        """
        return sum(1 for node in self.nodes if node.fan_out == 0 and node.fan_in > 1 and not node.built_in)


    def get_leaf_nonLeaf_ratio(self) -> float:
        """
        The leaf to non-leaf ratio provides a proxy for the overall structure of the graph
        """
        
        leaf_count = sum(1 for node in self.nodes if node.fan_out == 0 and not node.built_in)
        nonLeaf_count = sum(1 for node in self.nodes if node.fan_out != 0 and not node.built_in)

        return leaf_count / nonLeaf_count
    

    def calculate_transitivity(self) -> float:
        """
        Graph transitivity is the ratio of closed triangles to connected triplets of notes (K3 / P3) * 3
        This metric serves to capture violations of the single level of abstraction. If a function calls a function
        on the same abstraction level (they are both called by the same function), a closed triangle is formed
        """
        networkxGraph = nx.Graph(self.adjList)
        return nx.transitivity(networkxGraph)






            