def arithmetic_arranger(problems):
  if len(problems) >= 5:
    return "Error: Too many problems."
  #rescantando problemas en una variable de tipo lista
  problems = problems
  #aqui se guardaran el primer datos de la operacion
  datos_a = []
  #aqui se guardara los segundos datos de la operacion
  datos_b = []
  #el tipo de operacion
  signos = []
  #aqui se guardan los resultados de cada operacion
  resultados = []
  #para recorrer las listas.
  contador = 0
  for i in problems:
    #asignando a cada variable por cada iteracion de la lista de problemas, primer valor, signo y segundo valor
    a, signo, b = i.split()

    if signo != "+" and signo != "-":
      return "Error: Operator must be '+' or '-'."

    if not a.isdigit() or not b.isdigit():
      return "Error: Numbers must only contain digits."

    if len(a) > 4 or len(b) > 4:
      return "Error: Numbers cannot be more than four digits"

    datos_a.append(int(a))
    signos.append(signo)
    datos_b.append(int(b))
  numero_operaciones = len(signos)
  for operacion in signos:
    if operacion == "+":
      resultados.append(datos_a[contador] + datos_b[contador])
    else:
      resultados.append(datos_a[contador] - datos_b[contador])
    contador += 1
  contador = 0
  print(datos_a)
  print(datos_b)
  print(numero_operaciones)

  while contador < numero_operaciones:
    distancia = len(str(max(datos_a[contador],datos_b[contador])))
    print(f"{datos_a[contador]:>{distancia + 2}}\n{signos[contador]} {datos_b[contador]:>{distancia}}\n{'':->{distancia+2}}\n {resultados[contador]:>{distancia+2}}")
    
    contador = contador + 1
    print(contador)
  #return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
