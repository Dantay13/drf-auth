def fibonacci(n):
    """
    to get the fibonacci sequence using recursion that returns the nth value.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    Return the nth value in the Lucas series.
    The Lucas series is similar to the Fibonacci series, but starts with 2 and 1
    instead of 0 and 1.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, first=0, second=1):
    """
    Return the nth value in a series based on the given first two values.
    If first and second are 0 and 1, respectively, this function will return the
    nth value in the Fibonacci series. If first and second are 2 and 1, respectively,
    this function will return the nth value in the Lucas series.

    Parameters:
    -----------
    n : int
        The index of the value to return in the series.
    first : int
        The first value in the series. Defaults to 0 for the Fibonacci series and 2 for the Lucas series.
    second : int
        The second value in the series. Defaults to 1 for the Fibonacci series and 1 for the Lucas series.

    Returns:
    --------
    int
        The nth value in the series based on the given first two values.
    """
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)
