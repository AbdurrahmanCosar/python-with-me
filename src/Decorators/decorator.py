
# NORMAL
def say_hi(fnc):
    def wrapper():
        print("Hi")
        fnc()
    return wrapper


def morning():
    print("good morning")

m = say_hi(morning)
m()


# DECORATORS
def say_hi(fnc):
    def wrapper(name):
        print("Hi")
        fnc(name)
    return wrapper

@say_hi
def morning(name):
    print("good morning " + name)
morning("Abduley")