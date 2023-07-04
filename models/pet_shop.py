import random
from faker import Faker
# TODO не забывай следить за импортами, перед мержем можно использовать хоткей в пайчарме ctrl + alt + o ,
# TODO это форматирование импортов
from models.cat import RussianBlueCat, ScotishCat, SphinxCat


class PetShop:

  animals_dict = {1: RussianBlueCat, 2: ScotishCat, 3: SphinxCat}
  # TODO форматни словарик плз (одна запись - одна строка), это не критично ниразу, просто выглядит приятно

  @classmethod
  def sell(cls):
    return cls.animals_dict[random.randint(1, 3)]
    # TODO немного неудобный код для расширения количества пород, апни 3 так, чтобы если ты добавишь новый класс в словарик не пришлось тройку менять на 4 и тд
    # TODO давай еще фабрика будет возвращать тебе живого кота, а не абстракцию
