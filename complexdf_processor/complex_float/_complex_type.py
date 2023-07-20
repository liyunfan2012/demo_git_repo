from math import sqrt,atan,pi,cos,sin
class ComplexFloatCore:

    def __init__(self,re=0,im=0,mod=None,arg=None):
        if bool(mod) and bool(arg):
            self.re = round(mod * cos(arg),15)
            self.im = round(mod * sin(arg),15   )
        else:
            self.re = re
            self.im = im
    def __str__(self):
        if self.im>=0:
            strfmt=str(self.re)+'+'+str(self.im)+'i'
        else:
            strfmt = str(self.re) + '-' + str(-self.im) + 'i'
        return strfmt

    def __repr__(self):
        if self.im >= 0:
            strfmt = str(self.re) + '+' + str(self.im) + 'i'
        else:
            strfmt = str(self.re) + '-' + str(-self.im) + 'i'
        return strfmt

    def __eq__(self,x):
        return self.re == x.re and self.im == x.im
    @property
    def mod(self):
        return sqrt(self.re * self.re + self.im * self.im)
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
    def tuple(self):
        return (self.re,self.im)
    @property
    def conj(self):
        return ComplexFloatCore(self.re,-self.im)

