import time
#mi solucion
def get_count(sentence):
    # my code
    contador = 0
    for letter in sentence:
      if letter in "aeiou": contador = contador + 1 
    print(time.time())
    return contador 

#solucion de kata
def getCount2(sentence):
    print(time.time())
    return sum(1 for letter in sentence if letter in "aeiouAEIOU")


print(getCount2("aeiou"))
