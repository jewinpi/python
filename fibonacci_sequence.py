endNum = int(input('Fibonacci sequence range: ')) 
i = 0
i1 = 1
if endNum > 0:
  print('0')
  while endNum >= i:
    print(i1)
    i = i + i1
    print(i)
    i1 = i + i1 
else:
  print('Cannot have a range equal or less than 0')
