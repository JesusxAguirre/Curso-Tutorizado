def numeric_palindrome(number):
  number_reverse= 0
  while number != number_reverse:
    number = number + 1
    lista_numbers = list(map(str,str(number)))
    lista_numbers.reverse()

    number_reverse = "".join(lista_numbers)
    number_reverse = int(number_reverse)
    

  return number

def numeric_palindrome2(val):
  val += 1
  
  while str(val) != str(val)[::-1]:
    val+=1
  return val

print(numeric_palindrome2(50))