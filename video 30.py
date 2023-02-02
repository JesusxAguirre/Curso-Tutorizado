import queue

miCola =queue.Queue(4)

miCola.put("Barquisimeto")
miCola.put("Cabudare")
miCola.put("Madrid")

print(miCola.get()) 

print(miCola.full())

print("A contuacion se imprimen los elemenos restantes en la cola")

for elem in miCola.queue:
  print(elem)


while not miCola.empty():
  print(miCola.get()) 