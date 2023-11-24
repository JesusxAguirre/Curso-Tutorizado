import pandas as pd


df = pd.read_csv(
    'C:/Users/User/Documents/Jesús David/Jesus david 2.0/Curso python/Curso-Tutorizado/pandas/plantas.csv', sep=',')

busquedas = input(
    'Introduce tu busqueda del reino plantae. por nombre, filogenia, inflorescencia o Habitat -> ')


df = df.map(lambda x: x.lower())  # convierte del archivo csv todo en minisucla


def buscar_plantas(texto):

    texto = texto.lower()
    busquedas = [palabra for palabra in texto.split() if palabra in df.to_numpy()[
        0]]  # Esta linea de codigo sirve para filtrar por las palabras claves en el data frame, esto creo que prodia ser mejor

    df_filtrado = df

    # Aplicar filtros para cada busqueda

    # aply()
    # Aply recorre todos los values del data frame
    # lambda es una funcion anonima
    # row es toda la fila del data frame
    # el astype es para estar seguro que toda la fila es string
    # por lo tanto eso es relevante par ausar el meotod contains
    # que su nombre lo indica busca valga la redundancia si la fila contiene el valor
    # de la variabnle busqueda
    # axis solo acepta 0 y 1 , donde 0 son las columnas y 1 son los valores
    for busqueda in busquedas:
        filtro = df_filtrado.apply(lambda row: row.astype(str
                                                          ).str.contains(busqueda).any(), axis=1)
        df_filtrado = df_filtrado[filtro]

    return df_filtrado


print(buscar_plantas(busquedas))
