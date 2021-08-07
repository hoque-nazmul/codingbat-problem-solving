def pos_neg(a, b, negative):
  if negative is True:
    if a < 0 and b < 0:
      return True
    return False
  else:
    if a < 0 and b < 0:
      return False
    elif a < 0 or b < 0:
      return True
  return False
    