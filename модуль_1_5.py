immutable_var = 1, 2, 'apple', True, 'work', 7,
print(immutable_var)

# immutable_var[1] = 'rom'
# #TypeError: 'tuple' object does not support item assignment
#Кортежи неизменяемы.
# После создания кортежа значение какого-либо его элемента уже нельзя изменить,
# как нельзя добавлять и удалять элементы.
immutable_var = [1, 2, 'apple', True, 'work', [7, 8], True]
mutable_list = [1, 2, 'apple', True, 'work', [7, 8], True]
mutable_list[3] = 'Яблоко'
mutable_list[0] = 'one'
print(mutable_list)
