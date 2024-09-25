def calculate_structure_sum(data_structure):
    if len(data_structure) == 0:
        return 0
    elif isinstance(data_structure[0],int):
        return data_structure[0] + calculate_structure_sum(data_structure[1:])
    elif isinstance(data_structure[0],str):
        return len(data_structure[0])+calculate_structure_sum(data_structure[1:])
    elif isinstance(data_structure[0],list):
        return calculate_structure_sum(data_structure[0])+calculate_structure_sum(data_structure[1:])
    elif isinstance(data_structure[0],set):
        return calculate_structure_sum(list(data_structure[0]))+calculate_structure_sum(data_structure[1:])
    elif isinstance(data_structure[0],dict):
        x = list(data_structure[0].keys())
        y = list(data_structure[0].values())
        return (calculate_structure_sum(x) + calculate_structure_sum(y) + calculate_structure_sum(data_structure[1:]))
    elif isinstance(data_structure[0], tuple):
        return calculate_structure_sum(data_structure[0]) + calculate_structure_sum(data_structure[1:])

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((),[{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)