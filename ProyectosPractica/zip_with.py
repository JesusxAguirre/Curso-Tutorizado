def zip_with(fn,a1,a2):
    #your code herea
    return list(map(fn,a1,a2))
  

print(zip_with("add", [0,1,2,3,4,5], [6,5,4,3,2,1] ))