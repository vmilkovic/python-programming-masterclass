from Player import Player
from Enemy import Enemy, Troll, Vampire, VampireKing

tim = Player("Tim")

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll, end=""))
another_troll.take_damage(18)
print(another_troll)

brother_troll = Troll("Urg")
print("Brother troll - {}".format(brother_troll))

ugly_troll.grunt()
another_troll.grunt()
brother_troll.grunt()

vamp = Vampire("Vlad")
print(vamp)
vamp.take_damage(5)
print(vamp)

print("-" * 40)
another_troll.take_damage(30)
print(another_troll)

# while vamp._alive:
#     vamp.take_damage(1)
#     print(vamp)

vamp._lives = 0
vamp._hit_points = 1
print(vamp)

dracula = VampireKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)
