class Time:

    def __init__(self, time):
        self.time = time
        self.observers = []

    def change_time(self, time):
        self.time += time
        self.notify()

    def add_observer(self, who):
        self.observers.append(who) # TODO у тебя этот метод используется два раза в самом начале программы, а потом ты
        # TODO просто впихиваешь готовый список. Так не пойдет, у тебя при добавлении или удалении обсервера должны
        # TODO каждый раз дергаться конкретные методы созданные для этого.



    def notify(self):
     for obs in self.observers:
      obs.live_circle(self.time//24)
