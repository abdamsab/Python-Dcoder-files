class QueueError(IndexError):  # Choose base class for the new exception.
  pass
    #
    #  Write code here
    #


class Queue:
  def __init__(self):
    self.queue =[]
        #
        # Write code here
        #

  def put(self, elem):
    self.queue.insert(0, elem)
    #print(self.queue)
        #
        # Write code here
        #

  def get(self):
    if len(self.queue) > 0:
      val = self.queue[-1]
      del self.queue[-1]
      return val
    else:
      raise QueueError
        #
        # Write code here
        #
        
        
class SuperQueue(Queue):
  def __init__(self):
    Queue.__init__(self)
    # Write new code here.
    #
  def isempty(self):
    if len(self.queue) == 0:
      return True
    else:
      return False
      
      

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(100)
for i in range(4):
    print(que.isempty())
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
