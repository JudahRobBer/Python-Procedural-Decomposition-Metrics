
"""
Interface for complexipy and radon to collect complexity metrics.
Returns data as an average of each metric for the respective functions
"""

import radon.complexity
import os
import csv


def get_average_cyclomatic_complexity(package:str,filename:str) -> float:
    """
    Use Radon to get average cyclomatic complexity per function
    """
    with open(f"{package}/{filename}") as file:
        source = file.read()
        complexities = radon.complexity.cc_visit(source)
        total = sum(func.complexity for func in complexities)
        return total / len(complexities)
    

def get_average_cognitive_complexity(package:str,filename:str) -> float:
    """
    Use Complexipy to get average cognitive complexity per function
    Complexipy is a commandline tool, accessing the output efficiently requires a little bit of writing/deleting temporary ouputted csv files
    """

    def write_results_to_csv():
        os.system(f"complexipy ./{package}/{filename} -o -q")

    
    def read_csv_file():
        with open("complexipy.csv") as data:
            csvLines = list(csv.reader(data))
            return csvLines[1::] #ignore header line
            
                
    def delete_csv_file():
        os.system("rm complexipy.csv")
        os.system("clear")
    
    write_results_to_csv()
    csvLines = read_csv_file()
    delete_csv_file()
    
    #last index in the line represents the complexity
    total = sum(int(line[-1]) for line in csvLines)
    return total / len(csvLines)