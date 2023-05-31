import sqlite3
from flask_classic import BBDD

class Conexion:
    def __init__(self,querySql,params=[]):
        self.con = sqlite3.connect(BBDD)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySql,params)
    