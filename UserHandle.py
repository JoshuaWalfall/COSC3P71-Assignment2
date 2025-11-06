
from tkinter import Tk
from tkinter.filedialog import askopenfilename
def getFile():
    filePath = askopenfilename(
    title="Select input file",
    filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    content = ""
    print("Reading: " + filePath)
    try:
        file = open(filePath, "r")
        content = file.read()
        file.close()
    except Exception as e:
        print("Error reading file:", e)
        return "Error"
    
    input = content.splitlines()
    output = dict()
    #print (len(input))
    #print(input)
    
    if len(input) < 2:
        return "Error"
    elif input[0] == '26':
        output["size"] = 26
        output["key"] = "".join(input[1:])
    elif input[0] == '40':
        output["size"] = 40
        output["key"] = "".join(input[1:])
    else:
        return "Error"
    #print(output)
    return output

def getParameters():
    print("Please enter the following parameters for the Genetic Algorithm:")
    try:
        populationSize = int(input("Population Size (e.g., 100): "))
        mutationRate = float(input("Mutation Rate (e.g., 0.01): "))
        crossoverRate = float(input("Crossover Rate (e.g., 0.7): "))
        generations = int(input("Number of Generations (e.g., 1000): "))
    except ValueError:
        return "Error"
    
    if populationSize <= 0 or not (0 <= mutationRate <= 1) or not (0 <= crossoverRate <= 1) or generations <= 0:
        return "Error"
    
    params = {
        "populationSize": populationSize,
        "mutationRate": mutationRate,
        "crossoverRate": crossoverRate,
        "generations": generations
    }
    return params
