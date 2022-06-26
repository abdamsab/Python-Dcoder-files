#python 3.7.1

def unique_list(lst):
  return list(set(lst))
  
sample_list = [1,1,1,1,2,2,3,3,3,4,5]

print(unique_list(sample_list))