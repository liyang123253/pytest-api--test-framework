import openpyxl


def read_excel():
    # 打开excel文件
    workbook = openpyxl.load_workbook("../data/测试用例.xlsx") #excel文件路径
    # 选择表
    worksheet = workbook["Sheet1"]

    # 读取数据,通过zip()函数可以将excel文件中的数据以键值对的方式输出然后存放到一个空列表中
    # 定义一个空列表，用于组装列表
    data = []
    keys = [cell.value for cell in worksheet[2]] #拿第二行

    for row in worksheet.iter_rows(min_row=3,values_only=True): #从第三行开始拿，并且只拿cell里面的值
        dict_data = dict(zip(keys,row)) #将拿到的值通过zip()函数组装，并强转为dict
        if dict_data["is_true"]:
            data.append(dict_data) #添加到空的data列表中
    # print(data)


    # 关闭excel文件
    workbook.close()
    return data

# read_excel()

