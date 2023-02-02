import sys
print("Welcome to program par o impar")
#declaramos una variable booleana para cada vuelta de bucle
boolean=True
contador = 0
while(boolean):
  while contador <3:
    try:
      numero = int(input("What number are you thinking? \n"))
      break 
    except ValueError:
      contador = contador +1 
      print("it can't put no numeric data")
      if contador ==3:
        print("to many attempts. leaving the program...")
        sys.exit()        
  if numero % 2 == 0:
    print("It is par")
  else:
    print("It is impar")
    
  decision= input("Do you want to try again? Choice Y=(YES), N=(NOT) Y/N \n")
  
  if decision == "Y":
    boolean = True
  elif decision == "N":
    print("Thanks you for use my program! :)")
    boolean = False
  else:
    print("WARNING!!")
    break  