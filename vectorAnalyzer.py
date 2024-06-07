from decompositionVectorGenerator import generate_vector_from_file, DATA_ORDER
import numpy as np
"""
Module to handle the comparison and analysis of procedural decomposition vectors
"""

def analyze_vectors():
    package = "testpackage"
    decomposed = "drivetimes.py"
    globallyScoped = "drivetimesGlobal.py"
    
    solution_vector = generate_vector_from_file(package,decomposed)
    comparison_vector = generate_vector_from_file(package,globallyScoped)
    
    normalized_solution = normalize_vector(solution_vector)
    normalized_comparison = normalize_vector(comparison_vector)
    #similarity = cosine_similarity(normalized_solution,normalized_comparison)

    #print("Similarity: " + similarity)

    #testing sorting
    test1 = np.array([1,3,4])
    test2 = np.array([3,2,4])
    feature = get_most_significant_difference(test1,test2)
    print("Most different index: ",feature)


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
    
    most_significant_diff = labeled_sorted_diff_vector[0]
    
    #there is in fact a negative feature detected, return the original index of the feature
    if most_significant_diff[1] < 0:
        return most_significant_diff[0]

    #The comparison vector was better than the solution vector on all measurements
    return None


    

analyze_vectors()