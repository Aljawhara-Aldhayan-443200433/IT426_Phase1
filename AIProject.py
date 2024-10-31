#imports
import random

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

    return round(fitness_value, 2)


#Create the Selection function (binary tournament selection)
def binary_tournament_selection(population, dressCodePref, colorPalattePref, comfortLevelPref, budgetPref):
    # Select two random parents from the population
    parentA = random.choice(population)
    parentB = random.choice(population)

    # Calculate fitness for each parent
    fitnessA = fitness_function(parentA, dressCodePref, colorPalattePref, comfortLevelPref, budgetPref)
    fitnessB = fitness_function(parentB, dressCodePref, colorPalattePref, comfortLevelPref, budgetPref)

    #################################code for testing fitness and selection

    def display_parent_info(parent, fitness_score, label):
        top, bottom, shoes, neck, purse = parent
        print(f"\n{label} Fitness Score: {fitness_score}")
        print(f"Top: {top[0]} ({top[2]}, {top[3]}, ${top[1]}, Comfort Level: {top[4]})")
        print(f"Bottom: {bottom[0]} ({bottom[2]}, {bottom[3]}, ${bottom[1]}, Comfort Level: {bottom[4]})")
        print(f"Shoes: {shoes[0]} ({shoes[2]}, {shoes[3]}, ${shoes[1]}, Comfort Level: {shoes[4]})")
        print(f"Neck: {neck[0]} ({neck[2]}, {neck[3]}, ${neck[1]}, Comfort Level: {neck[4]})")
        print(f"Purse: {purse[0]} ({purse[2]}, {purse[3]}, ${purse[1]}, Comfort Level: {purse[4]})")

    print("\nParents:")
    display_parent_info(parentA, fitnessA, "Parent A")
    display_parent_info(parentB, fitnessB, "Parent B")

    #################################End ofcode for testing fitness and selection

    # Select the parent with the higher fitness score
    if fitnessA > fitnessB:
        return parentA
    elif fitnessB > fitnessA:
        return parentB
    # If scores are equal, randomly select one of the parents
    else:
        return random.choice([parentA, parentB])




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

    #Create the initial population
    population = Create_Initial_Population(Top, Bottom, Shoes, Neck, Purse, 10)

    #Get the user input
    dressCodePref, colorPalattePref, comfortLevelPref, budgetPref = user_input()
    


     # Select a parent using binary tournament selection
    selectedParent = binary_tournament_selection(
        population, dressCodePref, colorPalattePref, comfortLevelPref, budgetPref
    )
    

# Print the selected parent 
print("\nWe are working on preparing your optimal outfit...")
print("\nYour outfit selection is ready! Here’s your personalized outfit plan :\n")

# Destructure the selected parent tuple
top, bottom, shoes, neck, purse = selectedParent

print(f"Top: {top[0]}")
print(f"Bottom: {bottom[0]}")
print(f"Shoes: {shoes[0]}")
print(f"Neck: {neck[0]}")
print(f"Purse: {purse[0]}")

print("\nHope you feel fabulous in your outfit!")

    
