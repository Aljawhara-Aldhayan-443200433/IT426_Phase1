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
    if top[2] == dressCodePref and bottom[2] == dressCodePref and shoes[2] == dressCodePref and neck[2] == dressCodePref and purse[2] == dressCodePref:
        dressCodeMatch = 1

    # Total price of the indiviual to check budget
    totalPrice = top[1] + bottom[1] + shoes[1] + neck[1] + purse[1]

    #check if the individual match the prefered budget (budgetPref)
    if totalPrice <= budgetPref :
        budgetMatch = 1

    #check if the individual match the prefered color palatte (colorPalattePref)
    if top[3] == colorPalattePref and bottom[3] == colorPalattePref and shoes[3] == colorPalattePref and neck[3] == colorPalattePref and purse[3] == colorPalattePref:
        colorPalatteMatch =1

    #Average comfort level of the individual to check if it>= comfortLevelPref
    avgComfortLevel = (top[4] + bottom[4] + shoes[4] + neck[4] + purse[4]) / 5
    
    if avgComfortLevel >= comfortLevelPref:
        comfortLevelMatch = 1

    #fiteness function formula
    fitness_value = ((DRESS_CODE_WEIGHT * dressCodeMatch) + (COLOR_PALETTE_WEIGHT * colorPalatteMatch) + (COMFORT_LEVEL_WEIGHT * comfortLevelMatch) + (BUDGET_WEIGHT * budgetMatch))

    return fitness_value


#Create the Selectio function





#Get the user input 
def user_input():
    print("Welcome to PerfectFit! What is your name?")
    name = input("> ")
    
    print(f"\nHi {name}! Please enter your dress code preference (Casual, Sportswear, Business, Evening):")
    dressCodePref = input("> ")
    
    print("\nPlease enter your color palette preference (Dark, Bright):")
    colorPalattePref = input("> ")
    
    print("\nPlease enter your comfort level (1 (least comfortable) to 5 (most comfortable)): ")
    comfortLevelPref = int(input("> "))
    
    print("\nPlease enter your budget (in SAR).")
    budgetPref = float(input("> "))
    
    return dressCodePref, colorPalattePref, comfortLevelPref, budgetPref


#if __name__ == "__main__":

    #Create the initial population
    population = Create_Initial_Population(Top, Bottom, Shoes, Neck, Purse, random.randint(5, 100))

    #Get the user input
    dressCodePref, colorPalattePref, comfortLevelPref, budgetPref = user_input()
    
    #Evaluate fitness for each individual in the population
    fitness_scores = []
    for individual in population:
        fitness_score = fitness_function(individual, dressCodePref, colorPalattePref, comfortLevelPref, budgetPref)
        fitness_scores.append(fitness_score)
