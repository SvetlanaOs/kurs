#словарь
my_dist={'Slava':1974,'Sveta':1976,'Grigory':2002,'Polina':2007}
print(my_dist)
print(my_dist['Slava'])
print(my_dist.get('Yrik','Такого ключа нет'))
my_dist['Yrik']=2015
my_dist.update({'Nina':1952})
a=my_dist.pop('Sveta')
print(a)
print(my_dist)
#множество
my_set={'Печворк',0.8,3,3,1,2,3}
print(my_set)
my_set.add((1, 2, 3))
my_set.add(False)
my_set.discard(1)
print(my_set)