import time
from functools import wraps


def timed(func):
    """
    create a timing decorator function, use @timed and it will print out the time the calls to that func take

    heavily inspired by Luciano Ramalho's example 9-16 from fluent python
    """
    @wraps(func)  # improves debugging
    def timed_call(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        time_taken = time.perf_counter() - start_time
        name = func.__name__
        arg_list = [repr(arg) for arg in args]
        arg_list.extend(f'{k}={v!r} 'for k, v in kwargs.items())
        arg_str = ", ".join(arg_list)
        print(f'took [{time_taken:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return timed_call


class TimedMultipleRuns(object):

    def __init__(self, number_of_runs: int):
        """
        init so decorator can take args
        :param number_of_runs: the number of times to run the function in a loop through for timing
        """
        self.number_of_runs = number_of_runs

    def __call__(self, func):
        """
        the dunder call that allows the decorator to work

        :param func: the function ref we will call multiple times in a loop to time
        """
        @wraps(func)  # improves debugging
        def wrapped_func(*args, **kwargs):
            total_time = 0
            result = None
            for _ in range(self.number_of_runs):
                start_time = time.perf_counter()
                result = func(*args, **kwargs)
                total_time += time.perf_counter() - start_time
            name = func.__name__
            arg_list = [repr(arg) for arg in args]
            arg_list.extend(f'{k}={v!r} ' for k, v in kwargs.items())
            arg_str = ", ".join(arg_list)
            print(f'took [{total_time:0.8f}s] to run {name}({arg_str}) {self.number_of_runs} times')
            return result
        return wrapped_func
