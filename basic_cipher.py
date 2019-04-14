ciph = input('Type something to cipher: ')
alph1 = {'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e':'f', 'f':'g', 'g':'h', 'h':'i', 'i':'j', 'j':'k', 'k':'l', 'l':'m', 'm':'n', 'n':'o', 'o':'p', 'p':'q', 'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'w', 'w':'x', 'x':'y', 'y':'z', 'z':'a', '1':'2', '2':'3', '3':'4', '4':'5', '5':'6', '6':'7', '7':'8', '8':'9', '9':'0', '0':'1'}
alph2 = {}
phrase = []
a = ''
try:
 for char in ciph:
   phrase.append(alph1.get(char))

 Ciphed = a.join(phrase)
 print(Ciphed)
 phrase.clear()
except:
  print('Please only type in letters and numbers.')

deChiph = int(input('1 for decryption and 2 for a double encryption: '))
try:
  if deChiph == 1:
    print('ok')
  if deCiph == 2:
    
