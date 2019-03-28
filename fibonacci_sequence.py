endNum = int(input('Fibonacci sequence range: ')) 
i = 0
i1 = 1
if endNum > 0:
  print('0')
  print('1')
  while endNum >= i:
    i = i + i1
    i1 = i + i1 
    if endNum >= i: 
      print(i)
    if endNum >= i1:
      print(i1)
else:
  print('Cannot have a range equal or less than 0')
