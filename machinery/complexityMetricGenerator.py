
"""
Interface for complexipy and radon to collect complexity metrics.
Returns data as an average of each metric for the respective functions
"""

import radon.complexity, radon.metrics
import os
import csv
import time

# Provides the cyclomatic complexity of each method in dictionary format.
def get_cyclomatic_complexity_dictionary(package:str,filename:str):
    with open(f"{package}/{filename}") as file:
        source = file.read()
        complexities = radon.complexity.cc_visit(source)

        ret_Dict = {}

        # Populates the dictionary.
        for Function in complexities:
            ret_Dict[Function.name] = Function.complexity

        return ret_Dict

def get_maintainability_index(package:str,filename:str):
    with open(f"{package}/{filename}") as file:
        source = file.read()
        maintainability = radon.metrics.mi_visit(source)
    
    return maintainability


def get_average_cyclomatic_complexity(package:str,filename:str) -> float:
    """
    Use Radon to get average cyclomatic complexity per function
    """
    complexity_dictionary = get_cyclomatic_complexity_dictionary(package,filename)
    if len(complexity_dictionary) != 0:
        return sum(value for value in complexity_dictionary.values()) / len(complexity_dictionary)

    #empty case, no functions
    return 0

    

def get_average_cognitive_complexity(package:str,filename:str) -> float:
    """
    Use Complexipy to get average cognitive complexity per function
    Complexipy is a commandline tool, accessing the output efficiently requires a little bit of writing/deleting temporary ouputted csv files
    """

    def write_results_to_csv():
        os.system(f"complexipy ./{package}/{filename} -o -q")

    
    def read_csv_file():
        try:
            with open("complexipy.csv") as data:
                csvLines = list(csv.reader(data))
                return csvLines[1::] #ignore header line
        except FileNotFoundError:
            print("Couldn't read csv file?")
            return None
            
                
    def delete_csv_file():
        os.system("rm complexipy.csv")
        os.system("clear")
    
    write_results_to_csv()
    csvLines = read_csv_file()
    delete_csv_file()
    
    #last index in the line represents the complexity
    if csvLines is not None and len(csvLines) > 0:
        total = sum(int(line[-1]) for line in csvLines)
        if len(csvLines) > 0:
            return total / len(csvLines)
    
    #totally global code
    return 0