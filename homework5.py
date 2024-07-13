immutable_var=(1,2,3, 'a', True)
print(immutable_var)
immutable_var[0]=2
print(immutable_var)#не выведет, так как кортеж нельзя изменить
mutable_list=[1,2,'a', 'c', 5, True]
print(mutable_list)
mutable_list[0]=5
print(mutable_list)