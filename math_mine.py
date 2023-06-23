
class Mathematics:
    """
    A list of simple mathematical functions
    and operations
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y  

    def divide(self):
        return self.x / self.y 
    # =======================================

    def modulus(x, y):
        return x % y 
    
    def power(x, y):
        return x ** y
    
    def reciprocal(x, y):
        return 1 / (x ** y) 
    # =======================================

    def sum(x, y):
        r = 0
        for i in range(x, y+1):
            r += i 
        return r
    
    def factorial(x, y):
        r = 1
        for i in range(x, y+1):
            r *= i
        return r 

    def gcf(x, y):
        gcfs = []
        for a in range(1, x+1):
            for b in range(1, y+1):
                if a == b:
                    gcfs.append(a)

        return gcfs
    # =======================================
    
    # m in kg; h in metres
    def bmi(m, h):
        bmi = m / (h ** 2)
        return bmi

# *****************************************
# use __doc__ to view the documentation string in the program
# use the help function tool; print(help(a))


a = Mathematics(2, 3)
# print(a.__doc__)
# print(help(a))

print(a.add())
print(a.subtract())
print(a.multiply())
print(a.divide())
