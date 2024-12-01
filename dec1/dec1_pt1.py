
def list_diff(list1, list2):
    total = 0
    ziperator = zip(sorted(list1), sorted(list2))
    for ele_list1, ele_list2 in ziperator:
        diff = abs(ele_list1 - ele_list2)
        total += diff

    return total


if __name__ == '__main__':
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]

    result = list_diff(list1, list2)
    print(result)

    list1_input = []
    list2_input = []

    with open('input.txt', 'r') as file:
        for file_line in file:
            ele_list1, ele_list2 = filter(None, file_line.split(' '))
            list1_input.append(int(ele_list1))
            list2_input.append(int(ele_list2))

    input_result = list_diff(list1_input, list2_input)
    print(input_result)

