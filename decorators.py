def announce(f):
    def wrapper():
        print("starting ...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("hello, world!")



hello()