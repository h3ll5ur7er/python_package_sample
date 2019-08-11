from .some_module import func1
from .mypack.another_module import func2

def entry():
    a = ["a"]
    kw = { "b": "c" }
    func1(*a, **kw)
    func2(*a, **kw)
