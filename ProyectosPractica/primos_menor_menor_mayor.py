def only_oddDigPrimes (num): # P.O.D.P (pure ood digit prime)
    for x in range(2,num):
      if x % x == 0 :
        print("no es primo: ",x)
      else:
        print("es primo: ",x)



print(only_oddDigPrimes(20))