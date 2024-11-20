#imports
import random
import matplotlib.pyplot as plt
#Search space
Top=[
    ["T-shirt",0.0,"Casual","Bright",5],
    ["Formal Shirt",120.0,"Business","Dark",3],
    ["Polo Shirt",80.0,"Sportswear","Bright",4],
    ["Evening Blouse",150.0,"Evening","Dark",3],
    ["Sweater",0.0,"Casual","Dark",5],
    ["Hoodie",60.0,"Casual","Bright",4],
    ["Tank Top",0.0,"Sportswear","Bright",4],
    ["Silk Blouse",200.0,"Evening","Dark",3]]

Bottom=[
    ["Jeans",0.0,"Casual","Dark",4],
    ["Formal Trousers",150.0,"Business","Dark",3],
    ["Sports Shorts",0.0,"Sportswear","Bright",5],
    ["Skirt",100.0,"Evening","Bright",3],
    ["Chinos",90.0,"Business","Dark",4],
    ["Leggings",60.0,"Casual","Dark",5],
    ["Athletic Pants",80.0,"Sportswear","Bright",5],
    ["Evening Gown Bottom",250.0,"Evening","Dark",1]
]

Shoes=[
    ["Sneakers",0.0,"Sportswear","Bright",5],
    ["Leather Shoes",180.0,"Business","Dark",2],
    ["Running Shoes",120.0,"Sportswear","Bright",5],
    ["Ballet Flats",90.0,"Casual","Dark",4],
    ["High Heels",250.0,"Evening","Dark",2],
    ["Sandals",0.0,"Casual","Bright",5],
    ["Loafers",150.0,"Business","Dark",3],
    ["Evening Pumps",220.0,"Evening","Bright",2]
]

Neck=[
    ["Silk Scarf",70.0,"Business","Dark",3],
    ["Sports Scarf",0.0,"Sportswear","Bright",4],
    ["Necklace",220.0,"Evening","Dark",3],
    ["Casual Scarf",0.0,"Casual","Bright",5],
    ["Bow Tie",80.0,"Evening","Dark",3],
    ["Athletic Headband",50.0,"Sportswear","Bright",5],
    ["Diamond Necklace",750.0,"Evening","Bright",3],
    ["Choker",0.0,"Evening","Dark",4]
]

Purse=[
    ["Clutch Bag",100.0,"Evening","Dark",3],
    ["Canvas Bag",0.0,"Casual","Bright",5],
    ["Leather Briefcase",180.0,"Business","Dark",1],
    ["Sports Backpack",80.0,"Sportswear","Bright",5],
    ["Tote Bag",0.0,"Casual","Bright",4],
    ["Wristlet",150.0,"Evening","Dark",3],
    ["Fanny Pack",50.0,"Sportswear","Bright",4],
    ["Elegant Handbag",250.0,"Evening","Dark",3]
]

#Create_Initial_Population() function
def Create_Initial_Population(Top,Bottom,Shoes,Neck,Purse,p):
    population=[]
    for _ in range(p):
        individual=(random.choice(Top),random.choice(Bottom),random.choice(Shoes),random.choice(Neck),random.choice(Purse))
        population.append(individual)
    return population


#Create the fitness function
# weights as constants
DRESS_CODE_WEIGHT = 0.3
COLOR_PALETTE_WEIGHT = 0.2
COMFORT_LEVEL_WEIGHT = 0.2
BUDGET_WEIGHT = 0.3


def fitness_function(individual , dressCodePref ,  colorPalattePref , comfortLevelPref , budgetPref ):

    top, bottom, shoes, neck, purse = individual

    # Initial fitness score = 0
    dressCodeMatch = 0
    colorPalatteMatch= 0
    comfortLevelMatch = 0
    budgetMatch = 0

#check if the individual match the prefered dress code (dressCodePref)
    dressCodeMatches = [
        int(top[2] == dressCodePref),
        int(bottom[2] == dressCodePref),
        int(shoes[2] == dressCodePref),
        int(neck[2] == dressCodePref),
        int(purse[2] == dressCodePref)
    ]
    dressCodeMatch = sum(dressCodeMatches) / 5
   

    # Total price of the indiviual to check budget
    totalPrice = top[1] + bottom[1] + shoes[1] + neck[1] + purse[1]

    #check if the individual match the prefered budget (budgetPref)
    if totalPrice <= budgetPref :
        budgetMatch = 1

    #check if the individual match the prefered color palatte (colorPalattePref)
    if top[3] == colorPalattePref and bottom[3] == colorPalattePref and shoes[3] == colorPalattePref and neck[3] == colorPalattePref and purse[3] == colorPalattePref:
        colorPalatteMatch =1

    colorPalatteMatches = [
        int(top[3] == colorPalattePref),
        int(bottom[3] == colorPalattePref),
        int(shoes[3] == colorPalattePref),
        int(neck[3] == colorPalattePref),
        int(purse[3] == colorPalattePref)
    ]
    colorPalatteMatch = sum(colorPalatteMatches) / 5 

    #Average comfort level of the individual to check if it>= comfortLevelPref
    avgComfortLevel = (top[4] + bottom[4] + shoes[4] + neck[4] + purse[4]) / 5
    
    if avgComfortLevel >= comfortLevelPref:
        comfortLevelMatch = 1

    #fiteness function formula
    fitness_value = ((DRESS_CODE_WEIGHT * dressCodeMatch) + (COLOR_PALETTE_WEIGHT * colorPalatteMatch) + (COMFORT_LEVEL_WEIGHT * comfortLevelMatch) + (BUDGET_WEIGHT * budgetMatch))

    return fitness_value


#Create the Selection function (binary tournament selection)
def binary_tournament_selection(population, dressCodePref, colorPalattePref, comfortLevelPref, budgetPref):
    # Select two random parents from the population
    parentA = random.choice(population)
    parentB = random.choice(population)

    # Calculate fitness for each parent
    fitnessA = fitness_function(parentA, dressCodePref, colorPalattePref, comfortLevelPref, budgetPref)
    fitnessB = fitness_function(parentB, dressCodePref, colorPalattePref, comfortLevelPref, budgetPref)



    # Select the parent with the higher fitness score
    if fitnessA > fitnessB:
        return parentA
    elif fitnessB > fitnessA:
        return parentB
    # If scores are equal, randomly select one of the parents
    else:
        return random.choice([parentA, parentB])


def Crossover(parent1, parent2):

    # Randomly select two crossover points
    point1, point2 = sorted(random.sample(range(len(parent1)), 2))

    # Create offspring by swapping segments between the crossover points
    offspring1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    offspring2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

    return offspring1, offspring2


# Mutation() function: Mutate the items within the individual randomly if the mutation_rate exceeds random.random() 
def Mutation(individual, mutation_rate):

    mutant=list(individual)
    itemLists=(Top,Bottom,Shoes,Neck,Purse)

    for eachGene in range(len(mutant)):
        if random.random() < mutation_rate:
                mutant[eachGene]= random.choice(itemLists[eachGene])

    mutant=tuple(mutant)
    return mutant


# Replacement(): Replace the old population with the new one(offspring)
def Replacement(population, offspring):
    
    return offspring


#Create Termination condition function
#Variable for tracking progress against meeting termination conditions
optimal_solution = 1.0 #best possible fitness value

def termination_condition(generation_counter, objective_function_value, optimal_solution):
    #measure how close the current fitness is to the optimal solution
    if abs(objective_function_value - optimal_solution) < 1e-8:
        return True
    #stop if the maximum number of generations has been reached (20000)
    elif generation_counter >= 20000:
        return True
    else:
        return False


#Get the user input 
def user_input():
    print("Welcome to PerfectFit! What is your name?")
    
    # get user name and ensure it's not empty
    name = input("> ")
    while len(name.strip()) == 0:
        print("Name cannot be empty, please enter your name.")
        name = input("> ")

    # get dress code preference and validate the input to ensure it is within the dress code list
    print(f"\nHi {name}! Please enter your dress code preference (Casual, Sportswear, Business, Evening):")
    dressCodePref = input("> ")
    while len(dressCodePref.strip()) == 0 or dressCodePref not in ['Casual', 'Sportswear', 'Business', 'Evening']:
        print("\nInvalid input, please enter a valid dress code preference: Casual, Sportswear, Business, Evening.")
        dressCodePref = input("> ")

    # get color palette preference and validate the input to ensure it is within the color palette list
    print("\nPlease enter your color palette preference (Dark, Bright):")
    colorPalattePref = input("> ")
    while len(colorPalattePref.strip()) == 0 or colorPalattePref not in ['Dark', 'Bright']:
        print('Invalid input, please enter a valid color palette preference: Dark or Bright.')
        colorPalattePref = input("> ")

    # get comfort level and validate the input to ensure it is within the comfort level range
    print("\nPlease enter your comfort level (1 (least comfortable) to 5 (most comfortable)): ")
    comfortLevelPref = input("> ")
    while len(comfortLevelPref.strip()) == 0 or not comfortLevelPref.isdigit() or not (1 <= int(comfortLevelPref) <= 5):
        print('Invalid input, please enter your comfort level in the range 1 to 5.')
        comfortLevelPref = input("> ")

    #get the user budget and check if it is a positive number
    print("\nPlease enter your budget (in SAR).")
    while True:
        budgetPref = input("> ").strip()
        if len(budgetPref) == 0:
            print("Budget cannot be empty, please enter a valid budget.")
            continue
        try:
            budgetPref = float(budgetPref)
            if budgetPref <= 0:
                print("Input must be a positive number, please enter a valid budget (in SAR).")
                continue
            break
        except ValueError:
            print("Invalid input, please enter a valid number.")

    return dressCodePref, colorPalattePref, int(comfortLevelPref), budgetPref


if __name__ == "__main__":
    # Get user input
    dressCodePref, colorPalattePref, comfortLevelPref, budgetPref = user_input()

    # Store the fitness progress of multiple GA runs for performance analysis
    all_fitness = []
    print("\nWe are working on preparing your optimal outfit...")

    for run in range(20):  # Run the GA 20 times
        population = Create_Initial_Population(Top, Bottom, Shoes, Neck, Purse, 10)
        # Variables for tracking progress against meeting termination conditions
        best_fitness = []  # To track fitness for each generation
        generation_counter = 0
        objective_function_value = 0 #highest fitness score found in the current generation

        # Run the GA until the termination condition is met
        while not termination_condition(generation_counter, objective_function_value, optimal_solution):
            # New generation
            offspring = []
            for _ in range(5):  # Since the population is fixed=10
                # Select parents using binary tournament selection
                parent1 = binary_tournament_selection(population, dressCodePref, colorPalattePref, comfortLevelPref, budgetPref)
                parent2 = binary_tournament_selection(population, dressCodePref, colorPalattePref, comfortLevelPref, budgetPref)
                # Perform crossover
                child1, child2 = Crossover(parent1, parent2)
                # Perform mutation on the offspring
                child1 = Mutation(child1, mutation_rate=0.1)
                child2 = Mutation(child2, mutation_rate=0.1)
                # Add offspring to the new generation
                offspring.extend([child1, child2])
            # Replace the old population with the new generation
            population = Replacement(population, offspring)
            # Evaluate the fitness scores
            fitness_scores = [fitness_function(ind, dressCodePref, colorPalattePref, comfortLevelPref, budgetPref) for ind in population]
            # Set the objective function value to the highest fitness score in the current population
            objective_function_value = max(fitness_scores)
            # Record the best fitness value of the current generation to track progress
            best_fitness.append(objective_function_value)
            # Increment the generation counter
            generation_counter += 1

        # Store the best fitness values for all generations of the current run in all_fitness.
        all_fitness.append(best_fitness)

    # Calculate average fitness across all runs for each generation
    # Determine the number of generations from the length of the first run
    num_generations = len(all_fitness[0])

    # List to store the average fitness for each generation
    average_fitness = []

    # Calculate the average fitness for each generation
    for gen_idx in range(num_generations):
        # Collect the fitness values for the current generation from all runs
        generation_values = [run[gen_idx] for run in all_fitness]
    
    # Calculate the average fitness for the current generation
    average = sum(generation_values) / len(generation_values)
    
    # Append the average fitness to the list
    average_fitness.append(average)

# Print the average fitness values for all generations
    print("Average fitness for each generation:", average_fitness)
    # Select the best outfit from the last generation
    selectedOutfit = population[fitness_scores.index(max(fitness_scores))]

    # Print the selected parent
    print("\nYour outfit selection is ready! Here’s your personalized outfit plan:\n")
    top, bottom, shoes, neck, purse = selectedOutfit
    print(f"Top: {top[0]}")
    print(f"Bottom: {bottom[0]}")
    print(f"Shoes: {shoes[0]}")
    print(f"Neck: {neck[0]}")
    print(f"Purse: {purse[0]}")
    print("\nHope you feel fabulous in your outfit!")

# Plot the performance graph without limiting the number of generations
plt.figure(figsize=(10, 6))  # For better visualization
plt.plot(
    range(0, len(average_fitness), 300),  # Plot every 100th generation on the x-axis
    average_fitness[::300],  # Use the fitness values corresponding to every 100th generation
    marker='D', linestyle='-', color='b'  # Diamond marker with a blue line
)
plt.title('GA Performance')  # Title of the graph
plt.xlabel('Generation')  # Label for the x-axis
plt.ylabel('Fitness')  # Label for the y-axis
plt.grid(axis='y', linestyle='-', color='gray')  # Display horizontal grid lines only
plt.show()  # Display the plot


