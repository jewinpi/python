def swap_fun():
  x = nums.pop(i1)
  nums.insert(i, x)
  print(nums)
nums = [1,3,2,6,4]
print(nums)
i = 0
i1 = 1
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
     else:
       i = 0
       i1 = 1
    except:
      break
  break
