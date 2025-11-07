import random
import copy
from Evaluation import Evaluation
class Chromosome:
    def __init__(self):
        # Placeholder for chromosome initialization
        self.genes = []
    def __init__(self, genes):
        self.genes = genes
    def __str__(self):
        return "".join(self.genes)
    __repr__ = __str__



class GeneticAlgorithm:
    
    def __init__(self, input, params):
        #Read Program Instance Data
        #Set the GA Parameters
        self.popSize = params["populationSize"]
        self.mutationRate = params["mutationRate"]
        self.crossoverRate = params["crossoverRate"]
        self.crossoverSelect = params["crossoverSelect"]
        self.maxGen = params["generations"]
        self.chromSize = params["chromosomeSize"]
        self.elitism = params["elitism"]
        self.text = input
        self.verbose = 1 #Optional Variable that can be tweaked for more detailed output during execution
        
    def run(self):
        #Generate random initial population
        population = self.popInit(self.popSize, self.chromSize)
        #population[0].genes = ['p', 'a', 's', 's', 'w', 'o', 'r', 'd'] + ["-"]*32  # For testing purposes
        #population = self.popInitV2(self.popSize, self.chromSize)
        if (self.verbose == 1):   
            print ("Initial Population Created")
        #print (population)

        data = {"averageFitness": [], "bestFitness": [], 'sortedResults': [], "solution": ""}
    
        for x in range(self.maxGen):
            if (self.verbose == 1):
                print("Generation " + str(x))
            #Evaluate the fitness of every chromosome in the population
            fitness = []
            for i in range(len(population)):
                #print("Evaluating Chromosome " + str(population[i]) + " of Generation " + str(x))
                fitness.append(Evaluation.fitness(str(population[i]), self.text))

            if (self.verbose == 2):
                print("Initial Generation:")
                self.printPopulation(population)
            #Select the new pop
            parents = self.selection(population, fitness, 3)
            if (self.verbose == 2):
                print("Pre Crossover:")
                self.printPopulation(parents)

            #Apply Crossover
            newPopulation = self.crossover(parents)
            if (self.verbose == 2):
                print("Post Crossover:")
                self.printPopulation(newPopulation)
            
            #Apply Mutation
            newPopulation = self.mutation(newPopulation)
            if (self.verbose == 2):
                print("Post Mutation:")
                self.printPopulation(newPopulation)

            elite = self.getElite(population, fitness, self.elitism)
            if (self.verbose == 2):
                print("Elite:")
                self.printPopulation(elite)

            population = newPopulation + elite
            

            #Report
            data["bestFitness"].append(min(fitness))
            data["averageFitness"].append(sum(fitness)/len(fitness))
        print("GA Complete")
        
        
        data["sortedResults"] = sorted(zip(population, fitness), key=lambda x: x[1])
        data["solution"] = Evaluation.decrypt(str(data["sortedResults"][0][0]), self.text)

        data["params"] = {
            "populationSize": self.popSize,
            "mutationRate": self.mutationRate,
            "crossoverRate": self.crossoverRate,
            "crossoverSelect": self.crossoverSelect,
            "generations": self.maxGen,
            "chromosomeSize": self.chromSize,
            "elitism": self.elitism
        }

        return data
        
    def popInit(self, popSize, chromSize):
        createPop = []
        for i in range(popSize):
            #Create a random chromosome
            genes = []
            for j in range(chromSize):
                temp = random.randint(96, 122) # Random lowercase letter, with 96 as a placeholder for space
                if temp == 96:
                    temp = 45
                genes.append(chr(temp))
                  
            createPop.append(Chromosome(genes))
        return createPop
    def popInitV2(self, popSize, chromSize):
        createPop = []
        for i in range(popSize):
            #Create a random chromosome
            genes = []
            for j in range(chromSize):
                if random.randint(0,1) == 0:
                    temp = 45  # Placeholder for space
                else:
                    temp = random.randint(97, 122) # Random lowercase letter
                genes.append(chr(temp))
                  
            createPop.append(Chromosome(genes))
        return createPop

    #Runs thorugh a population, and applies tournament selection to select parents for the next generation
    def selection(self, population, fitness, k):
        selected = []
        
        for i in range (int(len(population)) - self.elitism):
            #Select k random individuals for the tournament
            tournament = random.sample(list(zip(population, fitness)), k)
            #Select the best individual from the tournament
            tournament.sort(key=lambda x: x[1])  # Sort by fitness
            selected.append(tournament[0][0])  # Append the best chromosome

        return selected
    
    def getElite(self, population, fitness, e):
        #Find the best chromosome in the population
        bestList = list(zip(population, fitness))
        bestList.sort(key=lambda x: x[1])
        return [x[0] for x in bestList[:e]]
    
    def crossover(self, oldPop):    
        if (self.crossoverSelect == 1):
            return self.customCrossover(oldPop)
        return self.uniformCrossover(oldPop)
        
    def uniformCrossover(self, oldPop):
        newPop = []
        for i in range(0, len(oldPop), 2):
            
            if i + 1 >= len (oldPop):
                newPop.append(oldPop[i])
            elif random.random() < self.crossoverRate:
                child1 = Chromosome([])
                child2 = Chromosome([])
                #print("Crossover between " + str(oldPop[i]) + " and " + str(oldPop[i + 1]))
                for j in range (self.chromSize):
                    if random.randint(0,1) == 1:
                        child1.genes.append(oldPop[i].genes[j])
                        child2.genes.append(oldPop[i + 1].genes[j])
                    else:   
                        child1.genes.append(oldPop[i + 1].genes[j])
                        child2.genes.append(oldPop[i].genes[j])
                newPop.append(child1)
                newPop.append(child2)
                #print("Produced children " + str(child1) + " and " + str(child2))
            else: 
                newPop.append(oldPop[i])
                newPop.append(oldPop[i + 1])
        return newPop

    def customCrossover(self, oldPop):
        newPop = []
        for i in range(0, len(oldPop), 2):
            if i + 1 >= len (oldPop):
                newPop.append(oldPop[i])
            elif random.random() < self.crossoverRate:
                child1 = Chromosome([])
                child2 = Chromosome([])
                #print("Crossover between " + str(oldPop[i]) + " and " + str(oldPop[i + 1]))
                randomPoint = random.randint(1, self.chromSize - 1)
                #print("Crossover Point at " + str(randomPoint))
                for j in range (self.chromSize):

                    if j >= randomPoint:
                        child1.genes.append(oldPop[i + 1].genes[j])
                        child2.genes.append(oldPop[i].genes[j])
                    else:   
                        child1.genes.append(oldPop[i].genes[j])
                        child2.genes.append(oldPop[i + 1].genes[j])
                newPop.append(child1)
                newPop.append(child2)
                #print("Produced children " + str(child1) + " and " + str(child2))
            else: 
                newPop.append(oldPop[i])
                newPop.append(oldPop[i + 1])
        return newPop
    #Reciprocal Exchange Mutation
    def mutation(self, oldPop):
        newPop = []
        for i in range (len(oldPop)):
            mutated = copy.deepcopy(oldPop[i])
            if (random.random() < self.mutationRate):
                #Select two random points in the chromosome
                point1 = random.randint(0, self.chromSize - 1)
                point2 = random.randint(0, self.chromSize - 1)
                #Swap the genes at the two points
                temp = oldPop[i].genes[point1]
                mutated.genes[point1] = oldPop[i].genes[point2]
                mutated.genes[point2] = temp
            newPop.append(mutated)
            #print("Mutated " + str(oldPop[i]) + " to " + str(mutated))
        return newPop

    def printPopulation(self, population):
        for i in range(len(population)):
            print(str(i) + ": " + str(population[i]) + " Fitness: " + str(Evaluation.fitness(str(population[i]), self.text)))
        print ("")
#test = 'a'
#print(ord (test))
#print(test == chr(97))
