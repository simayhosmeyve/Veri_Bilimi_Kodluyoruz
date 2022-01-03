ex_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(my_list):
    new_list = []
    
    for i in my_list:
        if type(i) is my_list:
            new_list.extend(flatten(i))
        else:
            new_list.append(i)
    return new_list


print(flatten(ex_list))