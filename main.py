from typing import ParamSpecArgs


def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    if n==0:
      return 0
    elif n==1:
      return 1
    else:
      counts[n] += 1
      return fib_recursive(n-1,counts) + fib_recursive(n-2, counts)
    ###TODO
    pass

    
def fib_top_down(n, fibs):
    if fibs[n] != -1:
      return fibs[n]
    elif n==0:
      return n
    elif n==1:
      return 1
    fibs[n] = fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)
    return fibs[n]
   
    ###TODO
    pass


def fib_bottom_up(n):
    if n <= 1:
      return n
    fib = [0] * (n+1)
    fib[1] = 1
    for i in range(2, n + 1):
      fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]
  ###TODO
    pass



