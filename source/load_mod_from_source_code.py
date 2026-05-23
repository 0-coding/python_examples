sc = "a=b"
my_name_space = {"b": "b"}
exec(sc, my_name_space)
print(my_name_space['a'])
