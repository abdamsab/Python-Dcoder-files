 
def segment(num):
  if num == 0:
    print("#"*10)
    print(("#" + " "*16 + "#\n" )*3, end='')
    print(("#" + " "*16  + "#\n" )*3, end='')
    print("#"*10)
    
  elif num == 1:
    print(" "*9 + "#" )
    print(( " "*10 + "#\n" )*3, end='')
    print(" "*9 + "#" )
    print((" "*10  + "#\n" )*3, end='')
    print(" "*9 + "#" )
  
  elif num == 2:
    print("#"*10)
    print(( " "*18 + "#\n" )*3, end='')
    print("#"*10)
    print(("#" + " "*16+"\n" )*3, end='')
    print("#"*10)
  
  elif num == 3:
    print("#"*10)
    print(( " "*16 + "#\n" )*3, end='')
    print("#"*10)
    print(( " "*16  + "#\n" )*3, end='')
    print("#"*10)
    
  elif num == 4:
    print("#" +" "*8 + "#")
    print(("#" + " "*16 + "#\n" )*3, end='')
    print("#"*10)
    print(( " "*16  + "#\n" )*3, end='')
    print("#"*10)
    
  elif num == 5:
    print("#"*10)
    print(("#" + " "*16 + "\n" )*3, end='')
    print("#"*10)
    print(( " "*16  + "#\n" )*3, end='')
    print("#"*10)
    
  elif num == 6:
    print("#"*10)
    print(("#" + " "*16 + "\n" )*3, end='')
    print("#"*10)
    print(("#" + " "*16  + "#\n" )*3, end='')
    print("#"*10)
    
  elif num == 7:
    print("#"*10)
    print(( " "*16 + "#\n" )*3, end='')
    print(" "*10 + "#")
    print(( " "*16  + "#\n" )*3, end='')
    print(" "*10 + "#")

  elif num == 8:
    print("#"*10)
    print(("#" + " "*16 + "#\n" )*3, end='')
    print("#"*10)
    print(("#" + " "*16  + "#\n" )*3, end='')
    print("#"*10)

  elif num == 9:
    print("#"*10)
    print(("#" + " "*16 + "#\n" )*3, end='')
    print("#"*10)
    print(( " "*16  + "#\n" )*3, end='')
    print("#"*10)
  
  
for i in range(10):
  segment(i)
