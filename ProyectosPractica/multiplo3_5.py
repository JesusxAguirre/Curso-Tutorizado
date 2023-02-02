def solution(number):
  
    return sum([int(multiplo) for multiplo in range(0,number) if multiplo % 3 ==0 or multiplo % 5 ==0 ])


print(solution(6))