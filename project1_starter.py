"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Arielle Gerald
Date: 10/23/2025

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    level = 1
    strength, magic, health = calculate_stats(character_class, level)

    if character_class.lower() == "warrior":
        gold = 120
    elif character_class.lower() == "mage":
        gold = 90
    elif character_class.lower() == "rogue":
        gold = 110
    elif character_class.lower() == "cleric":
        gold = 100
    else:
        gold = 100

    character = {}
    character["name"] = name
    character["class"] = character_class
    character["level"] = level
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] = gold

    return character



"""
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
"""
 
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation


def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    if character_class.lower() == "warrior":
        strength = 12 + (4 * level)
        magic = 3 + (1 * level)
        health = 140 + (20 * level) 

    elif character_class.lower() == "mage":
        strength = 4 + (1 * level)
        magic = 14 + (5 * level)
        health = 90 + (12 * level)

    elif character_class.lower() == "rogue":
        strength = 8 + (3 * level)
        magic = 6 + (2 * level)
        health = 100 + (15 * level) 

    elif character_class.lower() == "cleric":
        strength = 6 + (2 * level)
        magic = 11 + (3 * level)
        health = 120 + (18 * level) 

    else:
        strength = 7 + (2 * level)
        magic = 7 + (2 * level)
        health = 100 + (15 * level)

    return strength, magic, health
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    

def save_character(character, filename):
    file = open (filename, "w")
    file.write("Name: " + character[0] + "\n")
    file.write("Class: " + character[1] + "\n")
    file.write("Level: " + str(character[2]) + "\n")
    file.write("Strength: " + str(character[3]) + "\n")
    file.write("Magic: " + str(character[4]) + "\n")
    file.write("Health: " + str(character[5]) + "\n")
    file.write("Gold: " + str(character[6]) + "\n")
    file.close()    
    return True
    
"""
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully


def load_character(filename):
    file = open (filename, "r")
    lines = file.readlines()
    file.close()

    if len(lines) < 7:
        print("File data is incomplete.")
        return None
    
    name = lines[0].split(": ")[1].strip()
    character_class = lines[1].split(": ")[1].strip()
    level = int(lines[2].split(": ")[1].strip())
    strength = int(lines[3].split(": ")[1].strip()) 
    magic = int(lines[4].split(": ")[1].strip())    
    health = int(lines[5].split(": ")[1].strip())   
    gold = int(lines[6].split(": ")[1].strip()) 

    character = [name, character_class, level, strength, magic, health, gold]
    return character
"""
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors 


def display_character(character):
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("========================\n")
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    


def level_up(character):
    character[2] += character[2] + 1    
    strength, magic, health = calculate_stats(character[1], character[2])
    character[3] = strength
    character[4] = magic
    character[5] = health
    print(character[0] + " has leveled up to level " + str(character[2]) + "!")
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    


# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")

    hero = create_character("Lyra the Swift", "Rogue")
    display_character(hero)

    sucess = save_character(hero, "lyra.txt")
    if sucess == True:
        print("Character saved successfully!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
