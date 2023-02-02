
def square_digits(num):
    result = []
    num = str(num)
  
    lista = list(num)
    
    for i in lista:
      
      i = int(i)
      
      print(i)
      result.append(i**2)
    
    return  ''.join(map(str,result))

print(square_digits(2112))
