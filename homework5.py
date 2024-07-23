immutable_var = tuple([1, "two", True])
print("Immutable tuple:", immutable_var)

#immutable_var[0] = 2 значения внутри кортежа нельзя изменить
#поскольку он является неизменяемым объектом

mutable_list = [1, "two", 2.5, True]
mutable_list[0] = 3
mutable_list[1] = "tree"
mutable_list[2] = 3.0
mutable_list[3]=False
mutable_list.append("mutable")
print("Mutable list:",mutable_list)