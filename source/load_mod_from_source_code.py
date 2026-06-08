sc = "a = 'loaded from source code'"
my_name_space = {}
exec(sc, my_name_space)
print(my_name_space['a'])