from faker import Faker
import time

from models.man import Man, Wife
from models.home import Home
from models.time_obs import Time

if __name__ == "__main__":

  living_beings = []


  character = Man(Faker('ru_RU').first_name_male(), 30)
  women = Wife(Faker('ru_RU').first_name_female(), 29)
  character_home = Home()

  character.move_to_new_house(character_home)
  character.get_married(women)
  global_time = Time(24)
  global_time.add_observer(character)
  global_time.add_observer(women)

  livers = [character, women]


<<<<<<< HEAD
  for i in range(3650):
=======
  while True:
>>>>>>> main

    for cat in character.cats['живые']:
      if cat not in livers:
        livers.append(cat)
        global_time.add_observer(cat)

    for cat in character.cats['мертвые']:
      if cat in global_time.observers:
        livers.remove(cat)
        global_time.remove_observer(cat)

    if not (character.is_alive() and women.is_alive()):
      break

    else:
      global_time.change_time()

      print(f"\nДень {global_time.time//24}\n")
      for liver in livers:
        print(f"{liver}\n")

      character.home.fridge.man_food.spoil()
      character.home.fridge.cat_food.spoil()

    time.sleep(0)
  
  print(
    f"Симуляция закончена. У {character.name} {character.money} денег, {character.happiness} счастья. "
    f"Жена {women.name}, счастье {women.happiness}. {len(character.cats['живые'])} котиков. " 
    f"\nКотиков умерло: {len(character.cats['мертвые'])}."
  )



