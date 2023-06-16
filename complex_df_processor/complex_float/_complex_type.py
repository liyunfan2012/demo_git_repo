from math import sqrt,atan,pi
class ComplexFloatCore:

    def __init__(self,re=0,im=0,z=None,arg=None):
        if bool(z) and bool
        self.re = re
        self.im = im

    def __str__(self):
        return str(self.re)+"+"+str(self.im)+"j"

    @property
    def mod(self):
        return sqrt(self.re*self.re+self.im*self.im)
    @property
    def arg(self):
        re, im = self.re, self.im
        if re == 0:
            if im > 0:
                phi = pi/2
            elif im < 0:
                phi = -pi/2
            else:
                phi = None
        else:
            if re > 0 and im < 0:
                phi = atan(im/re) - pi
            elif re < 0 and im >=0:
                phi = atan(im/re) + pi
            else:
                phi = atan(im/re)
        return phi

    @property
    def conj(self):
        return ComplexFloatCore(self.re,-self.im)

class ComplexFloatModArg(ComplexFloatCore):



