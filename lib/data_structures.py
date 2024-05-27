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
    food_names = []
    for i in spicy_foods:
        food_names.append(i['name'])
    return food_names


def get_spiciest_foods(spicy_foods):
    spicy_list = []
    for i in spicy_foods:
        if i['heat_level'] > 5:
            spicy_list.append(i)
    return spicy_list

def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        print(f"{i['name']} ({i['cuisine']}) | Heat Level: {'🌶'* i['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    #food_by_cuisine = []
    for i in spicy_foods:
        if i['cuisine'] == cuisine:
            return i       
            #food_by_cuisine.append(i)
    #return food_by_cuisine

def print_spiciest_foods(spicy_foods):
    for i in spicy_foods:
        if i['heat_level']>5:
            print(f"{i['name']} ({i['cuisine']}) | Heat Level: {'🌶'* i['heat_level']}")

def get_average_heat_level(spicy_foods):
    spice_total = 0
    for i in spicy_foods:
        spice_total += i['heat_level']
    return spice_total / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    # spicy_foods= spicy_foods.append(spicy_food)
    spicy_foods.append(spicy_food)
    return spicy_foods


print(get_names(spicy_foods))
print(get_spiciest_foods(spicy_foods))
print_spiciest_foods(spicy_foods)
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))
print(print_spiciest_foods(spicy_foods))