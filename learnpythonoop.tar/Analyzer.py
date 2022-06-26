
from string import punctuation

class Analyzer:
  
  def __init__(self, s):
    for c in punctuation:
      s = s.replace(c, '')
      s = s.lower()
      self.words = s.split()
      
  def number_of_words(self):
    return len(self.words)
    
  def starts_with(self, s):
    return len([w for w in self.words if w[:len(s)]==s])
    
    
  def number_with_length(self, n):
    return len([w for w in self.words if len(w)==n])
  
      
    