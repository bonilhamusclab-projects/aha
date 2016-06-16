import numpy as np
import os
import pandas as pd
import pickle
import pylab as pl
import sys
import time

import bct

sys.path.append('../connectome_modules')
import connectome_functions as cf


def get_connectome_dir():
    return '../data/connectomes'


def get_study_ids():
    connectome_dir = get_connectome_dir()
    return [os.path.splitext(f)[0] for f in os.listdir(connectome_dir)]


def get_data_matrices():
    path_to_files = get_connectome_dir()
    list_files = cf.obtain_file_list(path_to_files)
    return cf.import_data_from_file(path_to_files, list_files)


def gen_null_matrices(num_rand, study_ids, dest_dir):

    for study_id in study_ids:
        t1 = time.time()

        mat = get_data_matrices()[study_id]
        num_rois = np.shape(mat)[1]

        null_matrix = np.zeros((num_rois, num_rois, num_rand))

        for r in xrange(0, num_rand):
            n_l = bct.randmio_und(mat, 3)
            null_matrix[:, :, r] = n_l[0]
            del n_l

        pik_name = os.path.join(dest_dir, "null_" + study_id + ".dat")
        with open(pik_name, "wb") as f:
            pickle.dump(null_matrix, f)

        del null_matrix

        t2 = time.time() - t1
        print "Elapsed individual time, subject = %s: %f" % (study_id, t2)
