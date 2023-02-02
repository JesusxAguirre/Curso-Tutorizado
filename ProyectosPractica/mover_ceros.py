def move_zeros(lst):
    return  [num for num in lst if num != 0 ] + [zero for zero in lst if zero == 0]
  
print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))