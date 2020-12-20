import math
from timer import *


class Vector(object):
    def __init__(self, *args):
        """ Create a vector, example: v = Vector(1,2,3) """
        if len(args)==0: 
            self.values = (0,0,0)
        else: 
            self.values = args
    
    def abs(self):
        """ Returns the norm (length, magnitude) of the vector """
        return math.sqrt(sum( x*x for x in self ))
   
    @timer
    def normalize(self):
        """ Returns a normalized unit vector """
        norm = self.abs()
        normed = tuple( float('{:.3f}'.format(x / norm)) for x in self )
        return self.__class__(*normed)
    
    def inner(self, vector):
        """ Returns the dot product (inner product) of self and another vector
        """
        if not isinstance(vector, Vector):
            raise ValueError('The dot product requires another vector')
        return sum(a * b for a, b in zip(self, vector))
    
    def __mul__(self, other):
        """ Returns the dot product of self and other if multiplied
            by another Vector.  If multiplied by an int or float,
            multiplies each component by other.
        """
        if isinstance(other, Vector):
            return self.inner(other)
        elif isinstance(other, (int, float)):
            product = tuple( a * other for a in self )
            return self.__class__(*product)
        else:
            raise ValueError("Multiplication with type {} not supported".format(type(other)))

    def __rmul__(self, other):
        """ Called if 4 * self for instance """
        return self.__mul__(other)            
    
    def __imul__(self, other):
        if isinstance(other, Vector):
            self = self.inner(other)
        elif isinstance(other, (int, float)):
            product = tuple( a * other for a in self )
            self = self.__class__(*product)
        else:
            raise ValueError("Multiplication with type {} not supported".format(type(other)))
        return self
            
    def __add__(self, other):
        """ Returns the vector addition of self and other """
        if isinstance(other, Vector):
            added = tuple( a + b for a, b in zip(self, other) )
        else:
            raise ValueError("Addition with type {} not supported".format(type(other)))
        
        return self.__class__(*added)

    def __iadd__(self, other):
        """ Returns the vector addition of self and other """
        if isinstance(other, Vector):
            added = tuple( a + b for a, b in zip(self, other) )
        else:
            raise ValueError("Addition with type {} not supported".format(type(other)))
        
        self = self.__class__(*added)
        return self
    
    def __sub__(self, other):
        """ Returns the vector difference of self and other """
        if isinstance(other, Vector):
            subbed = tuple( a - b for a, b in zip(self, other) )
        else:
            raise ValueError("Subtraction with type {} not supported".format(type(other)))
        
        return self.__class__(*subbed)
    
    def __isub__(self, other):
        if isinstance(other, Vector):
            subbed = tuple( a - b for a, b in zip(self, other) )
        else:
            raise ValueError("Subtraction with type {} not supported".format(type(other)))
        
        self = self.__class__(*subbed)
        
        return self

    def __matmul__(self, other):
        """ Returns cross product of self and other"""
        if isinstance(other, Vector):
            x1, y1, z1 = self.values
            x2, y2, z2 = other.values
            s = [y1 * z2 - z1 * y2, z1 * x2 - x1 * z2, x1 * y2 - x2 *y1]
            cross_product = tuple(s)
        else:
            raise ValueError("Cross with type {} not supported".format(type(other)))

        return self.__class__(*cross_product)     
    
    def __imatmul__(self, other):
        if isinstance(other, Vector):
            x1, y1, z1 = self.values
            x2, y2, z2 = other.values
            s = [y1 * z2 - z1 * y2, z1 * x2 - x1 * z2, x1 * y2 - x2 *y1]
            cross_product = tuple(s)
        else:
            raise ValueError("Cross with type {} not supported".format(type(other)))

        self = self.__class__(*cross_product)
        
        return self

    def __neg__(self):
        negative = tuple(-x for x in self.values)

        return self.__class__(*negative)

    def __iter__(self):
        return self.values.__iter__()
    
    
    def __getitem__(self, key):
        return self.values[key]
        
    def __repr__(self):
        return str(self.values)

    def __len__(self):
        return len(self.values)

    def __eq__(self, other):
        """ Checks if the vectors are equal """
        if isinstance(other, Vector):
            while True:
                for a, b in zip(self, other):
                   if a != b: 
                      return False
                return True      
        else:
            raise ValueError("Equality with type {} not supported".format(type(other)))
        
        