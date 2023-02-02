def validar_usuario(usuario):
    if usuario.isalnum():
      if len(usuario)<5:
        return  "El usuario no debe tener menor a 5 caracteres"
      elif len(usuario)>15:
        return "El usuario no debe tener mayor a 15 caracteres"
      else:
        return True
    return "El usuario solo puede contener letras y numeros"


def validar_password(password):
    mayuscula = False
    minuscula = False
    if len(password) < 10:
      return "la clave no puede tener menos  de 10 caracteres"
    elif password.isalnum():
       return "la clave debe contener un caracter que nosea ni letra ni numero"
    else:
     for i in password:
        if i.isupper(): mayuscula = True
        elif i.islower(): minuscula = True
        elif i == " ": return "la clave no puede contener espacios vacios"
    if mayuscula and minuscula:
      return True
    else:
      return "La clave no es segura"
