import time
import functools

from django.db import connection, reset_queries


def debugger_queries(func):
    """Basic function to debug queries."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("func: ", func.__name__)
        reset_queries()

        start = time.time()
        start_queries = len(connection.queries)

        result = func(*args, **kwargs)

        end = time.time()
        end_queries = len(connection.queries)

        print("queries:", end_queries - start_queries)
        print("queries:", start_queries)
        print("queries:", end_queries)
        print("took: %.2fs" % (end - start))
        return result

    return wrapper