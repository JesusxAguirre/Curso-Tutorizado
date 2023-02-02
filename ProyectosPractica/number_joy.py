def number_joy(n):
    i = sum(int(number) for number in str(n))
    second_number = str(i)[::-1]
   

    return True if i * int(second_number) == n else False
  
print(number_joy(1729))