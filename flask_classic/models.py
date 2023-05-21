import sqlite3

#conexion con la base de datos
def data_sql():
    con = sqlite3.connect("data/mov_criptos.sqlite")
    cur = con.cursor()
    res = cur.execute("select * from mov_criptos;")
    filas = res.fetchall()
    columnas = res.description 
    
