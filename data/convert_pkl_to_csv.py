import os,sys
import pandas as pd
import glob as glob

current_directory = os.getcwd()
pickles = glob.glob(f'{current_directory}/*.pkl')

for file in pickles:
    df = pd.read_pickle(file)
    df.to_csv(file.replace('pkl','csv'))
