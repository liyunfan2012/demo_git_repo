from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted
from sklearn.pipeline import Pipeline
from ._series_processor import *
class ColumnDropTrivial(BaseEstimator, TransformerMixin):
    """Class for dropping columns with one unique value.

    Attributes
    ----------
    sp : instance of class SeriesProcessor
        From complexdf_processor.column_transformer._series_processor

    Examples
    --------
    >>> import pandas as pd
    >>> import numpy as np
    >>> from complexdf_processor.column_transformer import ColumnDropTrivial,SeriesProcessor
    >>> sp = SeriesProcessor()
    >>> s1 = sp.series([(1,1),(1,1),(1,1),(1,1),(1,1)])
    >>> s2 = sp.series([(1,1),(-1,1),(1.5,-1.5),(0,2.5),(-3.2,0)])
    >>> s3 = sp.series([(1.2,1.1),(2.1,1),(1.5,-1.5),None,(-3.2,0)])
    >>> X = pd.DataFrame({'s1':s1,'s2':s2,'s3':s3})
    >>> cmr = ColumnDropTrivial()
    >>> cmr.fit_transform(X)
             s2        s3
    0      1+1i  1.2+1.1i
    1     -1+1i    2.1+1i
    2  1.5-1.5i  1.5-1.5i
    3    0+2.5i      None
    4   -3.2+0i   -3.2+0i
    """
    def __init__(self):
        self.sp = SeriesProcessor()

    def fit(self, X, y=None):
        """Fit the transformer on `X`.

        Parameters
        ----------
        X : dataframe of shape (n_samples, n_features)
            Input data, where `n_samples` is the number of samples and
            `n_features` is the number of features.

        y : Ignored
            Not used, present here for API consistency by convention.

        Returns
        -------
        self : object
            Fitted estimator.
        """
        self.columns = X.columns.tolist()
        uniques = X.apply(lambda s: self.sp.unique(s), axis=0)
        cnt = uniques.apply(len)
        cols_trivial = cnt.index[cnt<=1].tolist()
        self.cols_trivial = uniques[cols_trivial]
        return self

    def transform(self, X):
        """Drop one-unique-value columns in `X`.

        Parameters
        ----------
        X : dataframe of shape (n_samples, n_features)
            The input data to complete.

        Returns
        -------
        X_t : dataframe of shape (n_samples, n_non_trivial_features)
            `X` with non_trivial features.
        """
        check_is_fitted(self,['columns','cols_trivial'])
        X_t = X.drop(columns=self.cols_trivial.keys())
        return X_t

    def inverse_transform(self, X):
        """Append one-unique-value columns in `X`.

        Parameters
        ----------
        X : dataframe of shape (n_samples, n_features)
            The input data to complete.

        Returns
        -------
        X_t : dataframe of shape (n_samples, n_non_trivial_features)
            `X` with non_trivial features.
        """
        X_t = X.copy()
        for k,v in self.cols_trivial.items():
            X_t[k]=ComplexFloat(*v[0])
        return X_t[self.columns]


class ColumnMapRotate(BaseEstimator, TransformerMixin):
    """
    Parameters
    ----------
    phi : float, default =0
        rotation angle in rad.

    Attributes
    ----------
    columns : list of strings
        List of column names of columns mapped in `transform`.

    Examples
    --------
    >>> import math
    >>> import pandas as pd
    >>> import numpy as np
    >>> from complexdf_processor.column_transformer import ColumnMapRotate,SeriesProcessor
    >>> sp = SeriesProcessor()
    >>> s1 = sp.series([(1,1),(1,1),(1,1),(1,1),(1,1)])
    >>> s2 = sp.series([(1,1),(-1,1),(1.5,-1.5),(0,2.5),(-3.2,0)])
    >>> s3 = sp.series([(1.2,1.1),(2.1,1),(1.5,-1.5),None,(-3.2,0)])
    >>> X = pd.DataFrame({'s1':s1,'s2':s2,'s3':s3})
    >>> cmr = ColumnMapRotate(math.pi/2)
    >>> cmr.fit_transform(X)
              s1         s2         s3
    0  -1.0+1.0i  -1.0+1.0i  -1.1+1.2i
    1  -1.0+1.0i  -1.0-1.0i  -1.0+2.1i
    2  -1.0+1.0i   1.5+1.5i   1.5+1.5i
    3  -1.0+1.0i  -2.5+0.0i        NaN
    4  -1.0+1.0i  -0.0-3.2i  -0.0-3.2i
    """

    def __init__(self,phi=0):
        self.phi = phi
        self.sp = SeriesProcessor()

    def fit(self, X, y=None):
        self.columns = X.columns
        return self

    def transform(self, X):
        check_is_fitted(self,['columns'])
        X_t = X.copy()
        for col in self.columns:
            X_t[col] = self.sp.rotate(X_t[col],self.phi)
        return X_t

    def inverse_transform(self,X):
        check_is_fitted(self, ['columns'])
        X_t = X.copy()
        for col in self.columns:
            X_t[col] = self.sp.rotate(X_t[col],-self.phi)
        return X_t


class ComplexDfConjugate(BaseEstimator, TransformerMixin):
    """Class calculating conjugate of dataframes



    Returns
    -------

    Examples
    --------
    >>> import math
    >>> import pandas as pd
    >>> from complexdf_processor.column_transformer import ColumnMapRotate,SeriesProcessor
    >>> sp = SeriesProcessor()
    >>> s1 = sp.series([(1,1),(1,1),(1,1),(1,1),(1,1)])
    >>> s2 = sp.series([(1,1),(-1,1),(1.5,-1.5),(0,2.5),(-3.2,0)])
    >>> s3 = sp.series([(1.2,1.1),(2.1,1),(1.5,-1.5),None,(-3.2,0)])
    >>> X = pd.DataFrame({'s1':s1,'s2':s2,'s3':s3})
    >>> cmr = ColumnMapRotate(math.pi/2)
    >>> cmr.fit_transform(X)
              s1         s2         s3
    0  -1.0+1.0i  -1.0+1.0i  -1.1+1.2i
    1  -1.0+1.0i  -1.0-1.0i  -1.0+2.1i
    2  -1.0+1.0i   1.5+1.5i   1.5+1.5i
    3  -1.0+1.0i  -2.5+0.0i        NaN
    4  -1.0+1.0i  -0.0-3.2i  -0.0-3.2i
    """
    def __init__(self):
        self.sp = SeriesProcessor()

    def fit(self,X,y=None):

        """
        Parameters
        ----------
        X : dataframe of shape (n_samples, n_features)
            Input data.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
            Fitted estimator.
        """
        self.columns = X.columns
        return self

    def transform(self,X):
        check_is_fitted(self,['columns'])
        X_t = X.copy()
        for col in self.columns:
            X_t[col] = self.sp.conj(X_t[col])
        return X

    def inverse_transform(self, X):
        X_t = self.transform(X)
        return X_t



