def max_end3(nums):
  larger_num = 0
  first_num = nums[0]
  last_num = nums[-1]
  if first_num > last_num:
    larger_num = first_num
  else:
    larger_num = last_num
  return [larger_num] * 3