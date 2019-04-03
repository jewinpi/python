endNum = int(input('Fibonacci sequence range: ')) # prompts user for a number for the loop to stop at
i = 0 # used for start of fibbonacci sequence
i1 = 1 # used for start of fibbonacci sequence
if endNum > 0: # checks if value entered by user is larger than 0
  print(i) # prints i
  print(i1) # prints i1
  while endNum >= i: # runs loop if value entered by user is larger than or equal to i
    i = i + i1 # adds i to i1 
    i1 = i + i1 # adds the newely defined i to i1 
    if endNum >= i: # checks if value entered by user is larger or equal to i
      print(i)
    if endNum >= i1: # checks if value entered by user is larger or equal to i1
      print(i1)
else: # runs if value entered by user is less than 0
  print('Cannot have a range equal or less than 0')
