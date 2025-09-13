class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        def parse_complex(s):
            parts = s.split('+')
            real = int(parts[0])
            imag = int(parts[1][:-1])
            return real, imag

        a, b = parse_complex(num1)
        c, d = parse_complex(num2)
        real_part = a * c - b * d
        imag_part = a * d + b * c
        return str(real_part) + "+" + str(imag_part) + "i"