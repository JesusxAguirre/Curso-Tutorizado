#mi solucion
def create_phone_number(lista):
    #your code here
    phone_number = []
    contador= 0
    phone_number.append("(")
    for number in lista:
      if contador ==3: phone_number.append(")"), phone_number.append(" ")
      if contador == 6: phone_number.append("-")
      
      phone_number.append(number)
      
      contador = contador +1
    return "".join(map(str,phone_number))


#mejor solucion kata
def create_phone_number2(number):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*number)
print(create_phone_number2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

