def data_write(data_write):
    with open('./mylist','w') as file:
        file.write(data_write)

def equal_search(file_path,target_data,target_element):

    with open(file_path, 'r') as file:
        data_read = file.readlines()
        print(data_read)
        data_list2 = []

        for i in data_read:
            data_list1 = i.split('.')
            data_list2.append(data_list1)
            print(data_list2)

    for j in data_list2:

        for k in j:
            if k == target_data:
                target_list = j

    return target_list[target_element]
print(equal_search('23',2))