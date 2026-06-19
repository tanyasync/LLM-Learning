# runtime_errors

def show(label, func):
    try:
        func()
    except Exception as e:
        print(f"{label:<20} -> {type(e).__name__}: {e}")


show("NameError", lambda: eval("undefined_variable"))
show("TypeError", lambda: "3" + 5)
show("ValueError", lambda: int("abc"))
show("IndexError", lambda: [1, 2, 3][10])
show("KeyError", lambda: {"a": 1}["b"])
show("ZeroDivisionError", lambda: 1 / 0)
show("AttributeError", lambda: "hello".push("!"))
show("FileNotFoundError", lambda: open("does_not_exist_12345.txt"))

print()