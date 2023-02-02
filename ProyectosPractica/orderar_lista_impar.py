def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  print(odds)
  return [x if x%2==0 else odds.pop() for x in arr]


print(sort_array([5, 3, 2, 8, 1, 4]))
  