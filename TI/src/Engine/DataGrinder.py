import sqlite3 as lite

db_path = 'I:\\TI\\TI\\GameData.db'

con = None
cur = None

def open_con():
    global con
    try:
        con = lite.connect(db_path)
    except lite.Error, e:
        pass

def close_con():
    global con
    try:
        con.close()
    except lite.Error, e:
        pass

def get_tile_data(id):
    global con, cur
    query = 'SELECT * FROM Tiles WHERE ID = ' + str(id)
    
    open_con()
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchall()
    close_con()

    