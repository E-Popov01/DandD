import random

class Dungeon:
  def __init__(self, name, difficulty, recommended_min_lvl, loot_qual):
    self.name = name
    self.difficulty = difficulty
    self.recommended = recommended_min_lvl
    self.loot = loot_qual

  def __repr__(self):
    return "This Dungeon is called {name} and will have enemies of Level {difficulty} and therefore a minimum Level recommendation of Level {minimum}. The loot quality is {quality}.".format(name = self.name, difficulty=self.difficulty, minimum=self.recommended, quality=self.loot)

class Hero:
  def __init__(self, name, lvl, hero_type, magic,  friendly):
    self.name = name
    self.lvl = lvl
    self.type = hero_type
    self.magic = magic
    self.friendly = friendly

    self.hp = self.lvl * 30
    self.strength = 0
    self.dexterity = 0
    self.constitution = 0
    self.intelligence = 0
    self.wisdom = 0
    self.charisma = 0

    if self.type == "Warrior" or self.type == "Fighter":
      self.strength = 16
      self.dexterity = 9
      self.constitution = 15
      self.intelligence = 13
      self.wisdom = 11
      self.charisma = 14
    elif self.type == "Mage" or self.type == "Sorcerer":
      self.strength = 10
      self.dexterity = 16
      self.constitution = 12
      self.intelligence = 16
      self.wisdom = 13
      self.charisma = 8
    elif self.type == "Rogue" or self.type == "Thief":
      self.strength = 8
      self.dexterity = 16
      self.constitution = 10
      self.intelligence = 13
      self.wisdom = 12
      self.charisma = 16
    elif self.type == "Cleric" or self.type == "Priest":
      self.strength = 16
      self.dexterity = 8
      self.constitution = 13
      self.intelligence = 10
      self.wisdom = 16
      self.charisma = 12

  def __repr__(self):
    description = "This level {lvl} hero is {name} and he/she is a {typ}. ".format(name=self.name, lvl=self.lvl, typ=self.type)
    if self.friendly is True:
      description += "This hero is of a friendly kind."
    else:
      description += "This hero is of a macabre kind."
    description += " \n This hero's starting stats are: HP: {hp}, \n Strength: {str}, \n Dexterity: {dex}, \n Constitution: {con}, \n Intelligence: {int}, \n Wisdom: {wis}, \n Charisma: {cha}.".format(hp=self.hp, str=self.strength, dex=self.dexterity, con=self.constitution, int=self.intelligence, wis=self.wisdom, cha=self.charisma)
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

def create_hero():
  name = input("What is the name of the hero? ")
  lvl = 1
  hero_type = input("What is the type of the hero? You can choose between: Warrior, Mage, Rogue and Cleric. ")
  if hero_type == "Mage" or hero_type == "Sorcerer" or hero_type == "Cleric" or hero_type == "Priest":
    magic = True
  else:
    magic = False
  
  friendly = input("Is this hero friendly? (yes/no) ")
  if friendly.lower() == "yes" or friendly.lower() == "y":
    friendly = True
  elif friendly.lower() == "no" or friendly.lower() == "n":
    friendly = False

  return Hero(name, lvl, hero_type, magic, friendly)

def create_dungeon():
  name = input("What is the name of the dungeon? ")
  danger_lvl = int(input("What is the danger level of the dungeon? "))
  recommended_min_lvl = int(input("What is the recommended minimum level for this dungeon? "))
  loot_qual = input("What is the loot quality of this dungeon? ")
  return Dungeon(name, danger_lvl, recommended_min_lvl, loot_qual)

"""def generate_situation():
  situations = [
    "You enter a dark cave and hear eerie sounds echoing through the tunnels.",
    "A mysterious figure approaches you in the forest, cloaked in shadows.",
    "You find an ancient map that leads to a hidden treasure buried deep underground.",
    "A sudden storm forces you to seek shelter in an abandoned castle.",
    "You stumble upon a village plagued by a strange curse that turns people into stone."
  ]
  return random.choice(situations)

def roll_dice(sides=20):
  return random.randint(1, sides)

def process_response(action: str, roll: int, skill_level: int, opponent, damage: int):
  if roll >= 20 - skill_level:
        return f"🎯 Kritischer Erfolg! Deine Aktion '{action}' gelingt perfekt!" and opponent.hp -= damage * 2
    elif roll >= 15 - skill_level:
        return f"✅ Erfolg! Du führst '{action}' mit ordentlichem Ergebnis aus." and opponent.hp -= damage
    elif roll >= 10 - skill_level:
        return f"⚠️ Teilerfolg. '{action}' klappt nur teilweise – es läuft nicht ganz rund."
    else:
        return f"❌ Misserfolg. Deine Aktion '{action}' scheitert völlig." and self.hp -= damage
        """

test_hero = Hero("Ismael the Mighty", 5, "Warrior", True, True) #For testing purposes
print(test_hero)
test_dragon = Dragon("Fire", 10, True) #For testing purposes
print(test_dragon)
test_dungeon = Dungeon("The Cave of Doom", 5, 3, "Legendary") #For testing purposes
print(test_dungeon)
hero1 = create_hero()
print(hero1)

"""
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('DungeonMaster')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.german')

while True:
    frage = input("Du: ")
    antwort = bot.get_response(frage)
    print(f"Bot: {antwort}")
"""