import json
from pprint import pprint
from augmentedCallGraphGenerator import AugmentedCallGraph,generate_augmented_call_graph




""" with open("example_results.json", "w+") as f:
    f.write(json.dumps(formatter.generate())) """



def main():
    package = "testpackage"
    filename = "dummy.py"
    augmented_call_graph = generate_augmented_call_graph(package,filename)
    print(augmented_call_graph.count_reused_leafs())

main()



