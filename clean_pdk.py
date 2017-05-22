import cPickle as pickle
import numpy as np
import pandas as pd
import os

path = '/Users/santucci/Dropbox/PhD/SK/fiTQun_analysis/Knu_muGamma/atmnu/multiring/'

start = 0
nfiles = 6
pdk_pickle = 'files/pdk/600k_sample_16c/original_seeding/pickle/'
pdk_file = 'Knu_600k_{}_pandas.p'
pdk_file = os.path.join(path, pdk_pickle, pdk_file)
pdk_out = os.path.join(path, pdk_pickle, 'Knu_600k_{}_filtered.p')

int_cols = ['tfcfv', 'fcfv', 'nring', 'nse', 'mg']
drop_cols = ['enll', 'munll', 'pinll', 'pmgnll']
cuts = ['fcfv==1', 'nring==1', 'enll_munll>0', 'nse==2']

def MakeInt(df, cols):
    for col in cols:
        df[col] = df[col].astype(int)
    return df

def DropCols(df):
    for i, col in enumerate(drop_cols):
        others = drop_cols[i+1:]
        for other in others:
            df['_'.join([col, other])] = df[col] - df[other]
        df.drop(col, axis=1, inplace=True)
    return df

def GetCuts(dfname, cuts):
    cuts = ['({}.{})'.format(dfname, cut) for cut in cuts]
    return '&'.join(cuts)

def pipeline(df, dfname):
    df = MakeInt(df, int_cols)
    df = DropCols(df)
    return df[eval(GetCuts(dfname, cuts))]

for i in xrange(start, nfiles):
    pdk = pickle.load(open(pdk_file.format(i), 'rb'))
    pdk = pipeline(pdk, 'df')
    pdk.to_pickle(pdk_out.format(i))
    print('Saved file {}:\n{}\n'.format(i, pdk_out.format(i)))

