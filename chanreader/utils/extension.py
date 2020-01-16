
def get_function(obj, func_name):
    try:
        func = getattr(obj, func_name)
        return func
    except AttributeError:
        return None
