data = ['A', 2, 3, 'A', 'K', 5, 6, 7, 7, 'A', 8, 10, 'A', 'J', 2, 3, 10, 'K', 'Q', 'J']


def change_to_values(sample_list):
    pairs_in = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}

    temp_list = []
    for elem in sample_list:
        if elem in pairs_in.keys():
            temp_list.append(pairs_in[elem])
        else:
            temp_list.append(elem)
    return temp_list


def change_back_to_signs(sample_list):
    pairs_out = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}

    temp_list = []
    for elem in sample_list:
        if elem in pairs_out.keys():
            temp_list.append(pairs_out[elem])
        else:
            temp_list.append(elem)
    return temp_list


def my_sort(sample_list):
    try:
        assert all(elem in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] for elem in sample_list)
    except AssertionError:
        return "Niedozwolone elementy na liście"
    else:
        temp_list = change_to_values(sample_list)
        temp_list = sorted(temp_list)
        result_list = change_back_to_signs(temp_list)
        return result_list

print(my_sort(data))

