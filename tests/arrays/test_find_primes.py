import pytest
import time
from src.arrays.find_primes import find_primes
from tests.strings.string_test_utils import print_long_string


@pytest.fixture(scope="session", autouse=True)
def before_session():
    print()
    print()
    print("=================")
    print("Test find_primes:")
    print("=================")


def test_up_to_1():
    expected = []
    do_test(1, expected)


def test_up_to_2():
    expected = [2]
    do_test(2, expected)


def test_up_to_1000():
    expected = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
        127,
        131,
        137,
        139,
        149,
        151,
        157,
        163,
        167,
        173,
        179,
        181,
        191,
        193,
        197,
        199,
        211,
        223,
        227,
        229,
        233,
        239,
        241,
        251,
        257,
        263,
        269,
        271,
        277,
        281,
        283,
        293,
        307,
        311,
        313,
        317,
        331,
        337,
        347,
        349,
        353,
        359,
        367,
        373,
        379,
        383,
        389,
        397,
        401,
        409,
        419,
        421,
        431,
        433,
        439,
        443,
        449,
        457,
        461,
        463,
        467,
        479,
        487,
        491,
        499,
        503,
        509,
        521,
        523,
        541,
        547,
        557,
        563,
        569,
        571,
        577,
        587,
        593,
        599,
        601,
        607,
        613,
        617,
        619,
        631,
        641,
        643,
        647,
        653,
        659,
        661,
        673,
        677,
        683,
        691,
        701,
        709,
        719,
        727,
        733,
        739,
        743,
        751,
        757,
        761,
        769,
        773,
        787,
        797,
        809,
        811,
        821,
        823,
        827,
        829,
        839,
        853,
        857,
        859,
        863,
        877,
        881,
        883,
        887,
        907,
        911,
        919,
        929,
        937,
        941,
        947,
        953,
        967,
        971,
        977,
        983,
        991,
        997,
    ]
    do_test(1000, expected)


def do_test(n, expected):
    print(f"\nPrimes up to {n}:")

    start_time = time.monotonic()
    primes = find_primes(n)
    end_time = time.monotonic()

    elapsed_time = end_time - start_time
    microseconds = int(elapsed_time * 1_000_000)

    print(print_long_string(str(primes)))
    print(f"Elapsed time = {microseconds} microseconds")

    assert primes == expected
