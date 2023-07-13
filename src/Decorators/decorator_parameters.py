
# DECORATOR ARGUMENTS
def do_twice(fnc):

    def wrapper_do_twice(*args, **kwargs): # Birden çok parametre göndermek için
        fnc(*args, **kwargs)
        fnc(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def greet(msg):
    print("hello " + msg)

# RETURN FUNCTION IN WRAPPER

def do_twice(fnc):

    def wrapper_do_twice(*args, **kwargs): # Birden çok parametre göndermek için
        return fnc(*args, **kwargs)
        return fnc(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def return_greeting(msg):
    print("return greeting function")
    return "hello " + msg

return_greeting("Abduley")
print(return_greeting("Abduley"))