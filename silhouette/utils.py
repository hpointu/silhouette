import os
from silhouette.settings import DATA_DIR


def data_path(filename):
    return os.path.join(DATA_DIR, filename)