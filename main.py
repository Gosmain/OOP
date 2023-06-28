from models.man import Man
from models.home import Home

if __name__ == "__main__":

  character = Man('Никитосов', 30)
  character_home = Home()
  character.move_to_new_house(character_home)

  for i in range(1, 366):

    character.live_circle(i)

    for cat in character.remember_living_cats():
      print(cat)
      cat.live_circle()

    print(f'День {i}\n{character}')

    if not character.is_alive():
      break

  print(
    f'Год закончен, котиков у человека: {len(character.remember_living_cats())+len(character.remember_dead_cats())}'
  )

