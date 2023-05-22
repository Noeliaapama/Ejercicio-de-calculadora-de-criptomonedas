import sqlite3

def conexion(): #aqui hacemos la conexion con la base de datos
    con = sqlite3.connect("data/mov_criptos.sqlite")
    cur = con.cursor()
    res = cur.execute ("select * from mov_criptos;")
    #necesitamos recorrer la información de la base de datos
    fila = res.fetchall() 
    columna = res.description

    #necesitamos crearnos un diccionario de rutas index
    li_diccionario=[]

    for f in fila:
        diccionario = {}
        posicion = 0
        for c in columna:
            diccionario[c[0]] = f[posicion]
            posicion += 1
    li_diccionario.append(diccionario)
    return li_diccionario

