immutable_var=('Svetlana',48,[9,16,22])
print(immutable_var)
#immutable_var[2]=25
#изменить нельзя( ,т.к. кортеж неизменяемый тип
immutable_var [2] [1] = 17 #а так можно)
print(immutable_var)
mutable_list=['Svetlana',48,[9,16,22]]
mutable_list[1]=25
mutable_list.append('Karelia')
mutable_list.remove('Svetlana')
print(mutable_list)
