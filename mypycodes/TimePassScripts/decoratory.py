def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return"<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper


def text(name):
    return "your name is {0}".format(name)




print p_decorate(text)("mani")


list_separator(queryconstructor(soicommand)