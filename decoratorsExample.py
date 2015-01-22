def logger(func):
    def inner(*args, **kwargs):
        print "Argumen" ,args,kwargs
        return func(*args, **kwargs)
    return inner

@logger 
def add(a,b,c=2,d=3):
    return (a,b,c,d)

print add(1,2,d=222,c=3)