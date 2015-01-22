def logger(func):
    def inner(*args, **kwargs):
        print "Argumen" ,args,kwargs
        return func(*args, **kwargs)
    return inner

@logger ;# commnet this and try
def add(a,b):
    return a+b

print add(1,2)