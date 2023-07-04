from configs import day_config


class Day:

  def __init__(self, today=day_config.START_DAY):
    self.today = today

  def next_day(self):
    self.today += 1
