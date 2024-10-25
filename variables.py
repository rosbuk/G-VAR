# Vegetable
veg_name = 'melon'
veg_weight = 3.5
veg_quant = 4
veg_ripe = False

# Meal
meal_name = 'fryed eggs'
meal_calories = 750
meal_weight = 0.2
meal_square = True

# Colleague
colleague_name = 'Venera'
colleague_age = 24
colleague_weight = 55.5
colleague_male = False

# Toy
toy_name = 'Teddy'
toy_color = 9990461
toy_smile = False
toy_velocity = 0.1

vars = [veg_name, veg_weight, veg_quant, veg_ripe, 
        meal_name, meal_calories, meal_weight, meal_square, 
        colleague_name, colleague_age, colleague_weight, colleague_male, 
        toy_name, toy_color, toy_smile, toy_velocity,
        ]

for var in vars:
    print(type(var))


