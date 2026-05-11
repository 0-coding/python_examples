sc = "a = b"
my_name_space = {}
my_name_space["b"] = "loaded from source code"
exec(sc, my_name_space)
print(my_name_space["a"])