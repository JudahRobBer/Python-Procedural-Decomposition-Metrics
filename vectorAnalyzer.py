from decompositionVectorGenerator import generate_vector_from_file, gen_labeled_vector, data_order
import numpy as np
import os
import csv
"""
Module to handle the comparison and analysis of procedural decomposition vectors
"""

def analyze_test_data():
    """
    Generate a CSV file containing the complete analysis of all the current metrics for all the files in a given directory
    
    1) Iterate over every file
    2) Generate analysis for each file
    3) write formatted analysis to a csv file
    """

    def write_to_csv(data:list,headers:list) -> None:
        with open(output_file, 'w') as csv_file:
            writer = csv.DictWriter(csv_file,fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

    #analyze data
    directory = "testpackage"
    output_file = "metric_outputs/test_table.csv"
    all_data = []
    for item in os.scandir(directory):
        data = generate_vector_from_file(directory,item.name) #for use in computation
        labeled_data = gen_labeled_vector(data) #for use in storage
        all_data.append(labeled_data)
    
    #header names
    fields = [data_type.name for data_type in data_order]

    write_to_csv(all_data,fields)

    
def analyze_vectors():
    package = "testpackage"
    decomposed = "drivetimes.py"
    globallyScoped = "drivetimesGlobal.py"
    
    solution_vector = generate_vector_from_file(package,decomposed)
    comparison_vector = generate_vector_from_file(package,globallyScoped)
    print("Original solution vector: ", solution_vector)
    print("Original global vector: ", comparison_vector)
    
    normalized_solution = normalize_vector(solution_vector)
    print("norm_solution: ",normalized_solution)
    normalized_comparison = normalize_vector(comparison_vector)
    print("norm global: ",normalized_comparison)
    
    #similarity = cosine_similarity(normalized_solution,normalized_comparison)
    most_significant_difference = get_most_significant_difference(normalized_solution,normalized_comparison)
    print(generate_suggestion(most_significant_difference))


    
    


def normalize_vector(vector:np.array) -> np.array:
    """
    u = (1 / |v|) * v
    """
    try:
        return vector / np.linalg.norm(vector)
    except ZeroDivisionError:
        return vector


def cosine_similarity(norm_solution_vector:np.array, norm_comparison_vector:np.array) -> float:
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
    print("difference vector: ",labeled_sorted_diff_vector)
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


analyze_test_data()