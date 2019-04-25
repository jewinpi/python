def swap_fun():
  x = nums.pop(i1)
  nums.insert(i, x)
nums = [0,-1,4,2,3,1]
print(nums)
i = 0
i1 = 1
y = 0
steps = 0
while i1 <= len(nums):
  try:
    if nums[i] > nums[i1]:
      swap_fun()
      i += 1
      i1 += 1
      y = 0
    if y >= len(nums):
      print('Took',steps,'passes to sort the numbers')
      break
    elif nums[i] <= nums[i1]:
      i += 1
      i1 += 1
      y += 1
  except:
    i = 0
    i1 = 1
    print(nums)
    steps += 1
