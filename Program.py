from Evaluation import * 
from UserHandle import getFile, getParameters, writeFile, selectFile, writeSelectFile, writeAnalysisFile
from GA import GeneticAlgorithm, Chromosome

def main():
    while True:
        text = input("Press any key to run Genetic Algorithm, type 'exit' to quit: ")
        if text == "exit":
            break
        #Select File and read it, checking if it's a valid input
        userInput = getFile()
        if (userInput == "Error"):
            print("Invalid file input, please try again.")
            continue
        
        #Set Parameters for the GA
        while True:
            params = getParameters()
            if (params == "Error" or params is None):
                print("Invalid parameter input, please try again.")
                
            break
        #Run Genetic Algorithm with input file and parameters
        params["chromosomeSize"] = userInput["size"]
        print("Running Genetic Algorithm with provided input and parameters...")
        print(params)
        ga = GeneticAlgorithm(userInput["key"], params)

        result = ga.run()
        if (result == "Error"):
            print("An error occurred while running the Genetic Algorithm.")
            return
        writeFile(result)

def analysis():
    data1 = selectFile("C:/Users/joshu/OneDrive/Documents/University/Year 5/COSC 3P71/Assignments/Assign2_Attachments/Assign2_Attachments/Data1.txt")
    data2 = selectFile("C:/Users/joshu/OneDrive/Documents/University/Year 5/COSC 3P71/Assignments/Assign2_Attachments/Assign2_Attachments/Data2.txt")
    if (data1 == "Error" or data2 == "Error"):
        print("Error reading files for analysis.")
        return
    tests = [
        {"test": "a","params": {"populationSize": 100, "mutationRate": 0.0, "crossoverRate": 1.0, "crossoverSelect":2, "generations": 100, "chromosomeSize": 0, "elitism": 2}},
        {"test": "b","params": {"populationSize": 100, "mutationRate": 0.1, "crossoverRate": 1.0, "crossoverSelect":2, "generations": 100, "chromosomeSize": 0, "elitism": 2}},
        {"test": "c","params": {"populationSize": 100, "mutationRate": 0.0, "crossoverRate": 0.9, "crossoverSelect":2, "generations": 100, "chromosomeSize": 0, "elitism": 2}},
        {"test": "d","params": {"populationSize": 100, "mutationRate": 0.1, "crossoverRate": 0.9, "crossoverSelect":2, "generations": 100, "chromosomeSize": 0, "elitism": 2}},
        {"test": "e","params": {"populationSize": 100, "mutationRate": 0.1, "crossoverRate": 0.95, "crossoverSelect":2, "generations": 100, "chromosomeSize": 0, "elitism": 2}}
    ]
    
    for i in range (len(tests)):
        analysisOutput1 = []
        analysisOutput2 = []
        print ("Starting Test " + tests[i]["test"])
        for j in range (10):
            params = tests[i]["params"]
            if (j < 5): 
                params["chromosomeSize"] = data1["size"]
                dataToUse = data1["key"]
            else:
                params["chromosomeSize"] = data2["size"]
                dataToUse = data2["key"]
            first = params
            first["crossoverSelect"] = 0
            second = params
            second["crossoverSelect"] = 1

            print("Running Genetic Algorithm with Uniform: " + str(first))
            ga1 = GeneticAlgorithm(dataToUse, first)
            ga1.verbose = 0
            result1 = ga1.run()
            writeSelectFile(result1, tests[i]["test"] + "-uniform-test" + str(j) + ".txt")
                
            print("Running Genetic Algorithm with Custom: " + str(second))
            ga2 = GeneticAlgorithm(dataToUse, second)
            ga2.verbose = 0
            result2 = ga2.run()
            writeSelectFile(result2, tests[i]["test"] + "-custom-test" + str(j) + ".txt")
            analysisOutput1.append(result1)
            analysisOutput2.append(result2)
        writeAnalysisFile(analysisOutput1, tests[i]["test"] + "-uniform-analysis.txt")
        writeAnalysisFile(analysisOutput2, tests[i]["test"] + "-custom-analysis.txt")


def test():
    ga = GeneticAlgorithm(
        "xbwdesmhihslwhkktefvktkktcwfpiibihwmosfilojvooegvefwnochsuuspsureifakbnlalzsrsroiejwzgfpjczldokrceoahzshpbdwpcjstacgbarfwifwohylckafckzwwomlalghrtafchfetcgfpfrgxclwzocdctmjebx", 
        {"populationSize": 100, "mutationRate": 0.1, "crossoverRate": 0.9, "crossoverSelect":1, "generations": 5, "chromosomeSize": 5, "elitism": 2}
        )
    #result = ga.run()
    #writeFile(result)

    test1 = Chromosome(['h', 'e', 'l', 'l', 'o'])
    test2 = Chromosome(['w', 'o', 'r', 'l', 'd'])
    print (ga.crossover([test1, test2]))

#test()
#main()
#analysis()