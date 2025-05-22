class Dungeon:
  def __init__(self, name, danger_lvl, recommended_min_lvl, loot_qual):
    self.name = name
    self.danger = danger_lvl
    self.recommended = recommended_min_lvl
    self.loot = loot_qual

  def __repr__(self):
    return "This Dungeon is called {name} and will have enemies of Level {danger_lvl} and therefore a minimum Level recommendation of Level {minimum}. The loot quality is {quality}.".format(name = self.name, danger_lvl=self.danger, minimum=self.recommended, quality=self.loot)

class Hero:
  def __init__(self, name, lvl, hero_type, magic = False,  friendly = True):
    self.name = name
    self.lvl = lvl
    self.type = hero_type
    self.magic = magic
    self.friendly = friendly
    self.hp = self.lvl * 30

  def __repr__(self):
    description = "This hero is {name} and of Level {lvl} and is a {typ}. ".format(name=self.name, lvl=self.lvl, typ=self.type)
    if self.friendly is True:
      description += "This hero is of a friendly kind."
    else:
      description += "This hero is of a marcarbre kind."
    return description

  def attack(self, opponent):
    damage = self.lvl * 5
    opponent.hp -= damage
    if opponent.lvl >= self.lvl + 12:
      return "You obviously hadn't thought about the consequences of you actions. You merely damaged you enemy by {dmg} points. Brace yourself for imminent death!".format(dmg=damage)
    else:
      return "Our brave hero {name} managed to damage his enemy by {dmg} points. The enemy now only has {hp} left.".format(name=self.name, dmg=damage, hp=opponent.hp)

  def healing_self(self):
    heal = self.lvl * 3
    if self.magic is True:
      if self.hp + heal <= self.lvl * 30:
        self.hp += heal
        return "Since {hero} is capable in the arcane arts, he managed to heal himself by {heal} HP and he now has {hp} HP.".format(hero=self.name, heal=heal, hp=self.hp)
      else:
        self.hp = self.lvl * 30
        return "Since {hero} knows magic, he managed to restore himslef up to his maximum health. He now has {hp} HP.".format(hero=self.name, hp=self.hp)
    else:
      return "{hero} does not know magic and therefore cannot heal himself.".format(hero=self.name)

  def healing_friend(self, friend):
    heal = self.lvl * 3
    if self.magic is True:
      if friend.hp + heal <= friend.lvl * 30:
        friend.hp += heal
        return "Since {hero} knows magic, he managed to heal his friend {partner} by {heal} HP and {partner} now has {hp} HP.".format(hero=self.name, partner=friend.name, heal=heal, hp=friend.hp)
      else:
        friend.hp = friend.lvl * 30
        return "Since {hero} knows magic, he managed to restore his friend {partner} up to his maximum health. {partner} now has {hp} HP.".format(hero=self.name, partner=friend.name, hp=friend.hp)
    else:
      return "{hero} does not know magic and therefore cannot heal his trusted friend {partner}.".format(hero=self.name, partner=friend.name)

class Dragon:
  def __init__(self, dragon_type, lvl, dangerous = True):
    self.type = dragon_type
    self.lvl = lvl
    self.danger = dangerous
    self.hp = self.lvl * 50

  def __repr__(self):
    description = "This dragon is of a {typ} type and has a Level of {lvl}. ".format(typ=self.type, lvl=self.lvl)
    if self.danger == True:
      description += "This dragon is dangerous. Watch out!"
    else:
      description += "This dragon is friendly. Rather rare, so behave yourself."
    return description

  def attack(self, opponent):
    damage = self.lvl * -10
    if self.danger is True:
      opponent.hp += damage
      return "This {typ} dragon has done {dmg} damage to our brave lord and savior {hero}! Our hero now only has {hp} left.".format(typ=self.type, dmg=-damage, hero=opponent.name, hp=opponent.hp)
    else:
      return "This {typ} dragon only attacks in self defense.".format(typ=self.type)
    
  def speak(self):
    if self.danger is False:
      return "This {typ} dragon decided to spread his wisdom to the mere mortals that call themselves heros. For they do not know the way of their faults and neither do they desire to acquire about it themselves.".format(typ=self.type)
    else:
      return "This {typ} dragon is ferral and knows only to survive. This means to kill anything at all times!".format(typ=self.type)

icy_hole = Dungeon("Icy Hole", 1, 1, 1)
pirate_island = Dungeon("Pirate Island", 2, 1, 2)

ilphalir_the_wise = Hero("Ilphalir the Wise", 2, "Mage", True, False)
wummwumm = Hero("Wumm Wumm", 2, "Brute")

fire_dragon = Dragon("Fire", 1)
dragon_of_wisdom = Dragon("Etheral", 100, False)
"""
print(fire_dragon)
print(dragon_of_wisdom)

print(icy_hole)
print(pirate_island)

print(wlphalir_the_wise)
print(wummwumm)
"""
"""
damage_fireD = Dragon.attack(fire_dragon, ilphalir_the_wise)
print(damage_fireD)
damage_ethD = Dragon.attack(dragon_of_wisdom, wummwumm)
print(damage_ethD)

damage_il = Hero.attack(ilphalir_the_wise, fire_dragon)
print(damage_il)
damage_wummwumm = Hero.attack(wummwumm, dragon_of_wisdom)
print(damage_wummwumm)
"""
"""
healing_w = Hero.healing_friend(ilphalir_the_wise, wummwumm)
print(healing_w)
healing_self = Hero.healing_self(ilphalir_the_wise)
print(healing_self)
fail_heal_s = Hero.healing_self(wummwumm)
fail_heal_f = Hero.healing_friend(wummwumm, ilphalir_the_wise)
print(fail_heal_s)
print(fail_heal_f)
"""

speaking1 = Dragon.speak(dragon_of_wisdom)
speaking2 = Dragon.speak(fire_dragon)
print(speaking1)
print(speaking2)