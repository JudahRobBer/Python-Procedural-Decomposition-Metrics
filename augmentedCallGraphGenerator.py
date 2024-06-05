import json
from graph import DirectedGraph, AugmentedCallGraph
from scalpel.call_graph.pycg import CallGraphGenerator, formats



def generate_augmented_call_graph(package:str,filename:str) -> AugmentedCallGraph:
    call_graph = __generate_call_graph(package,filename)
    fan_out = __generate_fan_out_map(call_graph)
    fan_in = __generate_fan_in_map(call_graph)
    return AugmentedCallGraph(call_graph,fan_in,fan_out)


def __generate_call_graph(package:str,filename:str) -> dict:
    cg_generator = CallGraphGenerator([f"./{package}/{filename}"], filename)
    cg_generator.analyze()
    formatter = formats.Simple(cg_generator)
    formatted_graph:dict = formatter.generate()
    cleaned_graph = __clean_formatted_graph(formatted_graph,filename)
    return cleaned_graph


def __clean_formatted_graph(formatted_graph:dict,filename:str) -> dict:
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
        if len(cleaned_key) > 0 and cleaned_key.find(".") == -1:
            cleaning_map[key] = cleaned_key

    return cleaning_map


def __generate_fan_out_map(call_graph:dict) -> dict:
    fan_out = {key : len(lst) for key,lst in call_graph.items()}
    return fan_out

def __generate_fan_in_map(call_graph:dict) -> dict:
    fan_in = {key : 0 for key in call_graph.keys()}

    for key in fan_in:
        
        for subroutines in call_graph.values():
            if key in subroutines:
                fan_in[key] += 1
                
    return fan_in
