﻿import sqlite3 as lite
import libtcodpy as libtcod
import  os, random

#db_path = 'C:\\Temporary_Insanity\\TI\\GameData.db'
db_path = 'I:\\TI\\TI\\GameData.db'

con = None
cur = None

def open_con():
    global con
    try:
        con = lite.connect(db_path)
        con.row_factory = dict_factory
    except lite.Error, e:
        print('Error in open_con')
        pass

def close_con():
    global con
    try:
        con.close()
    except lite.Error, e:
        print('Error in close_con')
        pass

def dict_factory(cursor, row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def execute_query(query):
    global cur

    open_con()
    cur = con.cursor()
    cur.execute(query)
    data = cur.fetchall()
    close_con()

    return data

def get_script(ID):
    script_data = {}
    query = 'SELECT * FROM Scripting WHERE ID = ' + str(ID)
    data = execute_query(query)
    script_data['Name'] = data[0]['SCRIPT_NAME']
    script_data['Arg_Ref'] = data[0]['ARG_REF']
    return script_data

def get_script_args(ARG_REF):
    args = {}
    query = 'SELECT ARG_NAME FROM Scripting_Args_Ref WHERE ARG_REF = "' + ARG_REF + '"'
    arg_names = execute_query(query)
    for name in arg_names:
        query = 'SELECT ' + name['ARG_NAME'] + ' FROM Scripting_Args WHERE ARG_REF = "' + ARG_REF + '"'
        arg = execute_query(query)
        args[name['ARG_NAME']] = arg[0][name['ARG_NAME']]
    return args

def get_script_data(ID):
    script = get_script(ID)
    temp = script['Arg_Ref']
    args = get_script_args(temp)
    return (script, args)

def get_color(name):
    if name == '':
        return libtcod.BKGND_NONE
    else:
        query = 'SELECT R,G,B FROM Colors WHERE Name = "' + name + '"'
        data = execute_query(query)
        return libtcod.Color(int(data[0]['R']), int(data[0]['G']), int(data[0]['B']))

def get_color_varied(name, variance):
    query = 'SELECT R,G,B FROM Colors WHERE Name = "' + name + '"'
    data = execute_query(query)
    return libtcod.Color(max(0, int(data[0]['R']) + random.randint(-variance,variance)), max(0, int(data[0]['G']) + random.randint(-variance,variance)), max(0, int(data[0]['B']) + random.randint(-variance,variance)))

def get_tile_data(id):
    tile_data = {}
    query = 'SELECT * FROM GameObject_Tiles WHERE ID = ' + str(id)
    
    data = execute_query(query)

    tile_data['Char'] = data[0]['Char']
    if data[0]['Varied_Color']:
        tile_data['Bcolor'] = get_color_varied(data[0]['Bcolor'], data[0]['Varied_Color'])
        tile_data['Fcolor'] = get_color_varied(data[0]['Fcolor'], data[0]['Varied_Color'])
    else:
        tile_data['Bcolor'] = get_color(data[0]['Bcolor'])
        tile_data['Fcolor'] = get_color(data[0]['Fcolor'])
    tile_data['Solid'] = data[0]['Solid']
    tile_data['Block_sight'] = data[0]['Block_sight']

    return tile_data

def get_actor_data(id):
    actor_data = {}

    query = 'SELECT * FROM GameObject_Actors WHERE ID = ' + str(id)
    
    data = execute_query(query)
    
    actor_data['Name'] = data[0]['Name']
    actor_data['Char'] = data[0]['Char']
    actor_data['Bcolor'] = get_color(data[0]['Bcolor'])
    actor_data['Fcolor'] = get_color(data[0]['Fcolor'])
    actor_data['AI_Script_Ref'] = data[0]['AI_Script_Ref']

    return actor_data

def get_prop_data(id):
    prop_data = {}

    query = 'SELECT * FROM GameObject_Props WHERE ID = ' + str(id)
    
    data = execute_query(query)

    prop_data['Char'] = data[0]['Char']
    prop_data['Bcolor'] = get_color(data[0]['Bcolor'])
    prop_data['Fcolor'] = get_color(data[0]['Fcolor'])
    prop_data['Solid'] = data[0]['Solid']
    prop_data['Block_sight'] = data[0]['Block_sight']

    return prop_data

def get_map_data(id):
    map_data = {}

    query = 'SELECT * FROM Maps Where ID = ' + str('id')

    data = execute_query(query)

    data = data[0]

    map_data['Name'] = data['Name']
    map_data['Width'] = data['Width']
    map_data['Height'] = data['Height']
    map_data['Size_Variance'] = data['Size_Variance']
    map_data['Num_Rooms'] = data['Num_Rooms']
    map_data['Script_ID'] = data['Script_ID']
    map_data['Tile_IDs'] = get_tile_ref_data(data['Tile_Ref'])

    return map_data

def get_tile_ref_data(TILE_REF):
    tile_ids = []

    query = 'SELECT * FROM Map_Tile_Refs WHERE Tile_Ref = "' + TILE_REF + '"'

    data = execute_query(query)

    for row in data:
        tile_ids.append(row['Tile_ID'])

    return tile_ids



    