def swap_fun():
  x = nums.pop(i1)
  nums.insert(i, x)
  print(nums)
nums = [6,9,8,1,2,4]
print(nums)
i = 0
i1 = 1
y = 0
while True: 
  while i1 <= len(nums):
    try:
     if nums[i] > nums[i1]:
       swap_fun()
       i += 1
       i1 += 1
     elif nums[i] <= nums[i1]:
       i += 1
       i1 += 1
    except:
      i = 0
      i1 = 1
  break
