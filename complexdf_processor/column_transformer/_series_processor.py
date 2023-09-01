import pandas as pd
import numpy as np

from ..complex_float import ComplexFloat
class SeriesProcessor:
    """Class for complex series operation.
    """
    def __init__(self):
        pass
    @staticmethod
    def series(lst):
        """Generate series of ComplexFloat with list of re and im tuples.

        Parameters
        ----------
        lst : list of tuples
            The list of tuples (re,im) for ComplexFloat constructor.

        Returns
        -------
        s ：list of ComplexFloat
            list of ComplexFloat with re and im parts from `lst`.

        Examples
        --------
        >>> from complexdf_processor.column_transformer import SeriesProcessor
        >>> sp = SeriesProcessor()
        >>> lst = [(1,1),(0,0.5),(-1,-2)]
        >>> sp.series(lst)
        0      1+1i
        1    0+0.5i
        2     -1-2i
        dtype: object
        """
        complist=[x if x is None else ComplexFloat(*x) for x in lst]
        s = pd.Series(complist)
        return s
    @staticmethod
    def unique(s):
        """Generate the list of unique values of a complex series.

        Parameters
        ----------
        s : series of ComplextFloat

        Returns
        -------
        uniques : list of ComplextFloat
            The list of unique ComplextFloat in s.

        """
        astuple = lambda x: None if x is None else x.tuple
        uniques = s.map(astuple).unique()
        return uniques

    @staticmethod
    def rotate(s,phi):
        factor = ComplexFloat(mod=1,arg=phi)
        s_t = s.apply(lambda x:np.nan if pd.isnull(x) else x*factor)
        return s_t

    @staticmethod
    def conj(s):
        s_t = s.apply(lambda x:x.conj)
        return s_t


