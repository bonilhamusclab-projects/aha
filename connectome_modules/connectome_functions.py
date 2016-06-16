import os
from os import listdir
from os.path import isfile, join
import numpy as np


def obtain_file_list(path, termination='.csv'):
    return [f for f in listdir(path) if isfile(join(path, f)) and termination in f]


def import_data_from_file(path, list_files):
    matrices = {}
    for ff in list_files:
        long_ff = join(path, ff)
        a = np.loadtxt(open(long_ff, "rb"), delimiter=",", skiprows=0)
        [name, b] = os.path.splitext(os.path.basename(ff))
        matrices[name] = a
    return matrices
