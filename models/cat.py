import random

from configs import cat_config


class Cat:

    def __init__(self, name):
        self.name = name
        self.owner = None
        self.satieti = cat_config.START_SATIETI
        self.breed = None
        self.home = None # TODO разбей свойства на группы в зависимости от того чему они равны, ноны вместе и тд

    def __str__(self):
        if self.is_alive():
            return f'{self.name}. Сытость - {self.satieti}. Порода - {self.breed}.\n'
        else:
            self.owner.cat = None
            return f'{self.name} умер от голода.\n'

    def is_alive(self):
        return self.satieti > 0

    def set_home(self):
        self.home = self.owner.home

    def eat(self):
        if self.home.cat_food >= cat_config.MIN_EAT_HOME_CAT_FOOD:
            self.owner.home.cat_food -= cat_config.STEP_EAT_FOOD
            self.satieti = min(cat_config.MAX_SATIETI,
                               self.satieti + cat_config.EAT_SATIETI_STEP)
            print(f'{self.name} поел.') # TODO отдели все принты в методах от логики пустой строкой
        else:
            self.satieti = max(cat_config.MIN_SATIETI,
                               self.satieti - cat_config.STEP_HUNGER)
            print(f'{self.name} голодает.')

    def steal_food(self):
        if random.randint(1, 10) <= cat_config.STEAL_CHANCE:
            # TODO опять путаешь уровни асбстракции, в краже еды не должно быть логики отвечающей за рандом, вынеси рандом уровнем выше
            # можно разделить на два метода, один сакссес, второй фейлд, или в общий передавать тру/фолс
            self.owner.home.fridge.man_food.value -= cat_config.STEAL_FOOD_STEP_FOOD
            self.satieti += min(cat_config.MAX_SATIETI,
                                self.satieti + cat_config.STEAL_FOOD_STEP_SATIETI)
            print(f'{self.name} стащил еду.')
        else:
            print(f'{self.name} попытался стащить еду, но потелпел неудачу.')
            self.satieti = max(
                cat_config.MIN_SATIETI,
                self.satieti - cat_config.STEAL_FOOD_STEP_SATIETI_UNLUCK)

    def sleep(self):
        self.satieti = max(cat_config.MIN_SATIETI,
                           self.satieti - cat_config.SLEEP_SATIETI_STEP)
        print(f'{self.name} поспал.')

    def walk(self):
        self.satieti = max(cat_config.MIN_SATIETI,
                           self.satieti - cat_config.WALK_SATIETI_STEP)
        print(f'{self.name} погулял.')

    def look_out_window(self):
        self.satieti = max(
            cat_config.MIN_SATIETI,
            self.satieti - cat_config.LOOK_OUT_THE_WINDOW_SATIETI_STEP)
        print(f'{self.name} смотрел в окно.')

    def action(self, selected_action):
        action_dict = {
            1: self.eat,
            2: self.sleep,
            3: self.walk,
            4: self.look_out_window,
            5: self.steal_food
        }
        return action_dict[selected_action]()

    def live(self):
        if self.satieti <= cat_config.LIVE_MIN_SATIETI:
            if self.owner.home.cat_food >= 20:
                self.eat()
            else:
                self.steal_food()
        else:
            self.action(random.randint(2, 4))

    # def lived_day(self, day): # TODO давно уже вижу этот кусок в комментарии, он точно нужен?
    #   if day % 365 == 0:
    #     self.age += cat_config.GROW_STEP

    def live_circle(self):
        if self.is_alive():
            self.live()


class RussianBlueCat(Cat):

    def __init__(
            self,
            name,
    ):
        super().__init__(name)
        self.breed = 'русская голубая'


class ScotishCat(Cat):

    def __init__(
            self,
            name,
    ):
        super().__init__(name)
        self.breed = 'шотландская'


class SphinxCat(Cat):

    def __init__(
            self,
            name,
    ):
        super().__init__(name)
        self.breed = 'сфинкс'
