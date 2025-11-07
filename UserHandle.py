
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
def selectFile(filePath):
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
        crossoverSelect = int(input("Crossover Selection Method (0: Uniform, 1: Custom): "))
        generations = int(input("Number of Generations (e.g., 1000): "))
        #chromosomeSize = int(input("Chromosome Size (e.g., 40): "))
        elitism = int(input("Elitism Count (e.g., 2): "))
    except ValueError:
        return "Error"
    
    if populationSize <= 0 or not (0 <= mutationRate <= 1) or not (0 <= crossoverRate <= 1) or generations <= 0 or crossoverSelect not in [0, 1]:# or chromosomeSize <= 0:
        return "Error"
    
    params = {
        "populationSize": populationSize,
        "mutationRate": mutationRate,
        "crossoverRate": crossoverRate,
        "crossoverSelect": crossoverSelect,
        "generations": generations,
        #"chromosomeSize": chromosomeSize,
        "elitism": elitism
    }
    return params

def writeFile(data):
    filePath = input("Enter output file path: ") + ".txt"
    
    try:
        file = open(filePath, "w")
    except Exception as e:
        print("Error writing file:", e)
    
    file.write("Generation Data:\n")
    file.write("Generation    Average Fitness    Best Fitness\n")
    
    for i in range(len(data["averageFitness"])):
        file.write(str(i) + "    " + str(data['averageFitness'][i]) + "    " + str(data['bestFitness'][i]) + "\n")

    file.write("\nBest Solution: " + str(data["sortedResults"][0][0]) + "\n")
    file.write("Decrypted Text: \n")
    file.write(str(data["solution"]))

    file.write ("\nSorted Solutions:\n")
    file.write ("Solution    Fitness\n")
    for i in range (len(data["sortedResults"])):
        file.write(str(data["sortedResults"][i][0]) + "    " + str(data["sortedResults"][i][1]) + "\n")

    file.close()
        
def writeAnalysisFile(data, filePath):
    try:
        file = open(filePath, "w")
    except Exception as e:
        print("Error writing file:", e)
    
    file.write("Params:\n")
    file.write( str(data[0]["params"]) + "\n\n")

    file.write("Generation Data:\n")
    file.write("Generation  " + len(data)*" Average Fitness    Best Fitness" + "\n")

    for i in range(len(data[0]["averageFitness"])):
        file.write(str(i))
        for j in range(len(data)):
            file.write ("  " + str(data[j]['averageFitness'][i]) + "    " + str(data[j]['bestFitness'][i]))
        file.write("\n")

    file.close()
def writeSelectFile(data, filePath):
    try:
        file = open(filePath, "w")
    except Exception as e:
        print("Error writing file:", e)
    
    file.write("Params:\n")
    file.write( str(data["params"]) + "\n\n")

    file.write("Generation Data:\n")
    file.write("Generation    Average Fitness    Best Fitness\n")
    
    for i in range(len(data["averageFitness"])):
        file.write(str(i) + "    " + str(data['averageFitness'][i]) + "    " + str(data['bestFitness'][i]) + "\n")

    file.write("\nBest Solution: " + str(data["sortedResults"][0][0]) + "\n")
    file.write("Decrypted Text: \n")
    file.write(str(data["solution"]))

    file.write ("\nSorted Solutions:\n")
    file.write ("Solution    Fitness\n")
    for i in range (len(data["sortedResults"])):
        file.write(str(data["sortedResults"][i][0]) + "    " + str(data["sortedResults"][i][1]) + "\n")

    file.close()