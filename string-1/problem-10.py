def non_start(a, b):
  if len(a) < 2 and len(b) < 2:
    return ''
  if len(a) < 2:
    return b[1:]
  if len(b) < 2:
    return a[1:]
  
  return a[1:] + b[1:]
