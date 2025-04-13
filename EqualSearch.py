def equal_search(file_path: str, target_data: str, target_element: int) -> str:

    with open(file_path, 'r') as file:
        data_read = file.readlines()
        print('data read', data_read)

        data_list2 = []
        for i in data_read:
            data_list1 = i.split('.')
            data_list1[len(data_list1) - 1] = data_list1[len(data_list1) - 1].strip()
            data_list2.append(data_list1)
            print('data_list2', data_list2)
    for j in data_list2:
        for k in j:
            if k == target_data:
                target_list = j

                return target_list[target_element]


def data_write(data_write: str | list, file_path: str = './mylist') -> bool:
    """
    将数据写入指定文件
    
    Args:
        data_write: 要写入的数据，可以是字符串或列表
        file_path: 文件路径，默认为'./mylist'
    
    Returns:
        bool: 写入成功返回True，失败返回False
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            if isinstance(data_write, list):
                # 如果是列表，将元素用换行符连接
                content = '\n'.join(map(str, data_write))
                file.write(content)
            else:
                # 如果是字符串，直接写入
                file.write(str(data_write))
        return True
    except Exception as e:
        print(f"写入文件时发生错误: {e}")
        return False


def modify_data(file_path: str, target_data: str, new_data: str) -> bool:
    """
    修改文件中的特定数据

    Args:
        file_path: str, 文件路径
        target_data: str, 要修改的目标数据
        new_data: str, 新的数据内容

    Returns:
        bool: 修改成功返回True，失败返回False
    """
    try:
        # 读取所有行
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 标记是否找到并修改了数据
        modified = False
        
        # 遍历每一行，查找并修改目标数据
        for i, line in enumerate(lines):
            data_list = line.strip().split('.')
            if target_data in data_list:
                # 找到目标数据所在的位置
                index = data_list.index(target_data)
                # 修改数据
                data_list[index] = new_data
                # 重新组合行数据
                lines[i] = '.'.join(data_list) + '\n'
                modified = True

        # 如果找到并修改了数据，写回文件
        if modified:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(lines)
            return True
        else:
            print(f"未找到目标数据: {target_data}")
            return False

    except Exception as e:
        print(f"修改文件时发生错误: {e}")
        return False


def delete_data(file_path: str, target_data: str) -> bool:
    """
    删除文件中的特定数据所在行

    Args:
        file_path: str, 文件路径
        target_data: str, 要删除的目标数据

    Returns:
        bool: 删除成功返回True，失败返回False
    """
    try:
        # 读取所有行
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 标记是否找到并删除了数据
        deleted = False
        
        # 保存未包含目标数据的行
        new_lines = []
        for line in lines:
            data_list = line.strip().split('.')
            if target_data not in data_list:
                new_lines.append(line)
            else:
                deleted = True

        # 如果找到并删除了数据，写回文件
        if deleted:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(new_lines)
            return True
        else:
            print(f"未找到目标数据: {target_data}")
            return False

    except Exception as e:
        print(f"删除数据时发生错误: {e}")
        return False

