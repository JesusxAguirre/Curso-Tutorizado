def find_short(sentence):
    sentence =sentence.split(" ")
    sentence.sort(key=len)
    
    return len(sentence[0])
    

def find_short2(sentece):
  
  return min(len(x) for x in sentece.split(" "))


