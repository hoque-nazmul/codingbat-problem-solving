def front3(str):
  front_ch = ''
  if len(str) > 3:
    front_ch = str[:3]
  else:
    front_ch = str
    
  return front_ch + front_ch + front_ch