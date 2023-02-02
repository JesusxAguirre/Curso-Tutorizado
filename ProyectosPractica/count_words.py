#import sys
import io
text = io.open("archivo-externo.txt",'r',encoding="utf-8")

string= text.readlines()
s = ' '.join(string)
a= s.split(' ')
print(a)


contador = 0
for i in a:
  print(i)
  contador = contador + 1

print(contador)
#print("Muy bien me has demostrado lo que estas pensando en: " + str() + " palabras" )