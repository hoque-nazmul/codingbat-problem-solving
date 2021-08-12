# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

# make_chocolate(4, 1, 9) → 4
# make_chocolate(4, 1, 10) → -1
# make_chocolate(4, 1, 7) → 2

def make_chocolate(small, big, goal):
  small_needed = goal - big * 5
  
  if goal > big * 5 + small:
    return -1
    
  if small_needed <= small and small_needed >= 0:
    return small_needed
    
  if small_needed < 0 and goal % 5 <= small:
    return goal % 5
    
  return -1