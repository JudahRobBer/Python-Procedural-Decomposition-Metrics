"""
Module to compose all relevant information about the source code into a vectorized representation
"""
from augmentedCallGraphGenerator import AugmentedCallGraph,generate_augmented_call_graph
from complexityMetricGenerator import get_average_cyclomatic_complexity, get_average_cognitive_complexity
from ast_analysis import get_global_code_volume, get_multiple_output_functions
from accessofForeignData import accessofForeignData
import numpy as np
from enum import IntEnum

class guidelines_data_order(IntEnum):
    reused_nodes = 0
    multiple_output_functions = 1
    largest_information_function = 2
    global_code_volume = 3

def gen_guidelines_vector(package:str,filename:str) -> np.array:
    #reused node count, information size of biggest class, multiple output count
    augmented_cg = generate_augmented_call_graph(package,filename)
    reused_nodes = augmented_cg.count_reused_leafs()

    #multiple output_functions
    multiple_output_functions_count = len(get_multiple_output_functions(package,filename))

    #function with largest information load
    foreignAccess = accessofForeignData()
    foreignAccess.get_Foreign_Access(package,filename)
    largest_function_size = foreignAccess.ret_Max_Access()


    return np.array([reused_nodes,multiple_output_functions_count,largest_function_size],dtype=float)



#enum matching the type of data to its index in the original vector
#used for later analysis of the data to make code more explicit
class data_order(IntEnum):
    global_code_volume = 0
    reused_nodes = 1
    leaf_ratio = 2
    transitivity = 3
    cyc_complexity = 4
    cog_complexity = 5


def gen_vector_from_file(package:str, filename:str) -> np.array:

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


def gen_labeled_vector(vector:np.array, labeling:IntEnum) -> dict:
    """
    Generate a labeled form of the vector for use in writing data
    Pythons dicts are preferred for this purpose because the generated list is used 
    for csv writing, rather than computation
    """
    index = 0
    data_dict = {}
    for data_type in labeling:
        data_dict[data_type.name] = vector[index]
        index += 1
    
    return data_dict




