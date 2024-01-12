import math
class c:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
        self.mod = (self.a**2 + self.b**2) ** 0.5
        self.conjugate = (self.a, -self.b)
        self.polar = ((self.a**2 + self.b**2) ** 0.5, math.atan(self.b/self.a))
    
    """
    Iterable method to allow unpacking, can be useful for quickly extracting components.
    Returns iterable object of self.a and self.b
    """
    def __iter__(self):
        return iter((self.a,self.b))
    """
    Method to add two complex numbers (can add complex to float, int or complex).
    Returns as (a,b) such that a + bi.
    """
    def __add__(self, c2):
        if isinstance(c2, (float, int, c)):
            a1,b1,a2,b2 = self.a,self.b,0,0
            if isinstance(c2, c):
                a2,b2 = c2.a, c2.b
            else:
                a2 = c2
            return (a1+a2, b1+b2)
        else:
            print("**| ERROR: when multiplying with a complex number you must use another complex number or integer or float.")
            raise ValueError("ERROR!")
        
    """
    Method for subtracting complex numbers. Allows use of integers floats, and complex.
    Returns as (a,b) such that the result, c = a + bi.
    """
    def __sub__(self, c2):
        if isinstance(c2, (float, int, c)):
            a1,b1,a2,b2 = self.a, self.b, 0, 0
            if isinstance(c2, c):
                a2,b2 = c2.a,c2.b
            else:
                a2 = c2
            return (a1-a2,b1-b2)
    """
    For the class complex, the __mul__ redefines the * operator. Works for complex*int, complex_float, and complex*complex.
    Returns as (a,b) such that the result is a + bi.
    """
    def __mul__(self, product):
        if isinstance(product, complex):
            #then do the multiplication of a complex
            return (self.a*product.a - self.b*product.b, self.a*product.b + self.b*product.a)
        #recall that an integer is a complex number with a zero for the complex scalar.
        elif isinstance(product, (int,float)):
            return (self.a*product, self.b*product)
        else:
            print("**| ERROR: when multiplying with a complex number you must use another complex number or integer or float.")
            raise ValueError("ERROR!")
        
    def __rmul__(self, product):
        self.__mul__(product)
    
    """
    Redefines division for complex numbers. Works for floats, ints and complex numbers.
    Returns as (a,b) where complex result = a + bi
    """
    def __truediv__(self, div):
        if isinstance(div, (int,float,c)):
            #calculate dividend
            if isinstance(div, (int,float)):
                a1, b1, a2, b2 = self.a, self.b, div, 0
            else:
                a1, b1, a2, b2 = self.a, self.b, div.a, div.b
            bottom = a2**2 + b2**2
            return ((a1*a2 + b1*b2) / bottom, (a2*b1 - a1*b2) / bottom)
        else:
            print("**| ERROR: when dividing with a complex number you must use another complex number or integer or float.")
            raise ValueError("ERROR!")
        
    
c1 = c(2,2)
c2 = c(1,1)
c3 = c(1,1)
print(c3.polar)
print(c1/c2)