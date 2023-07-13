from functools import wraps

def log_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """Bu wrapper fonksiyonunun dökümanıdır"""

        print(f"Method ismi {fn.__name__}")
        print(f"metod bilgisi: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_data
def add(x, y):
    """ Fonksiyona gönderilen 2 sayıyı toplar"""
    return x + y

add()


"""
wraps() decoratoru ile dışarıda çağırdığımız zaman metadayı kaybetmiyoruz
"""
print(add.__name__) 
print(add.__doc__)