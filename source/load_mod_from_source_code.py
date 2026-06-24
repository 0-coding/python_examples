sc = "b = 'loaded value'\na = b"
my_name_space = {}
exec(sc, my_name_space)
print(my_name_space['a'])