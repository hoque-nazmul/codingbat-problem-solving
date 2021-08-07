def front_times(str, n):
  result = ''
  ch_storage = ''
  if len(str) > 3:
    ch_storage = str[0:3]
  else:
    ch_storage = str

  for i in range(n):
    result += ch_storage
  
  return result