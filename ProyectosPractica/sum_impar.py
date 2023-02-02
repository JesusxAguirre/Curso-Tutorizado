def find_it(seq):
    lista =[num for num in seq if seq.count(num) % 2 != 0] 
    return lista[0]
  

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))