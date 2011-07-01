'''
Created on Jul 7, 2010

@author: brent
'''


def strs_to_float(row, default):
    return map(lambda x: str_to_float(x, default), row)

def str_to_float(str, default):
    try:
        flt = float(str)
    except ValueError:
        flt = default;
    return flt
    