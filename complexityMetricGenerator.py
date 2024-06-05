
"""
Interface for complexipy and radon to collect complexity metrics.
Returns data as an average of each metric for the respective functions
"""

from radon.complexity import cc_visit
import os
import csv


def get_average_cyclomatic_complexity(package:str,filename:str) -> float:
    with open(f"{package}/{filename}") as file:
        source = file.read()
        complexities = cc_visit(source)
        total = sum(func.complexity for func in complexities)
        return total / len(complexities)
    

def get_average_cognitive_complexity(package:str,filename:str) -> float:

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
    total = sum(int(line[-1]) for line in csvLines)
    return total / len(csvLines)