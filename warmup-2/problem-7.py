def array_front9(nums):
  first_4 = []
  if len(nums) > 4:
    first_4 = nums[:4]
  else:
    first_4 = nums
  
  if 9 in first_4:
    return True
  return False