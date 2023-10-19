import numpy as np

class ZNumber:
    def __init__(self, values):
        self.values = np.array(values)

    def __mul__(self, other):
        if isinstance(other, ZNumber):
            # Compute the product of the two Z-numbers using the algebraic product rule
            zprod = np.outer(self.values, other.values)
            zsum = zprod.diagonal(axis1=0, axis2=1)
            return ZNumber(zsum)
        else:
            # Compute the product of a Z-number and a scalar
            return ZNumber(self.values * other)

    def defuzzify(self, method):
        # Defuzzify the Z-number using the specified method
        if method == 'centroid':
            # Compute the centroid of the Z-number using the Sugeno integral formula
            numerator = np.sum(self.values * np.arange(len(self.values)))
            denominator = np.sum(self.values)
            return numerator / denominator
        else:
            raise ValueError(f"Invalid defuzzification method: {method}")

# This implementation provides support for multiplying two Z-numbers and for defuzzifying a Z-number using the centroid method. The __mul__ method implements the algebraic product rule for Z-numbers, and the defuzzify method computes the centroid of the Z-number using the Sugeno integral formula.

# explanation of the Z-number multiplication and defuzzification using the centroid method mathematically:

# Z-Number multiplication:

# Let Z1 = [a1, b1, c1] and Z2 = [a2, b2, c2] be two Z-numbers, where a, b, and c are the lower, middle, and upper bounds of the Z-number, respectively. To multiply these two Z-numbers, we can use the algebraic product rule as follows:

# Z1 * Z2 = [min(a1 * a2, a1 * b2, b1 * a2), min(a1 * c2, c1 * a2, b1 * b2), max(c1 * c2, c1 * b2, b1 * c2)]

# In this multiplication, we take the minimum of all possible combinations of lower and upper bounds of the two Z-numbers to determine the lower and upper bounds of the product, and the minimum of the middle bounds of the two Z-numbers to determine the middle bound of the product.

# Z-Number defuzzification using the centroid method:

# Let Z = [a, b, c] be a Z-number. To defuzzify this Z-number using the centroid method, we can first compute the membership function of the Z-number as follows:

# μ(z) = {0, if z < a
# (z - a) / (b - a), if a <= z < b
# (c - z) / (c - b), if b <= z < c
# 0, if z >= c

# Here, μ(z) represents the degree of membership of the value z in the Z-number.

# Next, we can compute the centroid of the Z-number using the following Sugeno integral formula:

# centroid = ∫(z * μ(z)) / ∫μ(z)

# The numerator represents the weighted sum of all possible values z in the Z-number, where the weight is the degree of membership μ(z), and the denominator represents the total weight of the Z-number. The centroid is the ratio of the numerator to the denominator, and represents the center of mass of the Z-number.
