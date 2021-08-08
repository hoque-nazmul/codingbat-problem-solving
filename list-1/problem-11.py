def make_ends(nums):
  if len(nums) > 2:
   return [nums[0], nums[-1]]
  if len(nums) == 2:
    return nums
  if len(nums) == 1:
    return [nums[0]] * 2