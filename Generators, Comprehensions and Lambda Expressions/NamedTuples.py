from NamedTuplesData import basic_plants_list, plants_list

print(plants_list)

for plant in basic_plants_list:
    print(plant[0])  # or plant.name

print("=" * 20)

for plant in plants_list:
    print(plant.name, plant.scientific_name)  # or plant[0] and plant[1]

print()

example = plants_list[0]
print(example)
example = example._replace(lifecycle="Annual")
print(example)
