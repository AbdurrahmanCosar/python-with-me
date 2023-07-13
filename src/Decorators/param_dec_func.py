def dec_do_twice(count):
    def do_twice(fnc):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                fnc(*args, **kwargs)
        return wrapper
    return do_twice

@dec_do_twice(count=3)
def hello():
    print("hello")

hello()

