#revertir de una oracion todas las palabras que tienen mas de 5 letras
import time
def spin_words(input):
    print(time.time())
    # Your code goes here
    #creando lista donde guardaremos la oracion revertida
    multiple_words = []
    sentence = input.split(" ")
    
    if len(sentence) > 1:
        #por cada palabra de la oracion
        for word in sentence:
            #si la palabra es mayor a 5 se pone al reves
            if len(word) >= 5:
                word= list(word)
                word.reverse()
                word = "".join(word)
                multiple_words.append(word)
            #caso contrario se deja igual
            else:
                multiple_words.append(word)
        return " ".join(multiple_words)
    else:
        single_word = input
        if len(single_word) >= 5:
            
            single_word = list(input)
            single_word.reverse()
            return "".join(single_word)
        else: 
            return single_word


def spin_words2(sentence):
    # Your code goes here
    print(time.time())
    return " ".join([word[::-1] if len(word) >= 5 else word for word in sentence.split(" ")])
  
print(spin_words2("Bienvenido a la manipulacion de archivos externos GWYN EL SEÑOR DE LA LUZ quien descubrio la llama primigenia dando asi la era de la luz y oscuridad estamos manipulando el documento"))