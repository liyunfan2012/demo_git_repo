import pandas as pd
import numpy as np

from ..complex_float import ComplexFloat
class SeriesProcessor:
    @staticmethod
    def series(lst):
        complist=[x if x is None else ComplexFloat(*x) for x in lst]
        return pd.Series(complist)
    @staticmethod
    def unique(s):
        astuple = lambda x: None if x is None else x.tuple
        return s.map(astuple).unique()

    @staticmethod
    def rotate(s,phi):
        factor = ComplexFloat(mod=1,arg=phi)
        s_t = s.apply(lambda x:np.nan if pd.isnull(x) else x*factor)
        return s_t

    @staticmethod
    def conj(s):
        s_t = s.apply(lambda x:x.conj)
        return s_t


