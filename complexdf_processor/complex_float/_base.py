from ._complex_type import ComplexFloatCore
from math import sqrt,atan,pi,cos,sin
class ComplexFloat(ComplexFloatCore):
    def __add__(self, x):
        if isinstance(x,ComplexFloatCore):
            re, im = self.re + x.re, self.im + x.im
        elif isinstance(x,float):
            re, im = self.re + x,self.im
        else:
            re, im = self.re, self.im
        return ComplexFloat(re,im)

    def __sub__(self, x):
        if isinstance(x,ComplexFloatCore):
            re, im = self.re - x.re, self.im-x.im
        elif isinstance(x,float):
            re, im = self.re - x, self.im
        else:
            re, im = self.re, self.im
        return ComplexFloat(re, im)


    def __mul__(self, x):
        if isinstance(x,ComplexFloatCore):
            re = self.re*x.re -self.im * x.im
            im = self.re*x.im + self.im * x.re
        elif isinstance(x,float):
            re, im = self.re * x, self.im * x
        else:
            re, im = self.re, self.im
        return ComplexFloat(re,im)

    def __truediv__(self, x):
        if isinstance(x,ComplexFloatCore):
            if x.mod == 0:
                z = None
            else:
                z = ComplexFloat(mod=self.mod/x.mod,
                                 arg=self.arg - x.arg)
        elif isinstance(x,float):
            z = ComplexFloat(self.re/x,self.im/x)
        return z



    def rotate(self,phi):
        return self * ComplexFloat(mod=1,arg=phi)

    def conjugate(self):
        self.im = - self.im



