ex_list = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(my_list):
    new_list = []
    
    for i in range(0, len(my_list)):
        new_list.append(my_list[len(my_list)-i-1][::-1])
    return new_list


print(reverse(ex_list))