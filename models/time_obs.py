class Time:

    def __init__(self, time):
        self.time = time
        self.observers = []

    def change_time(self, time):
        self.time += time
        self.notify()

    def add_observer(self, who):
        self.observers.append(who)

    def remove_observer(self, who):
        self.observers.remove(who)

    def notify(self):
        for obs in self.observers:
            obs.live_circle()