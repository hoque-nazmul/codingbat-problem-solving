def array123(nums):
  unique_nums = []
  for item in nums:
      if item not in unique_nums:
          unique_nums.append(item)

  unique_nums.sort()

  if unique_nums[0:3] == [1, 2, 3]:
      return True
  return False
