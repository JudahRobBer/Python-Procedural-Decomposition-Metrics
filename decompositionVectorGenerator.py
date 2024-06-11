"""
Module to compose all relevant information about the source code into a vectorized representation
"""
from augmentedCallGraphGenerator import AugmentedCallGraph,generate_augmented_call_graph
from complexityMetricGenerator import get_average_cyclomatic_complexity, get_average_cognitive_complexity
from ast_analysis import get_global_code_volume, get_multiple_output_functions
import numpy as np
from enum import IntEnum


#enum matching the type of data to its index in the original vector
#used for later analysis of the data to make code more explicit
class data_order(IntEnum):
    global_code_volume = 0
    reused_nodes = 1
    leaf_ratio = 2
    transitivity = 3
    cyc_complexity = 4
    cog_complexity = 5


def generate_vector_from_file(package:str, filename:str) -> np.array:
    #not included in vector
    violating_functions = get_multiple_output_functions(package,filename)

    augmented_cg = generate_augmented_call_graph(package,filename)
    global_code_volume = get_global_code_volume(package,filename)
    
    #multiply values by negative one to standardize later process of component comparison
    reused_node_count = -1 * augmented_cg.count_reused_leafs()
    leaf_nonLeaf_ratio = -1 * augmented_cg.get_leaf_nonLeaf_ratio()
    
    transitivity = augmented_cg.calculate_transitivity()

    avg_cyclomatic_complexity = get_average_cyclomatic_complexity(package,filename)
    avg_cognitive_complexity = get_average_cognitive_complexity(package,filename)

    lst = [global_code_volume,reused_node_count,leaf_nonLeaf_ratio,
           transitivity,avg_cyclomatic_complexity, avg_cognitive_complexity]
    
    return np.array(lst,dtype=float) 


def gen_labeled_vector(vector:np.array) -> dict:
    """
    Generate a labeled form of the vector for use in writing data
    Pythons dicts are preferred for this purpose because the generated list is used 
    for csv writing, rather than computation
    """
    index = 0
    data_dict = {}
    for data_type in data_order:
        data_dict[data_type.name] = vector[index]
        index += 1
    
    return data_dict


