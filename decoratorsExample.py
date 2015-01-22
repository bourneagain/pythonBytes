def makebold(func):
    def wrapped():
        return "<b>" + func() + "</b>"  
    return wrapped

def makeitalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"  
    return wrapped


@makebold
@makeitalic
def text():
    return "hello"

print text()






def logger(func):
    def inner(*args, **kwargs):
        print "Argumen" ,args,kwargs
        return func(*args, **kwargs)
    return inner

@logger 
def add(a,b,c=2,d=3):
    return (a,b,c,d)

print add(1,2,d=222,c=3)