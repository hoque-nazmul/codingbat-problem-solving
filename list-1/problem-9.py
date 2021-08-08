def sum2(nums):
  if len(nums) == 0:
    return 0
  if len(nums) >= 2:
    return sum(nums[:2])
  else:
    return nums[0]