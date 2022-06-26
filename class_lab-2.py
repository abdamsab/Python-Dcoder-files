
class QueueError(IndexError):  # Choose base class for the new exception.
  pass
    #
    #  Write code here
    #


class Queue:
  def __init__(self):
    self.__queue =[]
        #
        # Write code here
        #

  def put(self, elem):
    self.__queue.insert(0, elem)
    #print(self.__queue)
        #
        # Write code here
        #

  def get(self):
    if len(self.__queue) > 0:
      val = self.__queue[-1]
      del self.__queue[-1]
      return val
    else:
      raise QueueError
        #
        # Write code here
        #


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
