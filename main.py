from faker import Faker
import time

from models.man import Man, Wife
from models.home import Home
from models.time_obs import Time

if __name__ == "__main__":


  character = Man(Faker('ru_RU').first_name_male(), 30)
  women = Wife(Faker('ru_RU').first_name_female(), 29)
  character_home = Home()

  character.move_to_new_house(character_home)
  character.wedding(women)
  global_time = Time(24)
  global_time.add_observer(character)
  global_time.add_observer(women)

  while character.is_alive():
    
    time.sleep(0.5) # TODO перед первым проходом будем задержка, лучше убери в конец итерации

    global_time.observers = sorted([character, women] +
                            character.remember_living_cats(),
                            key=lambda x: type(x) == type(character),
                            reverse=True) # TODO оставил комментарий внутри Тайм()

    if not (character.is_alive() and women.is_alive()):
      break

    else:
      global_time.change_time(1) # TODO а тут разве кроме 1 что-то будет? Подумай как изменить метод, можно обойтись
      # TODO без аргументов

      print(f'\nДень {global_time.time//24}\n')
      for liver in global_time.observers: # TODO давай всех существ будем держать на этом уровне в списке/словарике, без
        # TODO обращения к Тайму()
        print(f'{liver}\n')

      character.home.fridge.man_food.spoil()
      character.home.fridge.cat_food.spoil()

  print(
    f'Симуляция закончена. У {character.name} {character.money} денег, {character.happiness} счастья. '
    f'Жена {women.name}, счастье {women.happiness}. {len(character.remember_living_cats())} котиков.' 
    f'\nКотиков умерло: {len(character.remember_dead_cats())}.'
  )
