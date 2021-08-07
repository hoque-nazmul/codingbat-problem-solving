def front_back(str):
    if len(str) == 1 or len(str) == 0:
      return str
    if len(str) == 2:
      return str[::-1]
    if len(str) > 2:
      li = list(str)
      first_ch = li[0]
      li[0] = li[len(str) - 1]
      li[len(str) - 1] = first_ch
      return ''.join(li)
  
    
    