from faker import Faker

from models.man import Man, Wife
from models.home import Home
from models.time_obs import Time

if __name__ == "__main__":

  character = Man(Faker('ru_RU').first_name_male(), 30)
  women = Wife(Faker('ru_RU').first_name_female(), 29)
  character_home = Home()
  character.move_to_new_house(character_home)
  character.wedding(women)
  time = Time(0)
  time.add_observer(character)
  time.add_observer(women)

  while character.is_alive():

    time.observers = sorted([character]+[women]+character.remember_living_cats(), key=lambda x: type(x) == type(character), reverse=True)

    if not (character.is_alive() and women.is_alive()):
      break
      
    else:
      time.change_time(1)
      
      print(f'\nДень {time.time//24}\n')
      for liver in time.observers:
        print(f'{liver}\n')
        
      character.home.fridge.man_food.spoil()
      character.home.fridge.cat_food.spoil()    

  print(
    f'Год закончен, котиков у человека: {len(character.remember_living_cats())}.\nКотиков умерло: {len(character.remember_dead_cats())}.'
  )
