from functools import wraps


def my_decorator(f):
      # commend this line and check whats the name :
      #it just is to have the function returned by decorator have the same attribuets example __name__
     @wraps(f)
     def wrapper(*args, **kwds):
         print 'Calling decorated function'
         return f(*args, **kwds)
     return wrapper

# print "done"
# @my_decorator


@my_decorator
def example():
    """Docstring"""
    print 'Called example function'
# example()

print example.__name__
