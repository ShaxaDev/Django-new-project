def add(func):
    def new_ex(*args,**kwargs):
        args=map(int,args)
        return func(*args,**kwargs)
    return new_ex

@add
def my(*args):
    print(sum(list(args)))
a=[i for i in range(1,2111111111111)]
my(*a)