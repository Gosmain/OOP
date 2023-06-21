from models.man import Man
from models.home import Home

if __name__ == "__main__":
  
  char = Man('Никитосов', 25)
  for i in range(1, 731):
    if char.is_alive():
      print(f'День {i}')
      char.live_circle(i)
      print(char)
    else:
      print(f'День {i}')
      print(char)
      break
  

