sc = "a=b"
my_name_space = {"b": 1}
exec(sc, my_name_space)
print(my_name_space['a'])