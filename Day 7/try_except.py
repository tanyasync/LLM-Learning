def to_int(text):
    try:
        return int(text)
    except ValueError:
        return None
    
print(to_int(42))
print(to_int("ABC"))

def safe_divide(a,b):
    try:
        result =a/b
    except ZeroDivisionError:
        print(f"{a}/{b}: cannot divide by zero")
    else:
        print(f"{a}/{b}={result}") #runs only if no exce
    finally:
        print("its done") #finally always runs