frases = ["Los lunes son los mejores días para programar","Python es moderno","Veremos Inteligencia Artificial más adelante"
          ,"Lambda simplifica el código"]

frases.sort(key=lambda f: len(f),reverse=True)

print(frases)