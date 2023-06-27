from models.man import Man
from models.home import Home

if __name__ == "__main__":

  char = Man('Никитосов', 33)
  hm = Home()
  char.move_to_a_new_house(hm)
  for i in range(1, 366):
    char.live_circle(i)
    print(f'День {i}\n')
    print(char)
    if char.cat != '':
      for el in char.list_of_alive_cats():
        el.live_circle()
        print(f'{el}\n')
    if not char.is_alive():
      break
  print(
    f'Год закончен, котиков у человека: {len(char.list_of_alive_cats())+len(char.list_of_dead_cats())}'
  )

 