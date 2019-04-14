ciph = input('Type something to cipher: ')
alph1 = {'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e':'f', 'f':'g', 'g':'h', 'h':'i', 'i':'j', 'j':'k', 'k':'l', 'l':'m', 'm':'n', 'n':'o', 'o':'p', 'p':'q', 'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'w', 'w':'x', 'x':'y', 'y':'z', 'z':'a', '1':'2', '2':'3', '3':'4', '4':'5', '5':'6', '6':'7', '7':'8', '8':'9', '9':'0', '0':'1'}
alph2 = {'a':'z', 'b':'a', 'c':'b', 'd':'c', 'e':'d', 'f':'e', 'g':'f', 'h':'g', 'i':'h', 'j':'i', 'k':'j', 'l':'k', 'm':'l', 'n':'m', 'o':'n', 'p':'o', 'q':'o', 'r':'q', 's':'r', 't':'s', 'u':'t', 'v':'u', 'w':'v', 'x':'w', 'y':'x', 'z':'y', '1':'0', '2':'1', '3':'2', '4':'3', '5':'4', '6':'5', '7':'6', '8':'7', '9':'8', '0':'9'}
phrase = []
a = ''
try:
 for char in ciph:
   phrase.append(alph1.get(char))

 Ciphed = a.join(phrase)
 print('Phrase ciphered is' , '"' + Ciphed + '"')
 phrase.clear()
except:
  print('Please only type in letters that are lowercase and numbers.')

deCiph = input('Do you want to dechiper the phrase? ')

if deCiph == 'yes':
  for char in Ciphed:
    phrase.append(alph2.get(char))
  deChiphed = a.join(phrase)
  print('Deciphered phrase is', '"' + deChiphed + '"')
else:
  print('Type in "yes" next time')
