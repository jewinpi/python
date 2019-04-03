leapTest = int(input('Find if a year is a leap year: ')) #gets user input to test for leap year
if leapTest > 0: # simple test to see if the integar inputted is positive
 if leapTest%4 == 0: # tests of inputted value can be divided by 4 evenly
   print(leapTest , 'is a leap year') 
 else: # if the value inputted cannot be divided by 4 evenly
   print(leapTest , 'is not a leap year')
else: # else statement for if the value entered was a negative
  print('Cannot have a negative year!')
leapYears = [2020, 2021] # list of a leap and non leap year to test method
for x in leapYears: # loops through each value in the list
  if x%4 == 0: # checks if a value in the list can be divided by 4 evenly
    print(x, 'is a leap year')
  else: # else statement for is a value in the list is not divisible by 4 evenly
    print(x, 'is not a leap year')
