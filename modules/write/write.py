def write(fn: str, data: str):
    with open(fn, 'w') as file: # should introduce file modes here
        return file.write(data)
    