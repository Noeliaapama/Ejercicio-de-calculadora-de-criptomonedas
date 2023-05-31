import sqlite3
from flask_classic import BBDD

class Conexion:
    def __init__(self,querySql,params=[]):
        self.con = sqlite3.connect(BBDD)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySql,params)

    def añadir_fila(id, date, time, from, quantity_from, to, quantity_to):
        conn = sqlite3.connect(BBDD)
        c = conn.cursor()
        c.execute("INSERT INTO mov_criptos ('id', 'date', 'time', 'from', 'quantity_from', 'to', 'quantity_to') VALUES (?,?,?,?,?,?,?)", ('id', 'date', 'time', 'from', 'quantity_from', 'to', 'quantity_to'))
        conn.commit()
        conn.close()
