import json
from ase import Atoms
from ase import Atom
import numpy as np


def json2atoms(jsonstr):
    dict = json.loads(jsonstr)
    symbols = ''
    for _i in dict['symbols']:
        symbols += _i
    atoms = Atoms(symbols, positions=dict['positions'])
    return atoms


frames = []
with open('DataSet.json') as f:
    while True:
        line = f.readline()
        if len(line) == 0: break
        atoms = json2atoms(line)
        frames.append(atoms)
