
from utils.decorators import timed


# i use the timed multiple runs decorator here because i wanted to make a decorator that took a param
@timed
def sum_multiples_of_3_or_5_in_range_naive(stop: int):
    """ This function sums the numbers divisble by either 3 or 5 up to the input number naively by iterating through
    and performing logic on each number in the range

    >>> sum_multiples_of_3_or_5_in_range_naive(10) # doctest:+ELLIPSIS
    took [...s] sum_multiples_of_3_or_5_in_range_naive(10) -> 23
    23
    >>> sum_multiples_of_3_or_5_in_range_naive(1000) # doctest:+ELLIPSIS
    took [...s] sum_multiples_of_3_or_5_in_range_naive(1000) -> 233168
    233168
    """
    return sum(n for n in range(stop) if n % 3 == 0 or n % 5 == 0)


@timed
def sum_multiples_of_3_or_5_in_range_steps(stop: int):
    """ This function sums the numbers divisble by either 3 or 5 up to the input number in a better way because you can
    skip a large amount of numbers by using the step argument of the range and subtracting the overlap from the 2 sums

    >>> sum_multiples_of_3_or_5_in_range_steps(10) # doctest:+ELLIPSIS
    took [...s] sum_multiples_of_3_or_5_in_range_optimized(10) -> 23
    23
    >>> sum_multiples_of_3_or_5_in_range_steps(1000) # doctest:+ELLIPSIS
    took [...s] sum_multiples_of_3_or_5_in_range_optimized(1000) -> 233168
    233168
    """
    return sum(n for n in range(0, stop, 3)) + sum(n for n in range(0, stop, 5)) - sum(n for n in range(0, stop, 15))


@timed
def sum_multiples_of_3_or_5_in_range_direct(stop: int):
    """ This function sums the numbers divisble by either 3 or 5 up to the input number in a better way because you can
    directly calculate the sum of the arithmetic series without needing to iterate

    >>> sum_multiples_of_3_or_5_in_range_direct(10) # doctest:+ELLIPSIS
    took [...s] sum_multiples_of_3_or_5_in_range_direct(10) -> 23
    23
    >>> sum_multiples_of_3_or_5_in_range_direct(1000) # doctest:+ELLIPSIS
    took [...s] sum_multiples_of_3_or_5_in_range_direct(1000) -> 233168
    233168
    """
    return arithmetic_series(0, stop, 3) + arithmetic_series(0, stop, 5) - arithmetic_series(0, stop, 15)


@timed
def arithmetic_series(start, stop, step):
    """

    >>> arithmetic_series(0, 10, 3)
    took [...s] arithmetic_series(0, 10, 3) -> 18
    18

    >>> arithmetic_series(0, 10, 5)
    took [...s] arithmetic_series(0, 10, 5) -> 5
    5

    :param start:
    :param stop:
    :param step:
    :return:
    """
    stop = stop - 1
    stop_for_step = stop // step * step
    number_of_terms = (stop_for_step - 0) // step
    sum_of_extrema = step + (stop_for_step - start)
    return number_of_terms * sum_of_extrema // 2


if __name__ == '__main__':
    """
    This __main__ serves as a place where I can call doctest to verify my functions return the right output, and a place
    where I test how long my functions take to solve the problem for 1 million and to check their results against 
    each other:
    example run on a 2016 acer i5 laptop---
    took [0.11183410s] sum_multiples_of_3_or_5_in_range_naive(1000000) -> 233333166668
    took [0.04134060s] sum_multiples_of_3_or_5_in_range_steps(1000000) -> 233333166668
    took [0.00000260s] arithmetic_series(0, 1000000, 3) -> 166666833333
    took [0.00000090s] arithmetic_series(0, 1000000, 5) -> 99999500000
    took [0.00000070s] arithmetic_series(0, 1000000, 15) -> 33333166665
    took [0.00003270s] sum_multiples_of_3_or_5_in_range_direct(1000000) -> 233333166668
    ---
    
    a tenth of a second isnt bad for a naive implement, but the direct arithmetic sum taking 3 millionths of a second
    is orders of magnitude faster. Depending on how often this is called the effort to program the direct calculation
    is very worth it
    """
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

    one_million = 1000000
    sum_multiples_of_3_or_5_in_range_naive(one_million)
    sum_multiples_of_3_or_5_in_range_steps(one_million)
    sum_multiples_of_3_or_5_in_range_direct(one_million)
