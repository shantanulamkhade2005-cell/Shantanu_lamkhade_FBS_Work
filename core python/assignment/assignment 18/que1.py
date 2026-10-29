class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return str(self.real) + " + " + str(self.imag) + "i"

    def __del__(self):
        print("Object destroyed")


c1 = Complex(5, 3)
c2 = Complex(2, 1)

print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)

