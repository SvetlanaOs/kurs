def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(2,4)
print_params(c = [1,2,3])
values_list = [25,'yes',234]
values_dist = {'a':2,'b':3,'c':4}
print_params(*values_list)
print_params(**values_dist)
values_list_2 = [54.32, 'строка']
print_params(*values_list_2, 42)