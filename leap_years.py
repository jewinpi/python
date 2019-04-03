leapTest = int(input('Find if a year is a leap year: ')) #gets user input for 
if leapTest%4 == 0:
  print(leapTest , 'is a leap year')
else:
  print(leapTest , 'is not a leap year')
leapYears = [2020, 2021]
for x in leapYears:
  if x%4 == 0:
    print(x, 'is a leap year aswell')
  else:
    print(x, 'is not a leap year')
