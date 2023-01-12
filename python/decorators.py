#%%
import pandas as pd
import numpy as np

#%%
def memoize(func):
    """Store the results of the decorated function for fast lookup
    """
    # Store results in a dict that maps arguments to results
    cache = {}
    #Define the wrapper function to return
    def wrapper(*args):
        # If these arguments haven't been seen before
        if (args) not in cache:
            # Call func() and store the results
            cache[(args)] = func(*args)
        return cache[(args)]
    return wrapper

@memoize
def suma(a,b):
    a = int(a)
    b = int(b)
    return a+b

suma('1','2')
suma('3','5')
suma('1','2')

#%%
def print_return_type(func):
  # Define wrapper(), the decorated function
  def wrapper(*args, **kwargs):
    # Call the function being decorated
    result = func(*args, **kwargs)
    print('{}() returned type {}'.format(
      func.__name__, type(result)
    ))
    return result
  # Return the decorated function
  return wrapper
  
@print_return_type
def foo(value):
  return value
  
print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))


# %%
def counter(func):
  def wrapper(*args, **kwargs):
    wrapper.count += 1
    # Call the function being decorated and return the result
    return func(*args, **kwargs)
  wrapper.count = 0
  # Return the new decorated function
  return wrapper

# Decorate foo() with the counter() decorator
@counter
def foo():
  print('calling foo()')
  
foo()
foo()

print('foo() was called {} times.'.format(foo.count))
# %%
# # # To conserve the metadata
# # Trying to get docstring
# function.__doc__ -> will return wrapper docstring
# # To get wrapped function
# decorator.__wrapped__ - > returns original function

# To get metadata of function of interest, use @wraps
from functools import wraps

def add_hello(func):
  # Decorate wrapper() so that it keeps func()'s metadata
  @wraps(func)
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper
  
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

# %%
# Creating decorators that take arguments
# Example: create a decorator that will raise an error
# if the function takes longer than expected
import signal
import time
from functools import wraps

def raise_timeout(*args, **kwargs):
    raise TimeoutError()

# When an 'alarm' signal goes off, call raise_timeout()
signal.signal(signalnum=signal.SIGALRM, handler=raise_timeout)

#Set off alarm in 5 sec
signal.alarm(5)

# Cancel alarm
signal.alarm(0)

def timeout(n_seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs): 
            #set alarm for n seconds
            signal.alarm(n_seconds)
            try:
                # Call the decorated func
                return func(*args, **kwargs)
            finally:
                # Cancel alarm
                signal.alarm(0)
        return wrapper
    return decorator

print('hello!')

@timeout(5)
def foo():
    time.sleep(10)
    print('foo!')
foo()

@timeout(5)
def bar():
    time.sleep(3)
    print('bar!')
bar()


# %%
'''Tagging something means that you have given that thing one or more strings that act as labels. For instance, we often tag emails or photos so that we can search for them later. You've decided to write a decorator that will let you tag your functions with an arbitrary list of tags. You could use these tags for many things:

- Adding information about who has worked on the function, so a user can 
look up who to ask if they run into trouble using it.
- Labeling functions as "experimental" so that users know that the inputs 
and outputs might change in the future.
- Marking any functions that you plan to remove in a future version of the 
code.
Etc.'''
def tag(*tags):
  # Define a new decorator, named "decorator", to return
  def decorator(func):
    # Ensure the decorated function keeps its metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
      # Call the function being decorated and return the result
      return func(*args, **kwargs)
    wrapper.tags = tags
    return wrapper
  # Return the new decorator
  return decorator

@tag('test', 'this is a tag')
def foo():
  pass

print(foo.tags)
# %%
'''Check the return type'''

def returns(return_type):
    # Complete the returns() decorator
    def decorator(func):
        def wrapper(*args, **kwargs):
          result = func(*args, **kwargs)
          assert type(result) == return_type
          return result
        return wrapper
    return decorator
    
@returns(dict)
def foo(value):
    return value

try:
    print(foo([1,2,3]))
except AssertionError:
    print('foo() did not return a dict!')
# %%
# Timeing a function
import time
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print ('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed

@timeit
def get_all_employee_details(**kwargs):
    print('employee details')

get_all_employee_details()