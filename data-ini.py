import pickle
import pathlib

abspath = pathlib.Path("data.dat").absolute()
def safe(array):
    pickle.dump(array,open(str(abspath),"wb"))

ini = [[],[],[],[]]
safe(ini)