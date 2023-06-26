from models.man import Man
from models.home import Home
from models.russianblueCat import RussianBlueCat

if __name__ == "__main__":

  char = Man('Никитосов', 33)
  char.home = Home(char)
  for i in range(1, 367):
    print(f'День {i-1}\n{char}')
    char.live_circle(i)
    if char.cat !='':
      for el in char.l_of_cat:
        el.live_circle()
        if el.satieti > 0:
          print(f'{el}\n')      
    if not char.is_alive():
      break
  print(f'Год закончен, котиков у человека: {len(char.l_of_cat)}')
  

  
  

  


  

  
  
  
  


  
  
  
  

  
  
