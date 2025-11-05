


from UserHandle import getFile, getParameters
from GA import runGeneticAlgorithm

def main():
    #Main Assignment program loop
    while True:
        #Select File and read it, checking if it's a valid input
        input = getFile()
        if (input == "Error"):
            print("Invalid file input, please try again.")
            return
        
        #Set Parameters for the GA
        params = getParameters()
        if (params == "Error"):
            print("Invalid parameter input, please try again.")
            return
        
        #Run Genetic Algorithm with input file and parameters
        print("Running Genetic Algorithm...")
        if (runGeneticAlgorithm(input, params) == "Error"):
            print("An error occurred while running the Genetic Algorithm.")
            return