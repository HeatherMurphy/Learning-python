def singleton(C):
    instances = {}
    def getInstance(*args, **kwargs):
        if C not in instances:
            instances[C]= C(*args,**kwargs)
        return instances[C]
    return getInstance

@singleton
class TestClass(object):
    pass

TestClass()
