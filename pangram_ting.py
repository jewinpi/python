p = input('Type your sentence\n') # prompts user to type in a sentence on a new line
p.lower() # makes everything the user enetered lowercase
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # a list of the alphabet used later for checking if string entered a pangram
i = 0 # useful in the for loop
for letter in alphabet: # loops through each value in the list
 if p.count(letter)<1: # checks if the count of each letter in the list in the string entered by the user is less than 1
   print('Your sentence is not a pangram')
   break # ends loop 
 else:
   i = i + 1 # adds one to itself if a letter in the list is inside the string entered
if i == 26: # checks if i = 26 (to account for every letter in the alphabet)
 print('Your sentence is a pangram')
