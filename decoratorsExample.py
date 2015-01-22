def makebold(func):
    def wrapped(*args,**kwargs):
        return "<b>" + func(*args,**kwargs) + "</b>"  
    return wrapped

def makeitalic(func):
    def wrapped(*args, **kwargs):
        return "<i>" + func(*args, **kwargs) + "</i>"  
    return wrapped


@makebold
@makeitalic
def text(num,name="hello"):
    return str(num)+" "+name

print text(2,name="sam")




print "-----------------"

def logger(func):
    def inner(*args, **kwargs):
        print "Argumen" ,args,kwargs
        return func(*args, **kwargs)
    return inner

@logger 
def add(a,b,c=2,d=3):
    return (a,b,c,d)

print add(1,2,d=222,c=3)