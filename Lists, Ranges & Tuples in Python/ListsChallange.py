# add to the program below so that if it finds a meal without spam
# it prints each of the ingredients of the meal.

menu = []

menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

print(menu)

for meal in menu:
    if "spam" not in meal:
        for ingredient in meal:
            print(ingredient)