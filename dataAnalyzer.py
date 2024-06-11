from decompositionVectorGenerator import gen_vector_from_file, gen_labeled_vector, data_order
from decompositionVectorGenerator import gen_guidelines_vector, guidelines_data_order
import numpy as np
import os
import csv
from enum import IntEnum
"""
Module to handle the comparison and analysis of procedural decomposition vectors
"""



def analyze_data_generic(files:set,input_directory:str,output_directory:str,vector_generator,data_schema:IntEnum):
    
    def write_to_csv(data:list,headers:list,output_file:str) -> None:
        with open(f"{output_directory}/{output_file}", 'w') as csv_file:
            writer = csv.DictWriter(csv_file,fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
    
    
    output_files = {file[:-3] + ".csv" for file in files}
    all_data = {file : [] for file in output_files}
    for student in os.scandir(input_directory):
        if student.is_dir():
            print(student.name)
            for item in os.scandir(student):
                print(item.name)
                if item.name in files:
                    data = vector_generator(f"{input_directory}/{student.name}",item.name) #for use in computation
                    labeled_data = gen_labeled_vector(data,data_schema) #for use in storage
                    labeled_data["id"] = student.name
                    print(labeled_data)
                    output_file = item.name[:-3] + ".csv"
                    
                    all_data[output_file].append(labeled_data)
    
    garden_solution = vector_generator("solution_code","hw2_garden_solution.py")
    labeled_solution = gen_labeled_vector(garden_solution,data_schema)
    labeled_solution["id"] = "solution"
    all_data["hw2_garden.csv"].append(labeled_solution)


    #header names
    fields = ["id"]
    fields += [data_type.name for data_type in data_schema]
    for file, data in all_data.items():
        write_to_csv(data,fields,file)

def analyze_data_with_guidelines():
    """
    Generate a csv file containing analysis of metrics according to current guidelines

    1) Is your code globally scoped? (Yes/No)
    2) How many of your functions return and print values? (count)
    3) How much data (inputs, parameters, and function calls) does your biggest function need? (diff)
    4) Is there shared behavior between functions thats being appropriately abstracted (count)

    Considerations 3 and 4 are considered in comparison to an optimally decomposed solution
    """
    files = {"hw2_garden.py","hw2_owls.py","hw2_tower.py"}
    analyze_data_generic(files=files,input_directory="student_code",output_directory="metric_outputs",vector_generator=gen_guidelines_vector,data_schema=guidelines_data_order)
    


def analyze_data():
    """ 
    Generate a CSV file containing the complete analysis of all the current metrics for all the files in a given directory
    
    1) Iterate over every file
    2) Generate analysis for each file
    3) write formatted analysis to a csv file
     """
    files = {"hw2_garden.py","hw2_owls.py","hw2_tower.py"}
    analyze_data_generic(files=files,input_directory="student_code",output_directory="metric_outputs",vector_generator=gen_vector_from_file,data_schema=data_order)

   

def normalize_vector(vector:np.array) -> np.array:
    """
    u = (1 / |v|) * v
    """
    try:
        return vector / np.linalg.norm(vector)
    except ZeroDivisionError:
        return vector


def calculate_cosine_similarity(norm_solution_vector:np.array, norm_comparison_vector:np.array) -> float:
    """
    After normalizing the vectors the equation for cos(theta) reduces to the dot product of the vectors
    """
    return sum(norm_solution_vector[i] * norm_comparison_vector[i] for i in range(len(norm_solution_vector)))


def get_most_significant_difference(norm_solution_vector:np.array, norm_comparison_vector:np.array) -> int | None:
    """
    If the code is detected to be significantly different from the solution vector,
    identify the component that differs the most, format it as a suggestion
    
    1.) calculate the difference vector as the solution_vector - comparison_vector
    2.) apply a sign flip to the criteria where negative values are a positive indicator (node_reuse, leaf_ratio)
    3.) Now, all negative indicators are registered as negative values
    4.) Sort the array in ascending order, return the criteria that has the largest negative value
    """
    diff_vector = norm_solution_vector - norm_comparison_vector
    #sort vector maintaining index as (original index,value) tuples
    labeled_sorted_diff_vector = sorted(enumerate(diff_vector),key= lambda x: x[1])
    most_significant_diff = labeled_sorted_diff_vector[0]

    #if the most significant difference relates to the graph structure, but the students code is totally global,
    #prioritize global structure
    if (norm_comparison_vector[data_order.leaf_ratio] == 0): #no nodes deteced
        return data_order.global_code_volume
    
    #there is in fact a negative feature detected, return the original index of the feature
    if most_significant_diff[1] < 0:
        return most_significant_diff[0]

    #The comparison vector was better than the solution vector on all measurements
    return None


def generate_suggestion(feature:int) -> str:
    match feature:
        case data_order.global_code_volume:
            return """
                Our analysis shows that you have significantly more code written in the global scope 
                compared to an optimally decomposed solution. Consider moving code from a global scope into an
                appropriate subroutine, or main.
            """
        case data_order.reused_nodes:
            return """
            Our analysis shows that you reused fewer functions than our optimally decomposed solution.
            Look for repetition in your code and try to create small, reusable functions.
            """
        
        case data_order.leaf_ratio:
            return """
            Our analysis shows that compared to our optimally decomposed solution, your ratio of 
            low abstraction to high abstraction functions was lower, meaning you had proportionally more
            complex functions. Consider separating more functionality into smaller functions
            """
        
        case data_order.transitivity:
            return """
            Our analysis shows that you had more usages of multiple levels of abstraction than our
            optimally decomposed solution. Check through your functions to ensure that within each function
            you maintain a single level of abstraction whenever possible
            """
        case data_order.cyc_complexity | data_order.cog_complexity:
            return """
            Our analysis shows that on average your functions were more complex than the functions in our 
            optimally decomposed solution. Ensure that your functions are following the single responsibility principle
            by making sure that all of the code in your function works together to accomplish a single, concise purpose
            """
        
    
def analyze_vectors():
    """
    function documents relevant analysis behavior and provides sample output
    """
    #currently used to test multiple function output types
    #ignore
    directory = "student_code/s1"
    filename = "hw2_garden.py"
    gen_guidelines_vector(directory,filename)

    


analyze_data_with_guidelines()