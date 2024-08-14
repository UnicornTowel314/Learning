import dnd_lists as dl
import random

gender = ["Female", "Male", "Nonbinary"]
random_character = []

def generate(list): #generate a random choice from each list in dnd_list and add choice to random_character list
    result = random.choice(list)
    random_character.append(result)
    return result

def generate_subclass(): #generate a random subclass based on the class that was picked and add class and subclass to random_character list
    dnd_class = generate(dl.dnd_classes)
    if dnd_class == "Artificer":
        generate(dl.dnd_subclasses[0])
    elif dnd_class == "Barbarian":
        generate(dl.dnd_subclasses[1])
    elif dnd_class == "Bard":
        generate(dl.dnd_subclasses[2])
    elif dnd_class == "Blood Hunter":
        generate(dl.dnd_subclasses[3])
    elif dnd_class == "Cleric":
        generate(dl.dnd_subclasses[4])
    elif dnd_class == "Druid":
        generate(dl.dnd_subclasses[5])
    elif dnd_class == "Fighter":
        generate(dl.dnd_subclasses[6])
    elif dnd_class == "Monk":
        generate(dl.dnd_subclasses[7])
    elif dnd_class == "Paladin":
        generate(dl.dnd_subclasses[8])
    elif dnd_class == "Ranger":
        generate(dl.dnd_subclasses[9])
    elif dnd_class == "Rogue":
        generate(dl.dnd_subclasses[10])
    elif dnd_class == "Sorcerer":
        generate(dl.dnd_subclasses[11])
    elif dnd_class == "Warlock":
        generate(dl.dnd_subclasses[12])
    elif dnd_class == "Wizard":
        generate(dl.dnd_subclasses[13])
    else:
        print("Error")

generate_character = input("Generate new character? (Y/N) ") #prompt user on whether they want to generate a character

while generate_character != "N": #allow user to continue to generate characters
    generate(gender)
    generate(dl.dnd_races)
    generate_subclass()
    print("Enjoy your new character! ")
    print("Gender: " + random_character[0])
    print("Race: " + random_character[1])
    print("Class: " + random_character[2])
    print("Subclass: " + random_character[3])
    random_character.clear()
    generate_character = input("Generate new character? (Y/N) ")