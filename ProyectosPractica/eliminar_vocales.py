def disemvowel(string_):
    
    return "".join([letter for letter in string_ if letter not in "aeiouAEIOU"])
  
print(disemvowel("This website is for losers LOL!"))