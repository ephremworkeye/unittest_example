def add(x, y):
    ''' add numbers '''
    return x + y

def subtract(x, y):
    ''' subtract numbers'''
    return x-y

def multiply(x, y):
    ''' multiply numbers'''
    return x * y

def divide(x, y):
    ''' divide numbers'''
    if y != 0:
        return x // y
    else:
        return " y should not be zero"
    