"""
Module to compose all relevant information about the source code into a vectorized representation
"""
from augmentedCallGraphGenerator import AugmentedCallGraph,generate_augmented_call_graph
from complexityMetricGenerator import get_average_cyclomatic_complexity, get_average_cognitive_complexity

def generate_vector_from_file(package:str, filename:str):
    #augmented_call_graph = generate_augmented_call_graph(package,filename)
    avg_cyclomatic_complexity = get_average_cyclomatic_complexity(package,filename)
    avg_cognitive_complexity = get_average_cognitive_complexity(package,filename)
    print(avg_cognitive_complexity)
