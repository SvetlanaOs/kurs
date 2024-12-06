class MyClass():
    x = 1

    def func3(x):
        pass


def introspection_info(obj):
    info = {}
    info ['type'] = type(obj).__name__
    info ['attributes'] = [a for a in dir(obj) if not callable(getattr(obj,a)) and a[:2]!='__']
    info ['methods'] = [method for method in dir(obj) if callable(getattr(obj,method))]
    info['module'] = obj.__class__.__module__
    info ['id'] = id(obj)


    return info

number_info = introspection_info(42)
print(number_info)
number_info2 = introspection_info('ho-ho-ho')
print(number_info2)
number_info3 = introspection_info(introspection_info)
print(number_info3)
obj_class = MyClass()
number_info4 = introspection_info(obj_class)
print(number_info4)


