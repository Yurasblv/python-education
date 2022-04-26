"""Module with decorated generator and logging"""

import logging

logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def decorator():
    """Decorator for fibonacci func"""
    def wrapper(func):
        try:
            logger.info('Fibonacci queue')
        except Exception as e:
            logger.info(e)
        return func
    return wrapper

@decorator()
def fib_num(num, a=0, b=1):
    """Return fibonacci array"""
    i = 0
    while i <= num:
        yield a
        i += 1
        a, b = b, a + b

if __name__=='__main__':
    f = fib_num(num=16)
    print([x**2 for x in f])
