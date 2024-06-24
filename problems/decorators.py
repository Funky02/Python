
def greet (fx):
    def mfx():
        print("hello mama vachinava iga ")
        fx()
        print("sal iga po mala raku")
    return mfx
@greet
def hello():
    print("kusooo")
    
hello()