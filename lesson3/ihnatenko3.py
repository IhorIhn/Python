#Task 1

alice_in_wonderland = """\
"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
"""

#Task 2

count = alice_in_wonderland.count("'")
print("Кількість одинарних лапок:", count)

#Task 3

print(alice_in_wonderland)

#Task 4

Black_sea_territory = 436402
Azov_sea_territory = 37800

print("Площа двох морів:", Black_sea_territory + Azov_sea_territory, "км²")

#Task 5


total_all = 375_291
first_plus_second = 250_449
second_plus_third = 222_950

second = (first_plus_second + second_plus_third) - total_all
first = first_plus_second - second
third = second_plus_third - second

print("Товари на першому складі:", first)
print("Товари на другому складі:", second)
print("Товари на третьому складі:", third)

#task 6

months = 18
price_per_month = 1179

print("Вартість комп'ютера: ", months * price_per_month)

#Task 7

print("a)", 8019 % 8)
print("b)", 9907 % 9)
print("c)", 2789 % 5)
print("d)", 7248 % 6)
print("e)", 7128 % 5)
print("f)", 19224 % 9)

#Task 8

pizza_large = 4 * 274
pizza_medium = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21

total = pizza_large + pizza_medium + juice + cake + water

print("Загальна сума замовлення:", total, "грн")

#task 9

photos = 232
photos_per_page = 8

pages = (photos + photos_per_page - 1) // photos_per_page

print("Потрібно сторінок:", pages)

#Task 10

distance = 1600
fuel_per_100km = 9
tank_capacity = 48

total_fuel = (distance / 100) * fuel_per_100km

refills = int(total_fuel // tank_capacity)
if total_fuel % tank_capacity != 0:
    refills += 1

print("Потрібно бензину:", total_fuel, "літрів")
print("Кількість заправок:", refills)
