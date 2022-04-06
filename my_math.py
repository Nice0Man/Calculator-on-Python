import math as common_math
from functools import reduce as common_reduce


def lcm(denominators):
    """
    least common multiple of variable list [x,y,...]
    input format: lcm([100,200,300,...])
    """
    return common_reduce(lambda a, b: a * b // common_math.gcd(a, b), denominators)


def cqeq(a, b, c):
    """ calculating roots of a quadratic equation """
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + common_math.sqrt(discr)) / (2 * a)
        x2 = (-b - common_math.sqrt(discr)) / (2 * a)
        return x1, x2
    elif discr == 0:
        x = -b / (2 * a)
        return x
    else:
        return "No relevant roots of the equation exist"


def tobase(num, base):
    """ conversion to a number system """
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = alpha[num % base]
    while num >= base:
        num = num // base
        b += alpha[num % base]
    return b[::-1]


def rparea(lngth, n):
    """ area of a regular polygon """
    return (lngth ** 2 * n) / round(4 * common_math.tan(common_math.pi / n))
