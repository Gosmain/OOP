from faker import Faker

from models.man import Man, Wife
from models.home import Home

if __name__ == "__main__":

  character = Man(Faker('ru_RU').first_name_male(), 30)
  women = Wife(Faker('ru_RU').first_name_female(), 29)
  character_home = Home() # TODO после инициализации добавь пустую строку
  character.move_to_new_house(character_home)
  character + women

  for i in range(1, 366):

    character.live_circle(i)
    women.live_circle(i)

    for cat in character.remember_living_cats():
      print(cat) # TODO в теоретической теории, если у тебя кот сразу будет, то ты инфу о нем выведешь раньше, чем номер дня
      cat.live_circle()

    print(f'День {i}\n{character}\n{women}')

    character.home.fridge.man_food.spoil()
    character.home.fridge.cat_food.spoil()

    if not (character.is_alive() and women.is_alive()):
      break

  print(
    f'Год закончен, котиков у человека: {len(character.remember_living_cats())}.\nКотиков умерло: {len(character.remember_dead_cats())}.'
  )
    # TODO сократи строку, не умещается в 80 символов, не вырезай ничего, просто вторую половину перенеси на новую строку (туду после исправления можно удалить)
    # TODO так же давай добавим в итоговую стату инфу по человечкам, сколько денег фарманули , что по счастью и тд

    # В остальном все хорошо, осталась финишная прямая и можно заканчивать)
