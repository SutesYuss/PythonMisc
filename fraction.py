
"""Contains a class that represents a Fraction (i.e., a rational number).
Author: Sudi Yussuf
"""
from fractions import Fraction as frac
import math
from functools import total_ordering 
# TODO: Implement the class Fraction
#instantiates the class
class Fraction:
  #variables here are class variables
    """A rational number.
    Fraction should have no public instance variables.
    """
    #special case of an instance method. starts initioalization
    #self is an instance of the class
    def __init__(self, *args):
        """Produces the fraction n/d in reduced form.
        By "reduced form", we mean that in the produced fraction, the numerator
        and denominator are relatively prime.
        """
        if len(args) >1:
          denominator = math.gcd(args[0], args[1]);
          self.num = args[0] // denominator;
          self.d = args[1] // denominator;
          self = frac(self.num/self.d);
        else:
          self = frac(args[0])
        
        
    def mixed_number(self) -> str:
        """Returns a string representation of self in mixed number form.
        For example, if self is 5/3, mixed_number should return "1 2/3".
        """
        numer = self.num // self.d
        recip = self.num % self.d

        return(f"{numer} {recip}/{self.d}");
          
      
    def __repr__(self):
        """Returns a string that is [numerator]'/'[denominator].
        __repr__ is called by the builtin function repr, or by print if
        there is no definition for __str__.
        """
        return(f"{self.num}/{self.d}");
        
    def __str__(self):
        """Returns a string that is [numerator]'/'[denominator].
        __str__ is called by the builtin print function.
        """
        str = f"{self.num}/{self.d}";
        return str;
        
    def __eq__(self, other: 'Fraction') -> bool:
        """Reports whether self is the same number as other.
        __eq__ is called by the equality operator, e.g., frac1 == frac2.
        """
        return (self.num/self.d) == (other.num/other.d);

    def __neg__(self) -> 'Fraction':
        """Returns the negation of self.
        __neg__ is called by the unary minus operator, e.g., -frac.
        """
        return self * -1;
      
    def __invert__(self) -> 'Fraction':
        """Returns the reciprocal of self.
        __invert__ is called by the unary tilde operator, e.g., ~frac.
        """
        
        return frac(self.d/self.num);
        
    def __add__(self, other: 'Fraction') -> 'Fraction':
        """Returns the sum of self and other.
        __add__ is called by the binary plus operator, e.g., frac1 + frac2.
        """
  
        return frac(self.num,self.d) + frac(other.num,other.d);
      
    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """Returns the product of self and other.
        __mul__ is called by the binary times operator, e.g., frac1 * frac2.
        """
        return frac(self.num,self.d) * frac(other.num,other.d);
    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """Returns the difference of self and other.
        __sub__ is called by the binary minus operator, e.g., frac1 - frac2.
        """
        return frac(self.num/self.d) - frac(other.num/other.d);
    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """Returns the quotient of self and other.
        __div__ is called by the binary division operator, e.g., frac1 / frac2.
        """
        return frac(self.num,self.d) / frac(other.num,other.d);

    def __lt__(self,other: 'Fraction')-> 'Fraction':
      return (self.num/self.d) < (other.num/other.d);

    def __le__(self,other: 'Fraction')-> 'Fraction':
      return (self.num/self.d) <= (other.num/other.d);

    def __ge__(self,other: 'Fraction')-> 'Fraction':
      return (self.num/self.d) >= (other.num/other.d);

    def __ne__(self,other: 'Fraction')-> 'Fraction':
      return (self.num/self.d) != (other.num/other.d);

    @classmethod
    def from_str(cls, str_rep: str) -> 'Fraction':
      try:
          fraction = frac(str_rep)
      except ValueError:
        print("Oops, this string cannot be converted to a fraction")
      return fraction


#Initialization and printing of a fraction with value 0. Hint: Such a fraction should have denominator 1 in reduced form
# s = Fraction(0,2);
# print(s);

# #Initialization and printing of a fraction with numerator and denominator that are relatively prime
# s = Fraction(5,7);
# print(s);

# #Initialization and printing of a fraction with nonzero numerator and denominator that are not relatively prime
# s = Fraction(8,6);
# print(s);

# #The sum of two fractions with the same denominator
# s = Fraction(5,6);
# p = Fraction(7,6);

# print(s + p);


# #The sum of two fractions with different denominators
# s = Fraction(8,6);
# p = Fraction(7,5);

# print(s + p);

#Use functools.total_ordering to enable Fractions to be compared with any of the comparison operators in 


# boo = s < p;
# print(boo);

# boo = s > p;
# print(boo);

# boo = s != p;
# print(boo);

# boo = s == p;
# print(boo);

# boo = s >= p;
# print(boo);

# boo = s <= p;
# print(boo);


# s = s.from_str('6/7')
# print(s)
