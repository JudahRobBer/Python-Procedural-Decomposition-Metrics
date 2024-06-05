"""
Module to compose all relevant information about the source code into a vectorized representation
"""
from augmentedCallGraphGenerator import AugmentedCallGraph,generate_augmented_call_graph
from complexityMetricGenerator import get_average_cyclomatic_complexity, get_average_cognitive_complexity

def generate_vector_from_file(package:str, filename:str):
    augmented_cg = generate_augmented_call_graph(package,filename)
    augmented_cg.printNodeSet()
    reused_node_count = augmented_cg.count_reused_leafs()
    leaf_nonLeaf_ratio = augmented_cg.get_leaf_nonLeaf_ratio()
    transitivity = augmented_cg.calculate_transitivity()

    #avg_cyclomatic_complexity = get_average_cyclomatic_complexity(package,filename)
    #avg_cognitive_complexity = get_average_cognitive_complexity(package,filename)
    
    print(transitivity)
