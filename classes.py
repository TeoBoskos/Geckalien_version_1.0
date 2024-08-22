# I am not sure yet if I want to use this.

class Enemy:
  def __init__(self, name: str, description: str, health: int, damage: int, width: int, height: int, shield: int):
    self.name = name
    self.description = description
    self.health = health
    self.damage = damage
    self.width = width
    self.height = height

  def read_discription(self):
    print(self.description)


regular_enemy = Enemy(
  "Infantry man",
  "A regular soldier. Has low health and causes little damage.",
  35,
  5,
  40,
  60,
  0
)

regular_enemy.read_discription()


class Weapon:
  def __init__(self, name: str, description: str, damage: int, cost: int):
    self.name = name
    self.description = description
    self.damage = damage
    self.cost = cost

  def read_description(self):
    print(self.description)


pistol = Weapon(
  "Pistol",
  "The default weapon. Strong enough to keep you alive in the beginning of your adventure.",
  10,
  0
)

pistol.read_description()