def equal_search(file_path:str,target_data:str,target_element:int) -> str:

    with open(file_path, 'r') as file:
        data_read = file.readlines()
        print('data read',data_read)
       
        data_list2 = []
        for i in data_read:
            data_list1 = i.split('.')
            data_list1[len(data_list1)-1] = data_list1[len(data_list1)-1].strip()
            data_list2.append(data_list1)
            print('data_list2',data_list2)

    for j in data_list2:
        for k in j:
            if k == target_data:
                target_list = j

                return target_list[target_element]

def data_write(data_write):
    with open('./mylist','w') as file:
        file.write(data_write)

