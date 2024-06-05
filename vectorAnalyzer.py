from decompositionVectorGenerator import generate_vector_from_file


def main():
    package = "testpackage"
    filename = "drivetimes.py"
    generate_vector_from_file(package,filename)

main()