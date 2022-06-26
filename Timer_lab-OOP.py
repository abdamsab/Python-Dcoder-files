
class Timer:
  def __init__(self, hour, minute, second):
    self.__hour = hour
    self.__minute = minute
    self.__second = second
      

  def __str__(self):
    if(self.__hour < 10):
      hrs = '0'+str(self.__hour)
    if(self.__minute < 10):
      mins = '0'+str(self.__minute)
    if(self.__second < 10):
      secs = '0'+str(self.__second)
      
    hrs = self.__hour
    mins = self.__minute
    secs = self.__second
    return str(hrs) + ':' + str(mins)+ ':' + str(secs)
        

  def next_second(self):
    self.__second += 1
    if(self.__second > 59):
      self.__second = 0
      self.__minute += 1
    if(self.__minute > 59):
      self.__minute = 0
      self.__hour += 1
    if(self.__hour > 23):
      self.__hour = 0
       

  def prev_second(self):
    self.__second -= 1
    if(self.__second <0):
      self.__second = 59
      self.__minute -= 1
    if(self.__minute < 0):
      self.__minute = 59
      self.__hour -= 1
    if(self.__hour < 0):
      self.__hour = 23


timer = Timer(2, 5,3)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
