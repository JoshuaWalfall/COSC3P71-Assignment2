


from UserHandle import getFile, getParameters
from GA import runGeneticAlgorithm

def main():
    #Main Assignment program loop
    while True:
        #Select File and read it, checking if it's a valid input
        input = getFile()
        if (input == "Error"):
            print("Invalid file input, please try again.")
            continue
        
        #Set Parameters for the GA
        while True:
            params = getParameters()
            if (params == "Error" or params is None):
                print("Invalid parameter input, please try again.")
                
            
            break
        print(params)
        #Run Genetic Algorithm with input file and parameters
        print("Running Genetic Algorithm...")
        if (runGeneticAlgorithm(input, params) == "Error"):
            print("An error occurred while running the Genetic Algorithm.")
            return
        break

main()