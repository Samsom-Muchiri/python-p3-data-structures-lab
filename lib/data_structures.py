spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    foodNames = []
    for name in spicy_foods:
        name = name["name"]
        foodNames.append(name)
    return foodNames
def get_spiciest_foods(spicy_foods):
    newList = []
    for temp in spicy_foods:
        if temp["heat_level"] > 5:
            newList.append(temp)
    return newList

def print_spicy_foods(spicy_foods):
    for spicy in spicy_foods:
        food_name = spicy["name"]
        cuisine = spicy["cuisine"]
        heat = spicy["heat_level"]
        print(f"{food_name} ({cuisine}) | Heat Level: {'🌶' * heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
     for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
            return spicy_food
     return None

def print_spiciest_foods(spicy_foods):
    for spicy in spicy_foods:
        if spicy["heat_level"] > 5:
            food_name = spicy["name"]
            cuisine = spicy["cuisine"]
            heat = spicy["heat_level"]
            print(f"{food_name} ({cuisine}) | Heat Level: {'🌶' * heat}")

def average_heat_level(spicy_foods):
    total_heat = 0
    num_spicy_foods = len(spicy_foods)

    if num_spicy_foods == 0:
        return 0  

    for spicy_food in spicy_foods:
        total_heat += spicy_food["heat_level"]

    average = total_heat / num_spicy_foods
    return int(average)
    

def create_spicy_food(spicy_foods, new_spicy_food):
    new_list = spicy_foods.copy()
    new_list.append(new_spicy_food)
    return new_list

new_spicy_food = {
    "name": "Griot",
    "cuisine": "Haitian",
    "heat_level": 10,
}

updated_spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)

# Print the updated list
for spicy_food in updated_spicy_foods:
    print(spicy_food)

