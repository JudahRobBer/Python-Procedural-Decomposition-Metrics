import json
from machinery.graph import DirectedGraph, AugmentedCallGraph
from scalpel.call_graph.pycg import CallGraphGenerator, formats
from machinery.ast_analysis import get_function_parameter_counts
from pprint import pprint

"""
Module augments the call graph outputted by Scalpel by:
cleaning it to include only function names, and labeling each node with its fan-out, fan-in, and parameter count
"""

def generate_augmented_call_graph(package:str,filename:str) -> AugmentedCallGraph:
    call_graph = __generate_call_graph(package,filename)
    parameter_counts = get_function_parameter_counts(package,filename)
    return AugmentedCallGraph(call_graph,parameter_counts)


def __generate_call_graph(package:str,filename:str) -> dict:
    """
    Generates unformatted graph using scalpel, removes unnecessary information and returns it
    """
    cg_generator = CallGraphGenerator([f"./{package}/{filename}"], filename)
    cg_generator.analyze()
    formatter = formats.Simple(cg_generator)
    formatted_graph:dict = formatter.generate()
    cleaned_graph = __clean_formatted_graph(formatted_graph,filename)
    return cleaned_graph


def __clean_formatted_graph(formatted_graph:dict,filename:str) -> dict:
    """
    Scalpel Call graph includes information in the node such as the package and module name,
    deemed irrelevant for our single file use-case
    """
    cleaning_map = __generate_cleaned_function_map(formatted_graph,filename)
    cleaned_graph = {}


    for key, lst in formatted_graph.items():
        if key in cleaning_map:
            cleaned_key = cleaning_map[key]
            cleaned_graph[cleaned_key] = set()
        
            for item in lst:
                if item in cleaning_map:
                    cleaned_graph[cleaned_key].add(cleaning_map[item])

    return cleaned_graph


def __generate_cleaned_function_map(formatted_graph:dict,filename:str) -> dict:
    """
    Utility function to map the original formatting of a given function to its reduced form
    Example: ...testpackage.dummy.print_beak' : 'print_beak'
    """
    cleaning_map = {}
    abbreviated_filename = filename[:filename.find(".py")]
    key:str
    for key in formatted_graph.keys():
        newIndex = key.find(abbreviated_filename) + len(abbreviated_filename) + 1
        cleaned_key = key[newIndex::]
        #filters built-in functions
        if len(cleaned_key) > 0:
            cleaning_map[key] = cleaned_key

    return cleaning_map



