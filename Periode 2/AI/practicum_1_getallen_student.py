#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""
# How about modules like 'numba'? Could speed up the code by **10.

naam = "Jasper van den Bremer"
klas = "V1C"
studentnummer = 1799441

# I hate Math.

# check is even; divide/2 and return remainder remainder 0 means even, 1 means odd so == 0 is true and 1 is false.
def is_even(n):
    return n % 2 == 0


# could be re-used but writing it out was a good exercise to actually understand everything.

# int number, if not smaller or equal to real, the next full number should be real-1
def floor(real):
    if int(real) <= real:
        return int(real)
    else:
        return int(real) - 1


# return int(n // 1) is also an option
# // returns the next smallest full number, be sure to int it as that's the expected return type.
# int() and int()-1 wont work correctly.

# int real, if not greater or equal to real, the next full number should be real +1
def ceil(real):
    if int(real) >= real:
        return int(real)
    else:
        return int(real) + 1


# return int(-1 * n // 1 * -1) is also an option
# returns the next smallest full number but before and after are inverted so you get the ceiling

# get the divisors of a number
def div(n):
    divisors = []
    for i in range(1, n + 1):  # loop start to end
        if int(n % i) == 0:  # if the remainder of n divided by i is 0
            divisors.append(int(i))
    return sorted(divisors)


# check if number is prime
def is_prime(n):
    if div(n) == [1, n]:
        return True
    return False


# calculate the primes below a number
def primes(num):
    primelist = []
    if num > 1:
        for i in range(2, num):
            if is_prime(i):
                primelist.append(i)

    return sorted(primelist)


def primefactors(n):
    """   https://youtu.be/XGbOiYhHY2c?t=263 saves headaches  """

    factors = []
    i = 2

    #  number is smaller than 2, return empty list
    if n < 2:
        return factors

    #  2 is the only even prime so we can count by 1
    #  all other primes are odd so we can count by 2 below
    while i == 2:  # Can be multiple factors of 2, 64 for example. Will continue below if odd primes are reached.
        if n % i == 0:  # check if the number (i) is a factor
            factors.append(i)
            n //= i
        else:
            i += 1  # count up by one, exits the loop and starts the next iteration which will be faster.

    #  count up until we reach n where n is always divided by I per iteration because its the new number.
    #  if n % i true then its not a factor so we can count up by 2 as all primes above 2 are odd.
    while i <= n:  # will automatically stop if the last number is reached.
        if n % i == 0:  # check if the number (i) is a factor
            factors.append(i)
            n //= i  # update n
        else:
            i += 2  # count by 2 as all primes above 2 are odd.

    return sorted(factors)


# Get the greatest common divisor of two numbers
def gcd(a, b):
    """    https://en.wikipedia.org/wiki/Euclidean_algorithm#Implementations
    Provides pseudo code for the Euclidean algorithm.
    function gcd(a, b)
    while b
        t = b
        b = a % b
        a = t
    return a

    t is a temporary variable to store the value of b but this can be made in one line.
    this makes
    t = b and a = t
    Can be equal to a = b if this is combined with b = a % b on the same line.
    This is because a, b = b, a would swap the values of a and b while separate lines would require a temp value.

    a, b = b, a % b

    At the end, B will be false and the loop will stop.
    Causing the return statement which should be a. According to the pseudo code and the Euclidean algorithm. IDK.
    """

    while b:
        a, b = b, a % b  # loads of text, small code.
    return a


# Get the least common multiple of two numbers
def lcm(a, b):
    """    https://www.youtube.com/watch?v=fjdeo6anRY4
    Example: a,b = 2,3
    2,4,6*,8,10,12*,14,16,18*
    3,6*,9,12*,15,18*,21,24

    2/gcd = 2
    3/gcd = 3

    We all know how to multiply fractions so...
    2*3 = 6
    gcd(2, 3) = 1
    6 / 1 = 6
    
    So a * b / gcd(a, b) = 6
    // for flooring, causing it to always be an int
    
    """

    return a * b // gcd(a, b)  # again text for little.



def add_frac(n1, d1, n2, d2):
    """
        a c   a*d + b*c
        -+- > ---------
        b d   b*d

        a*d + b*c
        b*d

        n1, d1, n2, d2
        a , b , c , d

        n1*d2 + d1*n2
        d1*d2
    """
    #  one line, less variables
    n1, d1 = n1*d2 + d1*n2, d1*d2

    #  reduce the fraction with the gcd
    g = gcd(n1, d1)
    n1, d1 = n1//g, d1//g
    return n1, d1


def __main():
    # devcode here // I added this to make it easier for me to debug


    __runtest()
    return

"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.

    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_is_even():
    testcases = [
        ((1,), False),
        ((2,), True),
        ((3,), False),
        ((4,), True)
    ]

    for case in testcases:
        __my_assert_args(is_even, case[0], case[1])


def test_floor():
    testcases = [
        ((1.05,), 1),
        ((1.95,), 1),
        ((-1.05,), -2),
        ((-1.95,), -2),
        ((0.05,), 0),
        ((-0.05,), -1),
        ((0.0,), 0),
        ((1.0,), 1),
        ((-1.0,), -1)
    ]

    for case in testcases:
        __my_assert_args(floor, case[0], case[1])


def test_floor_simulated():
    import random
    import math

    for _ in range(10):
        x = random.uniform(-10.0, 10.0)
        __my_assert_args(floor, (x,), math.floor(x))


def test_ceil():
    testcases = [
        ((1.05,), 2),
        ((1.95,), 2),
        ((-1.05,), -1),
        ((-1.95,), -1),
        ((0.05,), 1),
        ((-0.05,), 0),
        ((0.0,), 0),
        ((1.0,), 1),
        ((-1.0,), -1)
    ]

    for case in testcases:
        __my_assert_args(ceil, case[0], case[1])


def test_ceil_simulated():
    import random
    import math

    for _ in range(10):
        x = random.uniform(-10.0, 10.0)
        __my_assert_args(ceil, (x,), math.ceil(x))


def test_div():
    testcases = [
        ((1,), [1]),
        ((2,), [1, 2]),
        ((3,), [1, 3]),
        ((4,), [1, 2, 4]),
        ((8,), [1, 2, 4, 8]),
        ((12,), [1, 2, 3, 4, 6, 12]),
        ((19,), [1, 19]),
        ((25,), [1, 5, 25]),
        ((929,), [1, 929]),
        ((936,), [1, 2, 3, 4, 6, 8, 9, 12, 13, 18, 24, 26, 36, 39, 52, 72, 78, 104, 117, 156, 234, 312, 468, 936])
    ]

    for case in testcases:
        __my_assert_args(div, case[0], sorted(case[1]))


def test_is_prime():
    testcases = [
        ((1,), False),
        ((2,), True),
        ((3,), True),
        ((4,), False),
        ((5,), True),
        ((6,), False),
        ((9,), False),
        ((29,), True)
    ]

    for case in testcases:
        __my_assert_args(is_prime, case[0], case[1])


def test_primefactors():
    testcases = [
        ((-1,), []),
        ((1,), []),
        ((2,), [2]),
        ((3,), [3]),
        ((4,), [2, 2]),
        ((8,), [2, 2, 2]),
        ((12,), [2, 2, 3]),
        ((2352,), [2, 2, 2, 2, 3, 7, 7]),
        ((9075,), [3, 5, 5, 11, 11])
    ]

    for case in testcases:
        __my_assert_args(primefactors, case[0], sorted(case[1]))


def test_primes():
    testcases = [
        ((1,), []),
        ((2,), []),
        ((3,), [2]),
        ((4,), [2, 3]),
        ((5,), [2, 3]),
        ((6,), [2, 3, 5]),
        ((30,), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    ]

    for case in testcases:
        __my_assert_args(primes, case[0], sorted(case[1]))


def test_gcd():
    testcases = [
        ((60, 1), 1),
        ((60, 6), 6),
        ((60, 7), 1),
        ((60, 8), 4),
        ((60, 9), 3),
        ((60, 11), 1),
        ((60, 13), 1),
        ((60, 14), 2),
        ((60, 15), 15),
        ((60, 16), 4),
        ((60, 18), 6)
    ]

    for case in testcases:
        __my_assert_args(gcd, case[0], case[1])


def test_gcd_simulated():
    import random
    import math

    for _ in range(10):
        a = random.randrange(3, 201, 3)
        b = random.randrange(4, 201, 4)
        __my_assert_args(gcd, (a, b), math.gcd(a, b))


def test_lcm():
    testcases = [
        ((60, 1), 60),
        ((60, 2), 60),
        ((60, 7), 420),
        ((60, 8), 120),
        ((60, 9), 180),
        ((60, 10), 60),
        ((60, 11), 660),
        ((60, 18), 180)
    ]

    for case in testcases:
        __my_assert_args(lcm, case[0], case[1])


def test_add_frac():
    testcases = [
        ((1, 3, 1, 5), (8, 15)),
        ((1, 2, 1, 4), (3, 4)),
        ((2, 3, 3, 2), (13, 6)),
        ((1, 2, 1, 6), (2, 3)),
        ((3, 4, 1, 6), (11, 12)),
        ((1, 6, 3, 4), (11, 12)),
        ((1, 2, 1, 3), (5, 6)),
        ((1, 2, 2, 3), (7, 6))
    ]

    for case in testcases:
        __my_assert_args(add_frac, case[0], case[1])


def __runtest():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    import os
    os.system("")

    try:
        print("\x1b[32m")  # Groene tekstkleur
        test_id()

        test_is_even()
        print("Je functie is_even(n) werkt goed!")

        test_floor()
        test_floor_simulated()
        print("Je functie floor(real) werkt goed!")

        test_ceil()
        test_ceil_simulated()
        print("Je functie ceil(real) werkt goed!")

        test_div()
        print("Je functie div(n) werkt goed!")

        test_is_prime()
        print("Je functie is_prime(n) werkt goed!")

        test_primefactors()
        print("Je functie primefactors(n) werkt goed!")

        test_primes()
        print("Je functie primes(num) werkt goed!")

        test_gcd()
        test_gcd_simulated()
        print("Je functie gcd(a, b) werkt goed!")

        test_lcm()
        print("Je functie lcm(a, b) werkt goed!")

        test_add_frac()
        print("Je functie add_frac(n1, d1, n2, d2) werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")


    except AssertionError as ae:
        print("\x1b[31m")  # Rode tekstkleur
        print(ae)

    print("\x1b[0m")  # Reset tekstkleur


if __name__ == '__main__':
    __main()
