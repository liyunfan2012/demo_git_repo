from ._complex_type import ComplexFloatCore
class ComplexFloat(ComplexFloatCore):
    def __add__(self, x):
        if isinstance(x,ComplexFloatCore):
            return ComplexFloat(self.re+x.re,self.im+x.im)
        elif isinstance(x,float):
            return ComplexFloat(self.re + x, self.im)

    def __sub__(self, x):
        if isinstance(x,ComplexFloatCore):
            return ComplexFloat(self.re-x.re,self.im-x.im)

    def rotate(self,phi):



