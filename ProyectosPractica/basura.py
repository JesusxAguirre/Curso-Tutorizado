def find_roots(a, b, c):
    root1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
    root2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)
    respuesta = (root1,root2)
    print(respuesta)
    return respuesta

print(find_roots(2, 10, 8))
