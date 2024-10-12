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

