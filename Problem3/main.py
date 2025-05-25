from Food import Food
from Restaurant import Restaurant


food1 = Food(1, 'Pizza', 3000)
food2 = Food(2, 'Hamburger', 3700)
food3 = Food(3, 'Gyros', 4200)

restaurant = Restaurant('Teszt étterem', [food1, food2])
restaurant + food3

print(restaurant.food)
