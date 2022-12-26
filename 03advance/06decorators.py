'''
decorators: A decorator takes a function as an argument, and adds some functionality
to the exisiting code and returns a function
'''

def basic():
    print("I am a basic function")

# basic()

def add_feature(func):
    def wrapper():
        print("="*50)
        print("A new feature is added")
        print("="*50)
        func() #basic
    return wrapper

new_feature = add_feature(basic) #wrapper
new_feature() #-> wrapper()

@add_feature
def new_basic():
    print("I am new basic function")

new_basic()