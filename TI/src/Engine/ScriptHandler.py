import DataGrinder


def CallExternalScript(ID, args = None):
    script_data = DataGrinder.get_script_data(ID)
    script_data[1]['args'] = args
    script = __import__(script_data[0]['Name'])
    scriptcall = getattr(script, 'call')
    result = scriptcall(**script_data[1])
    return result