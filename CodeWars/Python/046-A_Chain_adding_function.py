# FYA Best practice
class add(int):
    def __call__(self, n):
        return add(self+n)

# FYI: more detailed way
# class add(object):
#     def __init__(self, arg):
#         self.arg = arg

#     def __call__(self, arg):
#         self.arg += arg
#         return self

#     def __repr__(self):
#         return repr(self.arg)

# FYI: by function, but need to adding call add(1)(2)(3)() to get value
# def add(v):
#     def _inner_adder(val=None):  
#         """ 
#         if val is None we return _inner_adder.v 
#         else we increment and return ourselves
#         """
#         if val is None:    
#             return _inner_adder.v
#         _inner_adder.v += val
#         return _inner_adder
#     _inner_adder.v = v  # save value
#     return _inner_adder